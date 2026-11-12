import unittest
from stats import mean


class StatsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2, 4]), 3)


if __name__ == "__main__":
    unittest.main()
