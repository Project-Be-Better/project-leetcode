from typing import List


class Solution217:

    def hasDuplicate(self, nums: List[int]) -> bool:
        # This is a set problem
        # Making into set decreases the number of elements if has duplicate
        # if the length of the lists are not the same, then, has duplicate
        if not nums:
            return False

        if len(nums) == 1:
            return False

        return False
