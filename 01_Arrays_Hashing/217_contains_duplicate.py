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


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pass


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # Expected: True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # Expected: False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Expected: True
