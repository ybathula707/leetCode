class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        if len(nums) == 0:
            return []
        # Base cases of empty list or NULL list

        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [i, hashMap[complement]]
            hashMap[nums[i]] = i
        
        #empty list if no pair is found
        return []

        """
        Idea: 
            - have a hash map where key:val pairs are num:idx.
            - for each element, check if complement is in the map before
            inserting.
             Return the indexes if found
             else [] empty array
            is returned
        """
