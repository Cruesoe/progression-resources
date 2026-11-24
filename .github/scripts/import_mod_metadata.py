"""Supplement the catalog from a synced reference index without another Steam snapshot."""
import argparse
import json
import re

import apply_weekly_snapshot as snapshot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('index', help='Path to the synced Progression index.json')
    args = parser.parse_args()
    with open(args.index, encoding='utf-8') as handle:
        index = {str(row['WorkshopId']): row for row in json.load(handle)}
    overlay_path = snapshot.ROOT / 'backup/packageids_overlay.json'
    overlay = json.loads(overlay_path.read_text(encoding='utf-8'))
    html = snapshot.HTML.read_text(encoding='utf-8')
    data = snapshot.load_data(html)
    titles = 0
    for item in data['items']:
        source = index.get(item['id'], {})
        if source.get('PackageId'):
            item['p'] = overlay[item['id']] = source['PackageId']
        if item['t'].startswith(('(unavailable ', 'Workshop item ')):
            item['t'] = source.get('Name') or f"Workshop item {item['id']}"
            titles += bool(source.get('Name'))
    html = re.sub(r'const DATA = \{.*?\};\s*\n', lambda _: 'const DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n', html, count=1, flags=re.S)
    have, total = sum(bool(item.get('p')) for item in data['items']), len(data['items'])
    html = re.sub(r'\s*packageId from RimSort steamDB: \d+ of \d+\.', '', html)
    html = re.sub(r'Known packageIds(?: \(RimSort \+ previous overlay\))?: \d+ of \d+\.', f'Known packageIds: {have} of {total}.', html)
    snapshot.HTML.write_text(html, encoding='utf-8')
    overlay_path.write_text(json.dumps(overlay, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    readme = snapshot.README.read_text(encoding='utf-8')
    readme = re.sub(r'\*\*packageId coverage:.*?\*\*', f'**packageId coverage: {have} of {total}**', readme)
    readme = re.sub(r'\*\*packageId from RimSort steamDB:.*?\*\*\s*', '', readme)
    readme = re.sub(r'\*\*Known packageIds.*?\*\*', f'**Known packageIds: {have} of {total}**', readme)
    iso_date, display_date = re.search(r'<time datetime="([^"]+)">([^<]+)</time>', html).groups()
    readme = re.sub(r'- packageIds filled .*', f'- packageIds filled {iso_date}', readme)
    snapshot.README.write_text(readme, encoding='utf-8')
    snapshot.write_backups(data, display_date)
    print(f'Catalog metadata: {have}/{total} package IDs; {titles} unlisted titles restored.')


if __name__ == '__main__':
    main()
