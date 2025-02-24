class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        




        """
                Idea:
                    1. Sort both and compare equality
                    2. Put both into a seperate dictionary and compare
                    equality of those dictionary
                    3. occurence counter using One hashmap of size 26 letters
                        - return Flase if ever key: value maps to <0
            """
