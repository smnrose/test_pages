from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
STYLESHEET = ROOT / "styles.css"
README = ROOT / "README.md"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.fragments = set()
        self.text_parts = []
        self.tags = set()

    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        href = attributes.get("href", "")
        if tag == "a" and href.startswith("#"):
            self.fragments.add(href)

    def handle_data(self, data):
        self.text_parts.append(data)

    @property
    def text(self):
        return " ".join(" ".join(self.text_parts).split())


class SiteContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = INDEX.read_text(encoding="utf-8") if INDEX.is_file() else ""
        cls.page = SiteParser()
        cls.page.feed(cls.source)

    def test_has_german_document_title_and_mobile_viewport(self):
        self.assertIn('<html lang="de">', self.source)
        self.assertIn("<title>", self.source)
        self.assertIn('name="viewport"', self.source)

    def test_category_anchors_target_existing_sections(self):
        self.assertTrue({"klassiker", "express", "videothek"} <= self.page.ids)
        self.assertTrue(
            {"#klassiker", "#express", "#videothek"} <= self.page.fragments
        )
        self.assertTrue(
            self.page.fragments <= {f"#{target}" for target in self.page.ids}
        )

    def test_primary_clue_points_from_hero_to_vip_pear(self):
        self.assertIn("Kurierkontakt steckt bei den Klassikern", self.page.text)
        self.assertIn("VIP-Birne", self.page.text)

    def test_contact_and_video_are_explicit_placeholders(self):
        self.assertIn("@TELEGRAM-PLATZHALTER", self.page.text)
        self.assertIn("AI-Slop-Clip folgt", self.page.text)
        self.assertNotIn("video", self.page.tags)

    def test_video_placeholder_has_no_play_affordance(self):
        self.assertNotIn("▶", self.page.text)
        self.assertNotIn("button", self.page.tags)

    def test_readme_documents_preview_and_github_pages(self):
        readme = README.read_text(encoding="utf-8") if README.is_file() else ""
        self.assertIn("python3 -m http.server 8000 --bind 127.0.0.1", readme)
        self.assertIn("Settings → Pages", readme)
        self.assertIn("Deploy from a branch", readme)
        self.assertIn("main", readme)
        self.assertIn("/ (root)", readme)
        self.assertIn("https://<owner>.github.io/test_pages/", readme)


class StylesheetContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.styles = (
            STYLESHEET.read_text(encoding="utf-8") if STYLESHEET.is_file() else ""
        )

    def test_stylesheet_has_a_narrow_single_column_layout(self):
        self.assertRegex(self.styles, r"@media\s*\(max-width:\s*\d+px\)")
        self.assertRegex(self.styles, r"grid-template-columns:\s*1fr")

    def test_navigation_has_visible_keyboard_focus(self):
        self.assertRegex(self.styles, r":focus-visible\s*\{[^}]*outline\s*:")

    def test_stylesheet_has_no_remote_assets_or_animation(self):
        self.assertTrue(self.styles.strip(), "styles.css is missing")
        self.assertNotRegex(self.styles, r"@import|url\(\s*['\"]?https?://")
        self.assertNotRegex(self.styles, r"animation\s*:")

    def test_small_text_on_pink_background_meets_contrast_target(self):
        variables = dict(
            re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;", self.styles)
        )

        def value_for(selector, property_name):
            match = re.search(
                rf"(?m)^{re.escape(selector)}\s*\{{([^}}]*)\}}", self.styles
            )
            self.assertIsNotNone(match, f"Missing CSS rule for {selector}")
            declaration = re.search(
                rf"{re.escape(property_name)}\s*:\s*([^;]+);", match.group(1)
            )
            self.assertIsNotNone(
                declaration, f"Missing {property_name} for {selector}"
            )
            color = declaration.group(1).strip()
            return variables.get(color[4:-1], color) if color.startswith("var(") else color

        def luminance(color):
            if re.fullmatch(r"#[0-9a-fA-F]{3}", color):
                color = "#" + "".join(channel * 2 for channel in color[1:])
            self.assertRegex(color, r"^#[0-9a-fA-F]{6}$")
            channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
            linear = [
                channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
                for channel in channels
            ]
            return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

        pink = variables["--pink"]
        for selector in (".site-stamp", ".hero-label", ".contact-section"):
            with self.subTest(selector=selector):
                foreground = value_for(selector, "color")
                background = value_for(selector, "background")
                self.assertEqual(background, pink)
                foreground_luminance = luminance(foreground)
                background_luminance = luminance(background)
                contrast = (max(foreground_luminance, background_luminance) + 0.05) / (
                    min(foreground_luminance, background_luminance) + 0.05
                )
                self.assertGreaterEqual(contrast, 4.5)

        with self.subTest(selector=".contact-section .section-number"):
            foreground = value_for(".contact-section .section-number", "color")
            foreground_luminance = luminance(foreground)
            background_luminance = luminance(pink)
            contrast = (max(foreground_luminance, background_luminance) + 0.05) / (
                min(foreground_luminance, background_luminance) + 0.05
            )
            self.assertGreaterEqual(contrast, 4.5)


if __name__ == "__main__":
    unittest.main()
