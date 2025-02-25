class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) -1
        i=0
        while i <= right:
            if (nums[i] == 0):
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i+=1
            elif (nums[i] == 2):
                nums[right], nums[i] = nums[i], nums[right]
                right -=1
            else:
                i += 1

        """
        Given: Array of vlaues representing colors, sort the array in-place
        w/o python sort function
                        i              
        [ 0, 0, 0 , 1 , 1, 2, 2, 2, 2]
                -       = 
        Pseudo:
        i == 0
        while i < twoPtr
            if i is 0:
                swap i w/ zeroPtr
                zeroPtr +=1
                i += 1
            elif i is 2:
                swap i w/ twoPtr
                twoPtr += 1
            else:            
            i += 1
     
        """
        