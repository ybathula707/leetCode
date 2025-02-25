"""
          -
A m a n , a p l a n , a c a n a l : P a n a m a 
                                      -
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # declaring 2 index ptrs

        while l < r:  # (while pointers don't overlap)
            """
            we want to break loop once ptrs overlap
            becuse this means palindrome is not possble,
            Ptrs should be symmetric
            """
            while s[l].isalnum() is False and l < r:
                l += 1
            while s[r].isalnum() is False and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
