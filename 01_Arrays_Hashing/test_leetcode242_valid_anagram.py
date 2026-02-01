import unittest
from leetcode242_valid_anagram import Solution


class TestLeetcode242(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testTestisSingleChar(self):
        self.assertTrue(self.sol.isAnagram("i", "i"))

    def testValidAnagram(self):
        self.assertTrue(self.sol.isAnagram("anagram", "nagaram"))

    def testNOTValidAnagram(self):
        self.assertFalse(self.sol.isAnagram("rat", "car"))

    def testDifferentStringLengths(self):
        self.assertFalse(self.sol.isAnagram("anagram", "nagarami"))


if __name__ == "__main__":
    unittest.main()
