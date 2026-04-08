class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if not word1 or not word2:
            return None
        wordsIndex = {}
        # populate the words hash dict were key= word hash, val= idx array
        for i, word in enumerate(wordsDict):
            if word not in wordsIndex:
                wordsIndex[word] = []
            wordsIndex[word].append(i)
        
        wArray1, wArray2 = wordsIndex[word1], wordsIndex[word2]
        wPtr1, wPtr2 = 0, 0
        minDist = float("inf")

        # if same, jsut check for min difference between all contingious elements
        # since indexes are  inorder 
        if word1 == word2:
            # first comparison b.w i=1 and i =0
            for i in range(1, len(wArray1)):
                minDist = min(minDist, abs(wArray1[i - 1] - wArray2[i]))
            return minDist

        # normal case, two ptr approach. 
        # move pointer at smaller index value

        while wPtr1 < len(wArray1) and wPtr2 < len(wArray2):
           minDist = min(minDist, abs(wArray1[wPtr1] - wArray2[wPtr2]))
           
           if wArray1[wPtr1] < wArray2[wPtr2]:
                wPtr1 += 1
           else:
                wPtr2 += 1

        return minDist

