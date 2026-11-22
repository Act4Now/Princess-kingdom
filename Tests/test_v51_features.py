import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'index.html').read_text(encoding='utf-8')
JS = (ROOT / 'v50-enhancements.js').read_text(encoding='utf-8')
SW = (ROOT / 'sw.js').read_text(encoding='utf-8')

class V51FeatureIntegrityTests(unittest.TestCase):
    def test_classic_base_bank_still_has_600_unique_challenges(self):
        match = re.search(r"const CLASSIC_BANK=(\[.*?\]);", HTML, re.S)
        self.assertIsNotNone(match)
        bank = json.loads(match.group(1))
        self.assertEqual(len(bank), 600)
        self.assertEqual(len({x['id'] for x in bank}), 600)

    def test_every_service_worker_asset_exists_locally(self):
        match = re.search(r"const APP_FILES = (\[.*?\]);", SW, re.S)
        self.assertIsNotNone(match)
        paths = json.loads(match.group(1))
        for path in paths:
            local = path.split('?', 1)[0]
            if local in ('./', './index.html'):
                continue
            self.assertTrue((ROOT / local.removeprefix('./')).is_file(), path)

    def test_drawing_gallery_has_search_and_sort(self):
        self.assertIn('id="v50-gallery-search"', HTML)
        self.assertIn('id="v50-gallery-sort"', HTML)
        self.assertIn("sort==='oldest'", JS)
        self.assertIn("sort==='title'", JS)

    def test_custom_challenges_support_edit_and_delete(self):
        self.assertIn('data-edit-custom', JS)
        self.assertIn('data-delete-custom', JS)

    def test_existing_enhancement_script_is_loaded_and_precached(self):
        self.assertIn('<script src="./v50-enhancements.js" defer></script>', HTML)
        self.assertIn('"./v50-enhancements.js"', SW)
        self.assertIn('princess-kingdom-v51-release', SW)

    def test_all_ten_feature_areas_are_present(self):
        for marker in [
            'Distinct, age-appropriate Princess Mode reflection quiz',
            'Optional charades timer',
            'Team play and',
            'Parent challenge editor',
            'Drawing gallery: IndexedDB',
            'Kingdom Adventure Map',
            'Printable certificates',
            'Comfort and accessibility settings',
            'Export/import include custom challenges',
        ]:
            self.assertIn(marker, JS)
        for control in ['v50-profile','v50-team-open','v50-timer-enabled','v50-adventure-open',
                        'v50-editor-open','v50-certificate-open','v50-text-size','v50-contrast',
                        'v50-reduced-motion','v50-speech-rate','v50-quiz']:
            self.assertIn(f'id="{control}"', HTML)

    def test_profile_snapshots_are_separate_by_player_and_mode(self):
        self.assertIn('pk-v50-profile-state:${id}:${style}', JS)
        self.assertIn('saveProfileSnapshot(oldStyle,activeProfileId)', JS)
        self.assertIn('profileSnapshotKey(activeProfileId,next)', JS)
        self.assertIn('v51-delete-profile', JS)
        self.assertIn('v51-current-player', HTML)
        self.assertIn('At least one player must remain', JS)

    def test_custom_challenges_are_exported_and_imported(self):
        self.assertIn('pk-v50-custom-challenges', JS)
        self.assertIn('customChallenges:readCustom(gameStyle)', JS)
        self.assertIn('data.customChallenges', JS)

    def test_gallery_uses_indexeddb_and_keeps_fallback(self):
        self.assertIn("indexedDB.open('princess-kingdom-artwork',1)", JS)
        self.assertIn("localStorage.getItem('pk-drawing-gallery')", JS)
        self.assertIn('v50GalleryItems.unshift', JS)

    def test_question_choices_are_not_falsely_marked_right_or_wrong(self):
        self.assertIn('There is no wrong answer', JS)
        self.assertIn('Nu există un răspuns greșit', JS)
        self.assertIn('aria-pressed', JS)

    def test_certificate_explains_print_to_pdf(self):
        self.assertIn('Save as PDF', JS)
        self.assertIn('window.print()', JS)

    def test_service_worker_precaches_all_local_v50_code(self):
        self.assertIn('./v50-enhancements.js', SW)
        self.assertIn('./index.html', SW)

    def test_release_metadata_is_v51(self):
        self.assertEqual((ROOT/'VERSION').read_text().strip(),'51')
        meta=json.loads((ROOT/'version.json').read_text())
        self.assertEqual(meta['version'],'51')
        self.assertEqual(meta['previous_version'],'50')
        self.assertIn('application-version" content="51',HTML)

if __name__=='__main__':
    unittest.main()
