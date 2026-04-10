class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums is None:
            return False

        if len(nums) == 0 or len(nums) == 1 :
            return False

        unique_nums = {}
    
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums[num] = num
        
        return False
