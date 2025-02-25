class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_lower = s.lower()
        t_lower = t.lower()

        charHash = {}

        for i in range(len(s_lower)):
            charHash[s_lower[i]] = 1 + charHash.get(s_lower[i], 0)
        for i in range(len(t_lower)):
            charHash[t_lower[i]] = charHash.get(t_lower[i], 0) - 1

        for charKey in charHash:
            if charHash[charKey] != 0:
                return False

        return True

        """
        In this version, converted string to lowercase and then used a simgle
        array, initialzed to all 0's to track occurences of each char in either str.
        If we run into it in s1, +=1
        If we run into it in s2 -=1
        At the end, if the char Hash array has any value != 0, something didn't
        match between strings. (Since if they had equal occurences of each char,
        after all inc and decr, val should be 0)
        """
