class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        elif len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str1, str2[len(str1):])


    
    '''
    Solved using recusion 
    Base: 
        1. str1+str2 == str2+str1 ? 
            YES => continue
            NO => return ""
        2. len(str1) == len(str2) ? GCD found!
            return str1 

    Recursive:
        if(len(str1) > len(str2)):
             return gcdOfStrings(str1[len(str2):], str2)
        if(len(str2) > str1):
             return gcdOfStrings(str1, str2[len(str1): ])

               


    EX: ABABAB & ABAB
    is ABABAB + ABAB == ABAB + ABABAB ? YES!  => GDC exists
    is len(ABABAB) == len(ABAB) ? NO ==> Recurse on longer w/len of shorter
     - gcdOfStrings(str1[len(str2):], ABAB)
        -> AB & ABAB
        -> str1 + st2 == str2 + str1 ? YES  => GDC exists
        -> len(str1) == len(str2) ? NO ==> resuuse longer w/index of shorter
            ->  gcdOfStrings(AB, str2(len[str1:]) )
            -> AB & AB 
            -> is tr1 + st2 == str2 + str1 ? YES => GDC exists
            -> is len(str1) == len(str2) ? YES => GCD found!


    '''