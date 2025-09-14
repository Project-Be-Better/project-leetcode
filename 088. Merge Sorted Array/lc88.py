from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1, p2, f = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[f] = nums1[p1]
                p1 -= 1
            else:
                nums1[f] = nums2[p2]
                p2 -= 1

            f -= 1

        while p2 >= 0:
            nums1[f] = nums2[p2]
            p2 -= 1
            f -= 1


solution = Solution()

num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
solution.merge(num1, 3, num2, 3)
assert num1 == [1, 2, 2, 3, 5, 6]

# Test 1: nums1 empty, only nums2
nums1 = [0]
nums2 = [1]
solution.merge(nums1, 0, nums2, 1)
assert nums1 == [1]

# Test 2: nums2 empty, only nums1
nums1 = [1]
nums2 = []
solution.merge(nums1, 1, nums2, 0)
assert nums1 == [1]

# Test 3: nums1 and nums2 both have data
nums1 = [4, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
solution.merge(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 3, 4, 5, 6]


print("All tests passed for LC-088")
