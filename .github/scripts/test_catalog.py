import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import apply_weekly_snapshot as snapshot


class CatalogRefreshTests(unittest.TestCase):
    def test_unlisted_title_and_local_package_id_survive_refresh(self):
        data = {'cats': ['Gameplay tweaks'], 'items': [{'id': '123', 't': 'Unlisted mod', 'c': 'Gameplay tweaks', 'p': ''}]}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'backup').mkdir()
            (root / 'backup/packageids_overlay.json').write_text('{"123":"example.mod"}')
            with patch.object(snapshot, 'ROOT', root), patch.object(snapshot, 'collection_ids', return_value={'123'}), patch.object(snapshot, 'published_details', return_value={'123': {'result': 9}}):
                result, _ = snapshot.refresh_items(data)
        item = result['items'][0]
        self.assertEqual(item['t'], 'Unlisted mod')
        self.assertEqual(item['p'], 'example.mod')
        self.assertTrue(item['metadataUnavailable'])
        self.assertNotIn('gone', item)

    def test_readme_coverage_updates_with_the_catalog(self):
        data = {'items': [{'p': 'example.mod', 'core': True, 'content': False, 'cosmetics': False}]}
        changes = {key: [] for key in ('added', 'removed', 'renamed', 'newly_unavailable')}
        result = snapshot.update_readme('**packageId coverage: 4 of 5**', data, changes, '24 November 2026')
        self.assertEqual(result, '**packageId coverage: 1 of 1**')

    def test_json_escapes_survive_html_replacement(self):
        data = {'items': [{'t': 'A\\B\nC', 'p': ''}]}
        changes = {key: [] for key in ('added', 'removed', 'renamed', 'newly_unavailable')}
        result = snapshot.update_html('const DATA = {};\n', data, changes, '2026-11-24', '24 November 2026')
        self.assertEqual(snapshot.load_data(result), data)


if __name__ == '__main__':
    unittest.main()
