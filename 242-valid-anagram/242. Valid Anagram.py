class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #Space O(n)
        hashS, hashT = {}, {}

        # Time O(n + m)
        for char in range(len(s)):
            hashS[s[char]] = 1 + hashS.get(s[char], 0)
            hashT[t[char]] = 1 + hashT.get(t[char], 0)

        # Time O(n)
        for c in hashS:
            if hashS[c] != hashT.get(c, 0):
                return False

        return True

        """
                Idea:
                    1. Sort both and compare equality
                    2. Put both into a seperate dictionary and compare
                    equality of those dictionary
                    3. occurence counter using One hashmap of size 26 letters
                        - return Flase if ever key: value maps to <0
            """
