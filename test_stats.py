import unittest
from stats import mean


class StatsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2, 4]), 3)

    def test_mean_non_integer(self):
        self.assertEqual(mean([1, 2]), 1.5)


if __name__ == "__main__":
    unittest.main()
