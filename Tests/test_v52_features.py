import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
JS = (ROOT / "v50-enhancements.js").read_text(encoding="utf-8")
SW = (ROOT / "sw.js").read_text(encoding="utf-8")


class V52BehaviorRegressionTests(unittest.TestCase):
    def test_player_indicator_is_no_longer_under_main_game_progress(self):
        self.assertNotIn('<div id="v51-current-player"', HTML)
        self.assertIn("const player=profiles.find(p=>p.id===activeProfileId)", JS)
        self.assertIn("box.innerHTML=playerMarkup", JS)

    def test_active_player_is_rendered_in_scoreboard_panel(self):
        self.assertIn("el('v50-team-scoreboard')", JS)
        self.assertIn("Jucător activ:", JS)
        self.assertIn("showPlayer=profiles.length>1", JS)

    def test_team_mode_button_has_failure_label(self):
        self.assertIn("Nu am reușit", JS)
        self.assertIn("I couldn’t do it", JS)
        self.assertIn("skip.innerHTML", JS)

    def test_failed_challenge_advances_team_without_scoring(self):
        block = re.search(
            r"/\* V52: failed team challenge.*?\*/\s*el\('skip-challenge'\)\.addEventListener\('click',e=>\{(.*?)\},true\);",
            JS, re.S
        )
        self.assertIsNotNone(block)
        body = block.group(1)
        self.assertIn("teamData.turn=(teamData.turn+1)%teamData.teams.length", body)
        self.assertIn("saveTeamData()", body)
        self.assertNotIn("team.score", body)
        self.assertNotIn("score+", body)

    def test_success_scoring_remains_on_success_button(self):
        self.assertIn("e.target.closest('#adaptive-action')", JS)
        self.assertIn("team.score=(Number(team.score)||0)+1", JS)

    def test_release_version_is_52(self):
        self.assertIn('content="52"', HTML)
        self.assertIn("princess-kingdom-v52-release", SW)
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "52")
        self.assertEqual(json.loads((ROOT / "version.json").read_text())["version"], "52")


if __name__ == "__main__":
    unittest.main()
