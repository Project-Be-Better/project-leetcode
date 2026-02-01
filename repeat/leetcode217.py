from typing import List


class Solution217:

    def hasDuplicate(self, nums: List[int]) -> bool:
        # This is a set problem
        # Making into set decreases the number of elements if has duplicate
        # if the length of the lists are not the same, then, has duplicate

        # if not nums:
        # return False
        # len(0) != len(0) -> False

        # Long winded
        """
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True

        return False
        """

        nums_set = set(nums)
        return len(nums_set) != len(nums)
