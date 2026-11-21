import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
SW = (ROOT / "sw.js").read_text(encoding="utf-8")
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
BANK_MATCH = re.search(r"const PRINCESS_BANK=(\[.*?\]);", HTML, re.S)
assert BANK_MATCH, "PRINCESS_BANK was not found"
PRINCESS_BANK = json.loads(BANK_MATCH.group(1))


class PrincessReleaseTests(unittest.TestCase):
    def test_exactly_150_challenges_and_50_per_category(self):
        self.assertEqual(len(PRINCESS_BANK), 150)
        counts = {}
        for challenge in PRINCESS_BANK:
            counts[challenge["cat"]] = counts.get(challenge["cat"], 0) + 1
        self.assertEqual(sorted(counts.values()), [50, 50, 50])

    def test_all_challenge_ids_are_present_and_unique(self):
        ids = [item["id"] for item in PRINCESS_BANK]
        self.assertTrue(all(isinstance(value, str) and value for value in ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_50_subjects_have_50_explicit_image_paths(self):
        images = {item.get("image") for item in PRINCESS_BANK}
        self.assertEqual(len(images), 50)
        for image in images:
            self.assertTrue(image and image.startswith("./"))
            self.assertTrue((ROOT / image[2:]).is_file(), f"Missing image: {image}")

    def test_each_subject_has_three_category_challenges(self):
        grouped = {}
        for challenge in PRINCESS_BANK:
            grouped.setdefault(challenge["image"], []).append(challenge)
        self.assertEqual(len(grouped), 50)
        self.assertTrue(all(len(items) == 3 for items in grouped.values()))

    def test_fallback_exists_and_is_used_on_image_error(self):
        self.assertTrue((ROOT / "princess-fallback.svg").is_file())
        self.assertIn("this.onerror=null", HTML)
        self.assertIn("princess-fallback.svg", HTML)

    def test_image_lookup_uses_explicit_paths_not_name_substrings(self):
        self.assertIn("person.image", HTML)
        self.assertNotIn("photoMap", HTML)
        self.assertNotIn("lower.includes(key)", HTML)

    def test_album_unlocks_only_after_three_challenges(self):
        self.assertIn("ids.length===3&&ids.every(id=>done.has(id))", HTML)
        self.assertIn("princess-album-open", HTML)
        self.assertIn("princess-album-grid", HTML)

    def test_progress_is_separate_for_both_modes(self):
        self.assertIn("function stateKey(style){return 'pk_game_'+style;}", HTML)
        self.assertIn("function statsKey(style){return 'pk_stats_'+style;}", HTML)

    def test_progress_export_uses_central_app_version(self):
        self.assertIn("version:Number(APP_VERSION)", HTML)
        self.assertNotIn("version:43", HTML)
        self.assertIn("application-version", HTML)

    def test_version_metadata_and_service_worker_match(self):
        version_json = json.loads((ROOT / "version.json").read_text(encoding="utf-8"))
        self.assertEqual(version_json["version"], VERSION)
        self.assertEqual((ROOT / "version.txt").read_text(encoding="utf-8").strip(), VERSION)
        self.assertRegex(HTML, rf'<meta name="application-version" content="{VERSION}">')
        self.assertIn(f"princess-kingdom-v{VERSION}-release", SW)

    def test_credits_record_all_50_subject_images(self):
        credits = (ROOT / "CREDITS.md").read_text(encoding="utf-8")
        for image in {item["image"] for item in PRINCESS_BANK}:
            self.assertIn(image[2:], credits)
        self.assertTrue((ROOT / "artwork-source-princess-grid.png").is_file())

    def test_all_50_images_are_in_offline_precache(self):
        for image in {item["image"] for item in PRINCESS_BANK}:
            self.assertIn(image, SW)
        self.assertIn("./princess-fallback.svg", SW)


if __name__ == "__main__":
    unittest.main()
