from __future__ import annotations

import hashlib
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class StaticSearchSiteTests(unittest.TestCase):
    def test_readme_leads_with_the_search_entry(self):
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        hero = readme.split("\n---\n", 1)[0]
        pages_url = "https://guangjunzeng.github.io/Humanoid-WBC-Handbook/"
        self.assertIn("site/assets/search-preview.svg", hero)
        self.assertIn("打开中英文快速搜索", hero)
        self.assertIn("所有工程问题均可搜索", hero)
        self.assertIn("可信度、状态和证据边界在独立详情页查看", hero)
        self.assertEqual(hero.count(f"]({pages_url})"), 2)
        self.assertNotIn("](site/)", hero)

    def test_site_uses_only_repository_relative_assets(self):
        html = (PROJECT_ROOT / "site/index.html").read_text(encoding="utf-8")
        for asset in (
            "./assets/handbook.css",
            "./assets/kinematics.svg",
            "./assets/search.js",
            "./vendor/flexsearch.bundle.min.js",
        ):
            self.assertIn(asset, html)
        self.assertNotIn("https://", html)
        self.assertIn("Content-Security-Policy", html)
        for forbidden in ("<nav", "eyebrow", "theme-toggle"):
            self.assertNotIn(forbidden, html)
        self.assertIn('class="language-switcher"', html)
        self.assertIn('data-locale="zh"', html)
        self.assertIn('data-locale="en"', html)
        self.assertIn('aria-pressed="true"', html)

    def test_search_interaction_keeps_accessibility_and_ime_guards(self):
        html = (PROJECT_ROOT / "site/index.html").read_text(encoding="utf-8")
        script = (PROJECT_ROOT / "site/assets/search.js").read_text(encoding="utf-8")
        for marker in (
            'role="combobox"',
            'aria-activedescendant=""',
            'aria-live="polite"',
            'role="listbox"',
        ):
            self.assertIn(marker, html)
        for marker in (
            "compositionstart",
            "compositionend",
            "event.isComposing",
            'event.key === "ArrowDown"',
            'event.key === "ArrowUp"',
            'event.key === "Enter"',
            'event.key === "Escape"',
            "history.replaceState",
            "wbc-handbook-locale",
            "navigator.languages",
            'searchParams.get("lang")',
            'searchParams.set("lang", locale)',
            "payload.schema_version !== 2",
            "title_zh",
            "title_en",
            "FlexSearch.Document",
        ):
            self.assertIn(marker, script)
        self.assertNotIn(".innerHTML", script)

    def test_mobile_and_reduced_motion_rules_are_present(self):
        css = (PROJECT_ROOT / "site/assets/handbook.css").read_text(encoding="utf-8")
        svg = (PROJECT_ROOT / "site/assets/kinematics.svg").read_text(encoding="utf-8")
        self.assertIn("@media (max-width: 640px)", css)
        self.assertIn("prefers-reduced-motion: reduce", css)
        self.assertIn("prefers-reduced-motion: reduce", svg)
        self.assertIn("pointer-events: none", css)
        self.assertGreaterEqual(svg.count("<circle"), 12)
        self.assertLessEqual(svg.count("<circle"), 20)
        self.assertEqual(svg.count('class="skeleton-a"'), 1)
        self.assertNotIn('class="skeleton-b"', svg)

    def test_vendored_flexsearch_hash_matches_notice(self):
        bundle = PROJECT_ROOT / "site/vendor/flexsearch.bundle.min.js"
        digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
        notice = (PROJECT_ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
        self.assertEqual(
            digest,
            "38ae9b1265fd083ef21e054405c1eb0a612cf7dff9c6108c2a281c941e9174e3",
        )
        self.assertIn(digest, notice)
        self.assertTrue((PROJECT_ROOT / "site/vendor/FLEXSEARCH-LICENSE").is_file())

    def test_pages_workflow_checks_and_deploys_the_static_site(self):
        workflow = (PROJECT_ROOT / ".github/workflows/pages.yml").read_text(
            encoding="utf-8"
        )
        for marker in (
            "branches: [main]",
            "workflow_dispatch:",
            "wbc_handbook validate",
            "wbc_handbook render-problems",
            "--check",
            "wbc_handbook build-web-index",
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v4",
            "path: site",
            "actions/deploy-pages@v4",
            "pages: write",
            "id-token: write",
            "name: github-pages",
        ):
            self.assertIn(marker, workflow)


if __name__ == "__main__":
    unittest.main()
