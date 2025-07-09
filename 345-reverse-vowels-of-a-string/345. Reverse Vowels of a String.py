class Solution:
    def reverseVowels(self, s: str) -> str:
         # Define a set of vowels for quick lookup
        vowels = "aeiouAEIOU"
    
        # Convert the string to a list to modify it easily
        s_list = list(s)
    
        # Initialize pointers for the start and end of the string
        left, right = 0, len(s) - 1
    
        # Loop until the two pointers meet or cross each other
        while left < right:
            # Move the left pointer to find a vowel on the left side
            if s_list[left] not in vowels:
                left += 1
            # Move the right pointer to find a vowel on the right side
            elif s_list[right] not in vowels:
                right -= 1
            # If both pointers have found vowels, swap them and move both pointers
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return ''.join(s_list)
