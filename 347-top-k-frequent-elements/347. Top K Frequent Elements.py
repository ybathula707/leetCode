class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freqArray =[[] for i in range(len(nums) + 1)]
        res_array = []

        for i in range(len(nums)):
            countMap[nums[i]] = 1 + countMap.get(nums[i], 0)
            # key:val hashmap where num:counter is used to
            # store the frequency of each number
        for num, counter in countMap.items():
            freqArray[counter].append(num)
            # 2D freq array where each idx correspnds to a freq/count
            # and the list of nums stored at [counter] are values
            # from nums array occur those 'counter' number of times
        
        # Now we have 2D frequency array matrix arranged like 
        '''
            least freq --> most freq.
            So parsing it from the end and returning elements from
            the nested array, we can return the k most freq elements

        '''
        #                   start idx       end idx    incr
        for i in range( len(freqArray) -1 , 0        ,   -1):
            for num in freqArray[i]:
                res_array.append(num)
                if len(res_array) == k:
                    return res_array        