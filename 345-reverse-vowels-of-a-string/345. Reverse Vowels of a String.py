class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        stringList = list(s)
        # convert input string to list to modify it easily
        # we'll need to convert back to string before returning

        left, right = 0, len(stringList)-1
        #pointers init to left and right of string array

        while left < right:
            #increment both ptrs until both pointing to vowels
            if stringList[left] not in vowels:
                left += 1
            elif stringList[right] not in vowels:
                right -= 1
            else:
                stringList[left], stringList[right] = stringList[right], stringList[left]
                # swapping reverseVowels
                left += 1
                right -= 1
        return ''.join(stringList)
