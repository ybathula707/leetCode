class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       
        merged = []
        minLen = min(len(word1), len(word2))

        for i in range(minLen):
            merged.append(word1[i])
            merged.append(word2[i])
        
        res = ''.join(merged) + word1[minLen:] + word2[minLen:]

        return res