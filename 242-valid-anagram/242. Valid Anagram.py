class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        s_lower = s.lower()
        t_lower = t.lower()

        charHash = [0] * 26

        for i in range(len(s_lower)):
            charHash[ord(s_lower[i]) - ord('a')] += 1
        for i in range(len(t_lower)):
            charHash[ord(t_lower[i]) - ord('a')] -= 1
        
        for charKey in charHash:
            if charKey != 0:
                return False
        
        return True