class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        next_location =1
        for i in range(len(nums)):
            if i >0 and nums[i] != nums[i-1]: # if unique element found
                nums[next_location] = nums[i]
                next_location +=1
        
        return next_location
        