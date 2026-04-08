
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        wordsIndex = {}

        if not word1 or not word2:
            return None

        #O(n) to populate but O(1) lookups
        for i, word in enumerate(wordsDict):
            if word not in wordsIndex:
                wordsIndex[word] = []
            wordsIndex[word].append(i)

        if word1 not in wordsIndex or word2 not in wordsIndex:
            return None

        # load the word index arrays
        word1IndexArray = wordsIndex[word1]
        word2IndexArray = wordsIndex[word2]

        # init ptrs and min aggregator
        word1Ptr, word2Ptr, minDist = 0, 0, float("inf")

        while word1Ptr < len(word1IndexArray) and word2Ptr < len(word2IndexArray):
            minDist = min(minDist, abs(word1IndexArray[word1Ptr] - word2IndexArray[word2Ptr]))

            # move the pointer that's the smaller index val
            if word1IndexArray[word1Ptr] < word2IndexArray[word2Ptr]:
                word1Ptr += 1
            else:
                word2Ptr += 1

        return minDist
