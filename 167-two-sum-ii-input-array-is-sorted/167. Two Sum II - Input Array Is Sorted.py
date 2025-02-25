class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        less, greater = 0, len(numbers)-1
        # traverse array by index
        for i in range(len(numbers)):
            if numbers[less] + numbers[greater] == target:
                return [less+1, greater+1]
            elif numbers[less] + numbers[greater] > target:
                greater -= 1
            else :
                less +=1

        return []



