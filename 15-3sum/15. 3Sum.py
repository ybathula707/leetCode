class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retArray = []

        for i in range(len(nums) - 2):
            # keep incrementing first tuple item intil not duplicate
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                # updating pointers based on current sum w.r to 0

                # use if/ elif and else block for 3 seperate cases.
                # if we did if, if and else, then the logic is WRONG
                # why? cuz else is part of the second if statement, they are not all grouped togehter
                # This means tuple is appended only if currSum <0, which is not the behavior we are going for
                # We want 3 seperate checks, where in each loop only one executes.
                # for that, if/elif and else is the correct choice.

                if currentSum > 0:  # decrement the larger pointer
                    right -= 1
                elif currentSum < 0:   # increment the smaller pointer 
                    left += 1
                else:
                    # append the items into array since they equal 0
                    retArray.append([nums[i], nums[left], nums[right]])
                    # incrment left and right while pointers dont overlap 
                    # and while next left or right is dup to current pointer
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    # increment left and right arbitrarily, or one final time after 
                    # avoiding dup logic
                    left += 1
                    right -= 1

        return retArray
