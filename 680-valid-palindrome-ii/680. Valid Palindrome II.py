class Solution:
    def validPalindrome(self, s: str) -> bool:
        checked = False
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                # If we haven't already removed a character
                if not checked:
                    checked = True
                    # Try skipping the left character (s[l]) or the right character (s[r])
                    # Check if skipping one character can make the rest a palindrome
                    # Skip the left character: Check s[l+1:r+1]
                    if s[l+1] == s[r]:
                        l += 1
                    # Skip the right character: Check s[l:r-1]
                    elif s[r-1] == s[l]:
                        r -= 1
                    else:
                        return False
                else:
                    return False
        
        return True
