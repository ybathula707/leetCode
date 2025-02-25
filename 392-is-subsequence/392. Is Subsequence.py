class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        search_ctr = 0
        for char in t:
            if char == s[search_ctr]:
                search_ctr += 1
            if search_ctr == len(s) :
                return True

        return False 
        