class Solution:
    def maxArea(self, height: List[int]) -> int:
        right_ptr, left_ptr = len(height) - 1, 0
        max_vol = 0

        if height is None or len(height) == 1:
            return max_vol

        while left_ptr < right_ptr:

            # calculate current volume
            curr_height = min(height[right_ptr], height[left_ptr])
            width = right_ptr - left_ptr
            curr_volume = curr_height * width

            # update maximum volume if we found a new max
            max_vol = max(curr_volume, max_vol)

            # increment smaller pointer
            if height[right_ptr] < height[left_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1

        return max_vol
