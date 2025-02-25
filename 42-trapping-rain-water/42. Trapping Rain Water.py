class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        leftMax, rightMax = height[left], height[right]
        rainwater = 0

        while left + 1 < right:
             # while there is space b/w to hold water, NOT till they overlap
            if rightMax > leftMax:
                left += 1 # traverse smaller side
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    rainwater += leftMax - height[left]
            else:
                right -=1 # traversing smaller side
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    rainwater += rightMax - height[right]

        return rainwater
                
