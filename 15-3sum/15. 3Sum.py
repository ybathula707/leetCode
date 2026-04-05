class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        soltn_array =[]
        nums.sort()

        # range from i -> 2nd to last element
        for current in (range(len(nums) - 2)):
            if current > 0 and nums[current - 1] == nums[current]:
                continue
            left = current + 1
            right = len(nums) - 1

            #while left and right dont overlap, run sum checks
            while left < right:
                current_sum = nums[current] + nums[left] + nums[right]
                if current_sum > 0:
                    right -=1
                elif current_sum < 0:
                    left += 1
                else:
                    soltn_array.append([nums[current], nums[left], nums[right]])
                    while left < right and nums[right -1 ] == nums[right]:
                        right -= 1
                    while left < right and nums[left + 1 ] == nums [left]:
                        left += 1
                    left += 1
                    right -= 1 


        return soltn_array









    ''' 
        Idea:
        - sort arraty
        - 2 ptr approach will be left and right ptr where left is curr +1 
        - curr is index i

        Incr scenarios:


    '''