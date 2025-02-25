class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        possibleMax = []
        maxCandy = max(candies)
    
        for kid in candies:
            possibleMax.append(((kid + extraCandies) >= maxCandy))

        return possibleMax

        '''
            BF:
            1. Declare another list, possibleMostCandy = []
            2. maxCandy = 0
            3. For loop: Iterate Candies
                for i in candies
                    if candies[i] > maxCandy
                    maxCandy = candies[i]

            4. For loop: Iterate candies and store if adding extraCandy makes curr > max
            5.     For each index, i
                        possibleMostCandy[i] = (candies[i] + extraCandies) > maxCandies

        '''  

 