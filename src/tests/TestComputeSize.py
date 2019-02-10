import unittest

from example import Conditional


class UnitTesting(unittest.TestCase):

    def test_categories_simple(self):
        large_double = 70.0
        medium_double = 50.0
        small_double = 10.0

        self.assertTrue(Conditional.computeSize(large_double) == "large", large_double)
        self.assertTrue(Conditional.computeSize(medium_double) == "medium", medium_double)
        self.assertTrue(Conditional.computeSize(small_double) == "small", small_double)

    def test_categories_boundaries(self):
        large_double = 60.0
        medium_double_upper_bound = 59.99
        medium_double_lower_bound = 30.0
        small_double = 29.99

        self.assertTrue(Conditional.computeSize(large_double) == "large", large_double)
        self.assertTrue(Conditional.computeSize(medium_double_upper_bound) == "medium", medium_double_upper_bound)
        self.assertTrue(Conditional.computeSize(medium_double_lower_bound) == "medium", medium_double_lower_bound)
        self.assertTrue(Conditional.computeSize(small_double) == "small", small_double)

    def test_categories_thorough(self):
        large_doubles = [60.0, 60.01, 70.0, 90.0, 1000.0]
        medium_doubles = [59.9, 30.0, 30.01, 40.0, 50.0]
        small_doubles = [29.99, 20.0, 10.0, 0.0, -100.0, -10000.0]

        large_doubles.append(10000.0)

        for large_double in large_doubles:
            self.assertTrue(Conditional.computeSize(large_double) == "large", large_double)
        for medium_double in medium_doubles:
            self.assertTrue(Conditional.computeSize(medium_double) == "medium", medium_double)
        for small_double in small_doubles:
            self.assertTrue(Conditional.computeSize(small_double) == "small", small_double)


if __name__ == '__main__':
    unittest.main()
