class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = {}

        for num in nums:
            if num in unique_nums:
                return True

            unique_nums[num] = 1

        return False 
        