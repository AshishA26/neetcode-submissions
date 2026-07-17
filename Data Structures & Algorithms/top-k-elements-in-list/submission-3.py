class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # *************** SOLUTION 1 *****************        
        # # O(nlogn) because of sorting
        # # Use a hashmap to count frequency of each number
        # count = defaultdict(int) # number : count
        # for n in nums:
        #     count[n] += 1
        # # Sort by value descending, this gives a list of tuples
        # freq = sorted(count.items(), key=lambda item: item[1], reverse=True)
        # # Get k highest elements
        # k_freq_elems = []
        # for i in range(k):
        #     k_freq_elems.append(freq[i][0])
        # return k_freq_elems

        # *************** SOLUTION 2 ********************
        # k*logn (not nlogn) - MIN HEAP
        # Count frequency like above, then add each pair to a min heap
        # The key of min heap would be the # of occurances, then we can
        # pop from the min heap k times.
        # Note: Heapify function

        # *************** SOLUTION 3 *******************
        # O(n) - BUCKET SORT
        # Count frequency, then create another mapping like: 
        #   frequency count : list of #s with this frequency 
        # Important trick: The 2nd mapping array should be of size of input list n !!!!
        #   Why? Because the max # of times one of the #s could occur is n times.
        # Then you go from the end of the array, getting k most to least frequent elements
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] += 1
        for num, count in count.items():
            freq[count].append(num)
        
        res = [] # final list of k most freq nums
        for i in range(len(freq) - 1, 0, -1): # Going until 0, in descending order (hence the -1)
            for n in freq[i]: # For each item in the freq sublist
                res.append(n)

                # When output has k values, then we can return.
                # We are gaurunteed to have at least k elements.
                if len(res) == k: 
                    return res
