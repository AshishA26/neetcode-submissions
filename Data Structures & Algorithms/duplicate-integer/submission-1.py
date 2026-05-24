class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a hashmap
        uniqueVals = {}
        for n in nums:
            if n in uniqueVals.keys():
                return True
            uniqueVals[n] = 1
        return False