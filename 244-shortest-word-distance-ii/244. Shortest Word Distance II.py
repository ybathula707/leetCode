class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsIndeces = {}

        #populate the index arrays per word in hash table
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.wordsIndeces:
                self.wordsIndeces[wordsDict[i]] = []
            self.wordsIndeces[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        #edge cases for input validation -> ret None
        if not word1 or not word2:
            return None
        if word1 not in self.wordsIndeces or word2 not in self.wordsIndeces:
            return None

        word1Array = self.wordsIndeces[word1]
        word2Array = self.wordsIndeces[word2]

        i, j,min_distance = 0,0,float("inf")

        while i < len(word1Array) and j< len(word2Array):
            min_distance = min(min_distance, abs(word1Array[i]-word2Array[j]))

            #iterate the pointer that's smaller in index value 

            if word1Array[i] < word2Array[j]:
                i +=1
            else:
                j += 1
            
        return min_distance





# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)