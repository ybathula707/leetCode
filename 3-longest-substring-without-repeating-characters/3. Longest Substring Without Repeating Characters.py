class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init our hashSet which will act as asa dictionary to track {value: freq} within the 
        # active dynamic sliding window
        uniqueWindow = {}
        start_window = 0  #  start pointer for the sliding window
        max_subarray = 0

        for end in range(len(s)):
            # adding current item to freq counter hashSet
            uniqueWindow[s[end]] = uniqueWindow.get(s[end], 0) + 1  #  incrementing frequency

            # shrink window until while it's an invalid Window
            while uniqueWindow[s[end]] > 1:
                #removing first element from hashSet, so decrement the freq in the set
                uniqueWindow[s[start_window]] -= 1
                start_window += 1 # move the window up one element, from left
            
            max_subarray = max(max_subarray, end - start_window + 1)
        
        return max_subarray
