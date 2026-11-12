import unittest
from stats import arithmetic_mean


class StatsTests(unittest.TestCase):
    def test_arithmetic_mean(self):
        self.assertEqual(arithmetic_mean([2, 4]), 3)


if __name__ == "__main__":
    unittest.main()
