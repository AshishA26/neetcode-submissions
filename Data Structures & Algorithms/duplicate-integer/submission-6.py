class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a hashmap or hashset: O(n). Checks if value already is in hashmap to see if duplicate
        uniqueVals = set()
        for n in nums:
            if n in uniqueVals:
                return True
            uniqueVals.add(n)
        return False

        # Other solutions include:
        # - Brute force
        # - Sorting the list before interating through. 
        #   Note: time complexity of sorting in general is O(nlogn)