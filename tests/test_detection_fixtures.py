"""Fixture-driven detection tests: only actual config is evidence."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("badges", Path(__file__).resolve().parents[1] / "scripts" / "badges.py")
badges = importlib.util.module_from_spec(spec)
spec.loader.exec_module(badges)

class DetectionFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "README.md").write_text("# Fixture\n\nPython Django Vue Postgres is a prose example.\n")

    def write(self, filename, value):
        path = self.root / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value)

    def test_prose_does_not_prove_technology(self):
        self.assertEqual(badges.detected(self.root), [])

    def test_package_dependency_frameworks(self):
        self.write("package.json", '{"dependencies":{"vue":"^3.0.0","next":"^15.0.0"},"devDependencies":{"typescript":"~5.0.0"}}')
        self.assertEqual(badges.detected(self.root), ["Next.js", "TypeScript", "Vue"])

    def test_python_requirement_in_pyproject(self):
        self.write("pyproject.toml", '[project]\ndependencies = [\n  "Django>=5",\n  "fastapi==0.1",\n]\n')
        self.assertEqual(badges.detected(self.root), ["Django", "FastAPI", "Python"])

    def test_compose_database_detection(self):
        self.write("compose.yaml", "services:\n  db:\n    image: postgres:16\n  cache:\n    image: redis:7\n")
        self.assertEqual(badges.detected(self.root), ["Docker", "Docker Compose", "PostgreSQL"])

    def test_github_pages_only_with_workflow(self):
        self.write(".github/workflows/pages.yml", "name: Deploy\njobs:\n  deploy:\n    steps:\n      - uses: actions/deploy-pages@v4\n")
        self.assertEqual(badges.detected(self.root), ["GitHub Pages"])

    def test_placeholder_license_is_not_validated(self):
        self.write("LICENSE", "TODO: choose a license")
        self.assertNotIn("[![License]", badges.generate(self.root))

    def test_readme_safe_repeated_updates(self):
        self.write("package.json", '{"dependencies":{"svelte":"^5"}}')
        self.assertTrue(badges.apply(self.root, write=True)[0])
        before = (self.root / "README.md").read_text()
        self.assertIn("prose example", before)
        self.assertFalse(badges.apply(self.root, write=True)[0])
        self.assertEqual((self.root / "README.md").read_text(), before)

if __name__ == "__main__":
    unittest.main()
