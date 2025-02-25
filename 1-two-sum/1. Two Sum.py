class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        
        return []

    """
    Given an array we need to return indices of two values
    that sum to a target
   
    NOTE: NOT sameas sort => sum pairs to return BOOL or the 
    actual value. We need to mainitin index of each val, to return
        -- this is a teo pointer, since we sort


    Strategy: 

    BF: for every elemnt i in the array, do the next
    values equal that? If so, return index as we check. 

    KEY: we do not need to know rest of the array
    in order to determine the COMPLEMENT of nums[i] that
    would give us the target.

    I.e if target is 10, and nums[3] is 4, we know that
    6 is the value we need for a solution
        => optimize how we search for 6 and index of 
        6 within this array





    """
