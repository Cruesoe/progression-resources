"""Validate the published research data and its cross-page counts."""
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    tree = json.loads((ROOT / 'research/tree.json').read_text(encoding='utf-8'))
    summary = json.loads((ROOT / 'research/summary.json').read_text(encoding='utf-8'))
    catalog = (ROOT / 'catalog.html').read_text(encoding='utf-8')
    items = json.loads(re.search(r'const DATA = (\{.*?\});\s*\n', catalog, re.S)[1])['items']
    assert len(items) == summary['packMods'], 'Catalog and research pack counts differ'
    assert set(tree['editions']) == {'Progression', 'ProgressionLESS', 'Genesis'}
    for edition, data in tree['editions'].items():
        projects = [p for p in data['projects'] if not p.get('na') and p.get('ot')]
        assert projects and not data['meta'].get('pending'), edition
        assert not data['meta']['missing'], (edition, data['meta']['missing'])
        assert not data['meta'].get('parseErrors'), (edition, 'Unreadable XML')
        assert not data['meta']['patchErrors'], (edition, 'Patch exceptions')
        packages = data['meta']['packages']
        assert len(packages) == len(set(packages)), (edition, 'Duplicate loaded packages')
        assert len(projects) == summary['projects'][edition], edition
        by_def = {p['d']: p for p in projects}
        assert len(by_def) == len(projects), (edition, 'Duplicate projects')
        unresolved = []
        overlaps = []
        for layout in ('o', 'c'):
            occupied = {}
            for p in projects:
                coords = [p[layout + axis] for axis in ('x', 'y')]
                assert all(isinstance(n, (int, float)) and math.isfinite(n) for n in coords), (edition, p['d'])
                key = (p[layout + 't'], *coords)
                if key in occupied:
                    overlaps.append((layout, occupied[key], p['d']))
                occupied[key] = p['d']
        for p in projects:
            unresolved.extend((p['d'], dep) for dep in p.get('p', []) if dep not in by_def)
        assert not overlaps, (edition, 'Coincident cards', overlaps[:10])
        assert not unresolved, (edition, 'Unresolved prerequisites', unresolved[:20])
        print(f'{edition}: {len(projects)} projects; {len(unresolved)} unresolved prerequisites; '
              f'{len(data["meta"]["unknownOps"])} unsupported patch classes; '
              f'{data["meta"]["patchErrors"]} patch exceptions')
        if unresolved:
            print('  Unresolved:', unresolved[:20])
    print(f'Catalog: {len(items)} mods; counts agree with the home page.')


if __name__ == '__main__':
    main()
