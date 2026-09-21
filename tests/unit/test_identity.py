import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from ollin_flylab.datasets import BANC_V888, FAFB_V783, SUPPORTED_DATASETS
from ollin_flylab.identity import PROJECT_ID, REPOSITORY_PROFILE


class IdentityTests(unittest.TestCase):
    def test_project_identity_is_frozen(self):
        self.assertEqual(PROJECT_ID, "ollin-fruit-fly-lab")
        self.assertEqual(REPOSITORY_PROFILE, "OLLIN_LITE")

    def test_initial_dataset_registry_is_exact(self):
        self.assertEqual(SUPPORTED_DATASETS, (FAFB_V783, BANC_V888))
        self.assertEqual(FAFB_V783.version, "v783")
        self.assertEqual(BANC_V888.version, "v888")

    def test_dataset_descriptors_are_distinct(self):
        self.assertNotEqual(FAFB_V783.key, BANC_V888.key)
        self.assertNotEqual(FAFB_V783.download_index_url, BANC_V888.download_index_url)


if __name__ == "__main__":
    unittest.main()
