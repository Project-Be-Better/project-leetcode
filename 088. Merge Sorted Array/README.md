# Problem

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

## Constraints:

- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -109 <= nums1[i], nums2[j] <= 109

# Solution

1. State the problem clearly. Identify the input & output formats.

- First array will have m elements to be selected for merge, sorted
- Second array will have n elements to be selected for merge, sorted
- Final length of the array should be m+n and should be sorted

2. Come up with some example inputs & outputs. Try to cover all edge cases.
   num1 = [1,2,3,0,0,0], m = 3
   num2 = [2,5,6], n = 3
   final =[1,2,2,3,5,6]

   num1 = [1], m = 1
   num2 = [], n = 0
   final =[1]

   num1 = [0], m = 0
   num2 = [1], n = 1
   final =[1]

3. Come up with a correct solution for the problem. State it in plain English.

- We have two pointers. p1 and p2 for each array and f which the third pointer, values are [m-1], [n-1], [m+n-1]
- We will compare and decrement the pointer values and update the f with the larger value
- We will exit once either the p1 and p2 are 0
- Only p2 will hav

4. Implement the solution and test it using example inputs. Fix bugs, if any.

5. Analyze the algorithm's complexity and identify inefficiencies, if any.

Time Complexity = O(m+n)
Space Compexity = O(1)

6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

- Two Pointer Technique
