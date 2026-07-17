class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hashmap to count frequency of each number
        freq_map = defaultdict(int) # number : count
        for n in nums:
            freq_map[n] += 1
        
        # Sort by value descending, this gives a list of tuples
        freq_list = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

        # Get k highest elements
        k_freq_elems = []
        for i in range(k):
            k_freq_elems.append(freq_list[i][0])

        return k_freq_elems