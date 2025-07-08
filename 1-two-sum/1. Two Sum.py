class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Iterate nums using indexes
        In hash map, if complemet does not exist, insert into map
        Index hashMap as {value: index}
        IN this way, when we encounter map[value] == complement,
        we can simply return

        map[value], map[target]
        which will each hold the index
        '''
        #Base cases where array is empty or NULL (return [])
        if nums is None or len(nums) == 0:
            return []

        hashMap ={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [i, hashMap[complement]]
            hashMap[nums[i]] = i

        return [] # no teo pair found 
      
        