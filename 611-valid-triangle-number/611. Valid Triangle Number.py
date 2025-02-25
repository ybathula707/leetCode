class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triangle_counter = 0

        for i in range(len(nums) - 1, 1 ,-1):
            right, left = i - 1, 0
            while(left< right):
                if (nums[left] + nums[right] > nums[i]):
                    triangle_counter += (right - left)
                    right -= 1           
                else:
                    left += 1
                    
        return triangle_counter                         

'''
Given: 
unsorted integer array nums representing side lengths

Expectation: 
return int tringle_count, the number of triplets from nums
that can form a valid traingle

Assumptions:
1. input array is unsorted
2. order of indexes in the tuple is not enforced

Key observation:
- to form a valid triangle, the sum of any two sides should be larger that the third side

Idea:
- sort the arry, to use the 2 ptr approach
- why: 
When sorted we can count valid tuples,based on the sum of the two pointers w.r. to a current 'target' side lenght, which we will choose as the rightmost item in array

[ 2, 2, 3, 4]. ==> L + R >? i  
  L.    R. i

==> increment L & R respectiveley and triangle_ctr
==> if FOUND, all lens b/w L -- R are possible triangle tuples
    (cuz sorted)  --> counter += R-L
==> if NOT, incrment smaller ptr, L (only happens if sum < i)    

PC

nums.sort()
traingle_counter =0
for i = end .. i -- .. i == 1:
    left = 0
    right = i - 1
    while ( l < right):
        if nums[left] + nums[right] > nums[i]:
            traingle_counter += right - left
            R -= 1
        else:
            L += 1 # sum < i, we need a bigger tuple

     return triangle_counter       

'''