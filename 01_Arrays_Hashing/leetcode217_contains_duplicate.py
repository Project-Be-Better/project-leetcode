"""
217. Contains Duplicate [Easy]
https://leetcode.com/problems/contains-duplicate/

Pattern: Arrays & Hashing

Question:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
"""

from typing import List
import unittest


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        converted_set = set(nums)
        return len(converted_set) != len(nums)

    def hasDuplicate_manual(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Category 1: Positive Cases
    def test_has_duplicates(self):
        self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 1]))
        self.assertTrue(self.sol.containsDuplicate([1, 1, 1, 3, 3, 4]))

    # Category 2: Negative Cases
    def test_no_duplicates(self):
        self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4]))
        self.assertFalse(self.sol.containsDuplicate([10, 20, 30, 40, 50]))

    # Category 3: Boundary Conditions
    def test_empty_array(self):
        self.assertFalse(self.sol.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.sol.containsDuplicate([1]))

    # Category 4: Large Constraints (Performance)
    def test_large_input(self):
        large_input = list(range(10000))
        self.assertFalse(self.sol.containsDuplicate(large_input))
        large_input.append(0)  # Introduce duplicate at the end
        self.assertTrue(self.sol.containsDuplicate(large_input))


if __name__ == "__main__":
    unittest.main()
