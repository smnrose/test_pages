# Berliner Obsttaxi Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a grell, mobile-friendly single-page „Berliner Obsttaxi“ scavenger-hunt website that leads visitors from a category clue to a contact placeholder and can be hosted on GitHub Pages.

**Architecture:** Use one semantic `index.html` document for all content and anchor navigation, with a separate `styles.css` for the exaggerated visual style and responsive layout. Keep the contact and video as replaceable placeholders; use no backend, JavaScript, or third-party dependencies.

**Tech Stack:** HTML5, CSS3, GitHub Pages; no build step or dependencies.

**Spec:** `docs/superpowers/specs/2026-10-27-berliner-obsttaxi-site-design.md`

## Global Constraints

- Statische Website für GitHub Pages; keine Datenbank, kein Server und keine Konten.
- Kategorien verwenden interne Sprungmarken. HTML und CSS reichen für den beschriebenen Aufbau; JavaScript ist nur bei später ergänzter Interaktion nötig.
- Der Video-Platzhalter lässt sich später durch ein eingebettetes oder lokal bereitgestelltes Video ersetzen.
- Die Messenger-/Bot-Interaktion ist nicht Teil dieser Website-Spezifikation.
- Die Seite soll auf Smartphones funktionieren, da sie über eine Visitenkarte aufgerufen wird.
- Die Hinweise sind spielerisch versteckt, nicht als geheime Daten geschützt; sie können im Seitenquelltext sichtbar sein.
- Der Kontakt bleibt im Entwurf ein Platzhalter und wird später durch einen eigens für das Spiel vorgesehenen Kontakt ersetzt.

## Review Focus

- **Small-screen overflow:** At 320 CSS pixels, the page should remain readable without horizontal scrolling. Verify in Task 2 at 320px.
- **Broken category anchors:** Every category link should reach the intended section. Verify all links in Task 1.
- **Neon styling reducing readability:** Large headings may be decorative, but body copy and clues must remain legible. Verify contrast and text readability in Task 2.
- **Main clue too obscure or optional clues becoming required:** The hero should clearly direct visitors to the VIP-pear offer, whose text leads to the contact. Follow only this route in Task 1.
- **Placeholder mistaken for real contact/media:** The contact must visibly say it is a placeholder, and the video area must be labeled as coming later rather than implying a working player. Verify both in Task 1.

---

### Task 1: Create the semantic page and clue path

**Files:**
- Create: `tests/test_site.py`
- Create: `index.html`

**Interfaces:**
- Produces section IDs `klassiker`, `express`, `videothek`, and `kontakt` for navigation and later QA.
- Produces CSS classes `site-header`, `category-nav`, `hero`, `offer-grid`, `offer-card`, `video-placeholder`, and `contact-placeholder` for Task 2.
- The primary clue reads from the hero to a distinctive VIP-pear offer in `klassiker`, then directs visitors to the contact placeholder in `kontakt`.

- [ ] **Step 1: Write standard-library tests for the page contract**

Create `tests/test_site.py` using Python's built-in `unittest` and `html.parser.HTMLParser`. Have the parser collect element IDs, internal `href="#..."` targets, visible text, and whether a `<video>` element exists. Read `index.html` if present and use an empty string if it is absent, so the red run fails with assertions rather than a file error. Add these tests:

```python
def test_has_german_document_title_and_mobile_viewport(self):
    self.assertIn('<html lang="de">', self.source)
    self.assertIn("<title>", self.source)
    self.assertIn('name="viewport"', self.source)

def test_category_anchors_target_existing_sections(self):
    self.assertTrue({"klassiker", "express", "videothek"} <= self.page.ids)
    self.assertTrue({"#klassiker", "#express", "#videothek"} <= self.page.fragments)
    self.assertTrue(self.page.fragments <= {f"#{target}" for target in self.page.ids})

def test_primary_clue_points_from_hero_to_vip_pear(self):
    self.assertIn("Kurierkontakt steckt bei den Klassikern", self.page.text)
    self.assertIn("VIP-Birne", self.page.text)

def test_contact_and_video_are_explicit_placeholders(self):
    self.assertIn("@TELEGRAM-PLATZHALTER", self.page.text)
    self.assertIn("AI-Slop-Clip folgt", self.page.text)
    self.assertNotIn("video", self.page.tags)
```

Implement a small parser in the test module that fills `ids`, `fragments`, `text`, and `tags` from the HTML; do not add a third-party package.

- [ ] **Step 2: Run the tests and verify the expected red result**

Run:

```bash
python3 -m unittest discover -s tests -v
```

**Expected:** The test module imports successfully and the four contract tests fail with assertion failures because `index.html` has not been created yet. There are no import errors or test errors.

- [ ] **Step 3: Create the HTML document structure and copy**

