class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[swapIndex], nums[i] = nums[i], nums[swapIndex]
                swapIndex += 1
        return