
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # iterate only once, assigning ptr1 to first found word
        # asignt ptr 2 in whichever iteration you could find it
        # this first time these pointers are both assigned, we calculate the
        # difference and can return this. 
        p1, p2 = -1, -1
        minDif = float("inf")

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            if wordsDict[i] == word2:
                p2 = i

            if p1 != -1 and p2 != -1:
                minDif = min(minDif, abs(p2-p1))

        return minDif