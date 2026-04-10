class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        numsSet.update(nums)

        return len(numsSet) < len(nums)
             
