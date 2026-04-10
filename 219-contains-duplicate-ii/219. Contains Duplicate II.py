class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if nums is None:
            return False
        if len(nums) == 1:
            return False

        vals = {}

        for index, val in enumerate(nums):
            if val in vals:
                if abs(index - vals[val] ) <= k:
                    return True
            vals[val] = index
        
        return False

            