Create `index.html` with a German document language, responsive viewport metadata, title, and a stylesheet link to `styles.css`. Use semantic `header`, `nav`, `main`, `section`, and `footer` elements. Include:

1. A `site-header` with the „Berliner Obsttaxi“ name and an exaggerated, clearly comic advert.
2. A `hero` with the direct clue: „Der Kurierkontakt steckt bei den Klassikern – frag die VIP-Birne, die weiß mehr.“
3. A `category-nav` with working links to `#klassiker`, `#express`, and `#videothek`.
4. An `offer-grid` with category sections. Under `klassiker`, include an absurd VIP-pear `offer-card` that says the courier's contact is at the bottom of the page. Include at least one extra joke/clue in another category, clearly optional to the main route.
5. A `videothek` section with a `video-placeholder` panel labeled „AI-Slop-Clip folgt“ and a note that its motif and media source are to be decided later. Do not add a fake play control.
6. A `kontakt` section with a `contact-placeholder` such as `@TELEGRAM-PLATZHALTER` and explanatory text that it is a game placeholder to replace later.

Do not add real contact details, working forms, or a bot integration.

- [ ] **Step 4: Run the tests and verify the page contract is green**

Run:

```bash
python3 -m unittest discover -s tests -v
```

**Expected:** All four contract tests pass, including anchor-target consistency and both placeholder labels.

- [ ] **Step 5: Run a local HTTP server and verify page structure and clue flow**

Run from the repository root:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/` in a browser. Click each category link and confirm it reaches a section with the corresponding ID. Follow the hero hint to the VIP-pear card and then to the contact placeholder without using the optional joke/clue. Confirm the contact says it is a placeholder and the video says it is not ready yet.

**Expected:** The document loads, all three category links land in the correct sections, and the intended clue route reaches the visibly fake contact placeholder.

### Task 2: Apply the vivid, responsive visual style

**Files:**
- Create: `styles.css`

**Interfaces:**
- Consumes the classes and section IDs defined in Task 1.
- Keeps category links, clue copy, video placeholder, and contact placeholder readable on desktop and mobile.

- [ ] **Step 1: Style the page with a deliberately over-the-top visual language**

Add CSS for a highly saturated palette, chunky borders, dramatic text shadows, slightly mismatched decorative rotations, and large WordArt-like headings. Use system fonts and CSS effects only; do not add external font or image dependencies. Give offer cards, the video placeholder, and the contact placeholder distinct visual treatments. Keep paragraph text and clues on solid or sufficiently opaque backgrounds with strong foreground/background contrast. Avoid animation that could distract from the clues.

- [ ] **Step 2: Add responsive layout rules**

Use a compact category row that wraps or scrolls without forcing page-wide overflow. Arrange offer cards in a multi-column grid at wide widths and a single column on narrow screens. Keep spacing, text sizes, and buttons/links comfortably usable by touch. Add a visible keyboard focus style for navigation links.

- [ ] **Step 3: Verify desktop and mobile presentation**

With the local server from Task 1 running, inspect `http://127.0.0.1:8000/` at 1440px, 390px, and 320px viewport widths. At each width, check title and clue readability, category navigation, cards, video panel, contact placeholder, and keyboard focus. At 320px, confirm no horizontal page scrolling. At all widths, follow the primary clue and ensure no optional content is needed.

**Expected:** The page looks intentionally loud and comic while its essential text remains readable; all sections fit the viewport and the main clue works at all tested widths.

### Task 3: Document local preview and GitHub Pages publishing

**Files:**
- Modify: `README.md`

**Interfaces:**
- Documents how to preview the root-level static page and publish it from the repository's `main` branch.

- [ ] **Step 1: Replace the starter README text with concise project instructions**

Document the project purpose, the local preview command `python3 -m http.server 8000 --bind 127.0.0.1`, and the local URL `http://127.0.0.1:8000/`. Add GitHub Pages setup steps: open repository **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save. Explain that the published address follows `https://<owner>.github.io/test_pages/` and that GitHub may take a short time to publish after the first save.

- [ ] **Step 2: Verify the documented local preview and repository cleanliness**

Run the documented local server command from the repository root and confirm the page is served at the documented URL. Run:

```bash
git diff --check
```

Review the changed files and confirm the README describes the actual root-level page and `main` branch deployment configuration.

**Expected:** README instructions match the repository structure, local preview works, and `git diff --check` reports no whitespace errors.

- [ ] **Step 3: Confirm the GitHub Pages deployment after enabling it**

After saving the Pages settings, open the published URL shown by GitHub. Confirm the home page loads over HTTPS, category anchors work, the primary clue reaches the contact placeholder, and the mobile layout remains usable. If repository settings are not available to the implementer, give the user the exact Settings steps above and ask them to share the published URL for this final check.

**Expected:** The page is reachable at the GitHub Pages URL and behaves like the local version.
