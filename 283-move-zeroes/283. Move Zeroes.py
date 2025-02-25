class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        zero_ptr, non_zero_ptr = len(nums), 0
        i = 0
        
        while non_zero_ptr < zero_ptr:
            if nums[i] != 0:
                nums[non_zero_ptr] = nums[i]
                non_zero_ptr +=1
            else:
                zero_ptr -= 1
            i += 1
        
        if zero_ptr == len(nums):
            return;
        
        for i in range(zero_ptr, len(nums)  , +1):
            nums[i] = 0
            
        
        
        """
        Given an array on integers, move the zeros in-place to the end of the arry
        EX: Input: nums = [0,1,0,3,12]
                  Output = [1,3,12,0,0]
        
        Idea: Two ptrs approach
        Ptr one is holding next-non-zero location, ptr two is append zero location 
        while next-non-zero < zero ptr:
            if arr[i] > 0:
                arr[next-non-zero] = arr[i]
                next-non-zero ++
            else:
                zero_ptr +=1
        
        then from zeor ptr-> len array, set arr[i] =0
        
        """
        