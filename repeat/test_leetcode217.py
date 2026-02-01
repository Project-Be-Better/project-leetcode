import unittest
from leetcode217 import Solution217


class TestSolution217(unittest.TestCase):

    def setUp(self):
        self.solution = Solution217()

    def testHasEmptyArray(self):
        self.assertFalse(self.solution.hasDuplicate([]))

    def testSingleInput(self):
        self.assertFalse(self.solution.hasDuplicate([1]))

    def testHasDuplicates(self):
        self.assertTrue(self.solution.hasDuplicate([1, 2, 3, 3]))

    def testHasNoDuplicates(self):
        self.assertFalse(self.solution.hasDuplicate([1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()
