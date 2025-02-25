class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashDup = set()
        for i in nums:
            if i in hashDup:
                return True
            else:
                hashDup.add(i)
        
        return False

        