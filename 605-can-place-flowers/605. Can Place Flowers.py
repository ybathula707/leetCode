class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plantingPossible = 0 
        planted = 0 
        if (len(flowerbed) % 2 == 0):
            plantingPossible = len(flowerbed)/2
        else:
            if flowerbed[0] == 1:
              plantingPossible =  ((len(flowerbed) + 1)/2)
            else:
                plantingPossible =  ((len(flowerbed) + 1)/2) -1 

        for i in flowerbed:
            planted += i

        return n <= plantingPossible - planted


    '''
    plantedPossible = 0
    If Odd length:
        - starts with 1, Total planted Possbile = (LEN + 1)/2 
        - starts with 0, Total planted possible is ((LEN + 1)/2) -1
    If EVEN:
        - planted possible is LEN /2  

    FOR  i in bed :
        planted += i  

    return n <= plantedPossible


    Recursion? 
    1. If index +1 & -1 are 0, we can plant
    2. If index is 0 or END and +1 or -1 are 0, we can plant

    BASE: 
    1. If index+1 and index -1 == 0
        return counter == n
    2. 
    '''    