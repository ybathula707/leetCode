class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCounterHash = collections.defaultdict(list)

        for s in strs:
            charCounter = [0] * 26
            for char in s:
                charCounter[ord(char) - ord("a")] += 1
            
            charCounterHash[tuple(charCounter)].append(s)

        return list(charCounterHash.values())

        """
            Idea:
                - We want to reduce lookup time for grouped anagrams to O(1),
                which can be done with hashMap.
                - For each string, make a character count hash
                - insert this into the hasmap where key: val pairs are like
                    [[character count hash] : [str1,str4, ...]]

                This way, we can jsut print the values of the hashmap for
                a grouped list of anagram strings

            * Note we cannot use list as a key, so convert the character count hash per string
            into a tuple before inseritign
        """
