class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultArray = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            greater = len(nums) - 1
            less = i + 1

            while less < greater:

                sumZero = nums[i] + nums[less] + nums[greater]
                if sumZero > 0:
                    # decrement larger ptr, until its not a duplicate
                    greater -= 1
                elif sumZero < 0:
                    # increment smaller ptr, until its not a duplicate
                    less += 1
                else:
                    # found a triple summing to 0! Add to resArray
                    resultArray.append([nums[i], nums[less], nums[greater]])

                    while less < greater and nums[greater] == nums[greater - 1]:
                        greater -= 1
                    while less < greater and nums[less + 1] == nums[less]:
                        less += 1

                    greater -= 1
                    less += 1

        return resultArray

        """
            Given: nonsotred int array, return list of all
            triplets (no dublicate elements) which sum to
            0, were indeces are unique

            Idea:
            O(N) time using 2 ptr approach (really 3 ptrs)
            1) Sort the array
            i = array idx ptr
                     i -
            [-1, -1, 0,1, 2, 3]
                             =

            for i to end of nums:
                while i is not 0, and i is not dup:
                    i ++ 

                r = i +1
                l = len(nums)
                while ptr do not overlap:
                    check zero sum
                    sum is < 0:
                        increment larger ptr
                    else bigger 
                        increment smaller ptr
                    else:
                        append triple to array 
                   -> in while() Increment pointers to the last occurence of dup
                   -> Increment all pointers to next unique value
        """
