from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hashmap to store the number of times a number occurs
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        
        # # Keep track of the k highest numbers
        # freqElems = []
        # for key in freqMap.keys():
        #     if freqElems
        #     freqElems.Add

        sorted_items = sorted(freqMap.items(), key = lambda item: item[1], reverse = True) # Returns a sorted list of tuples
        
        ret_list = []
        for i in range(k):
            ret_list.append(sorted_items[i][0])
        
        return ret_list