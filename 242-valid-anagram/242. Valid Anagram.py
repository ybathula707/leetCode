class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        charHash1, charHash2 = {}, {}

        '''
         Hash map will be key:value pairs where
          key is a character: val is counter 
         
         Each string will have its own hashed characters,
         which on comparison, we can return False if there 
         is not a match. 
         -> Means that the strings did not have identical characters
        O(n + m) space and O(n) time
        '''
        for i in range(len(s)):
            charHash1[s[i]] = 1 + charHash1.get(s[i], 0)
            charHash2[t[i]] = 1 + charHash2.get(t[i], 0)
        
        for charKey in charHash1:
            if charHash1[charKey] != charHash2.get(charKey, 0):
                return False
        
        return True