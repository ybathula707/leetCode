class Solution:
    def maxArea(self, heights: List[int]) -> int:
                # var to keep track of largest volume found so far
        max_vol = 0
        # two ptrs Right Hand Side (RHS) and Left Hand Side (LHS)
        LHS,RHS = 0, len(heights) - 1
        while(LHS < RHS):
            max_vol = max(max_vol, (min(heights[LHS], heights[RHS])* (RHS - LHS)))
            if (heights[RHS] < heights[LHS]):
                RHS -=1
            else:
                LHS +=1          
  

        return max_vol
