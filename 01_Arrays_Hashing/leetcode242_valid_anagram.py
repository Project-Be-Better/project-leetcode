"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Plausible Solution
        # Define a-z dict
        # Loop and count the letters
        # If the two words' counts match it is a pass?

        # Strings are not same length
        if len(s) != len(t):
            return False

        counter_map = {}

        for i in s:
            counter_map[i] = counter_map.get(i, 0) + 1

        for i in t:
            counter_map[i] = counter_map.get(i, 0) - 1

        if set(counter_map.values()) == {0}:
            return True

        return False
