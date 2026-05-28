from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a hashmap with the unique anagrams. Unique meaning that we sort the strings first,
        # then check if a string exists in the hashmap. The hashmap has a key of the sorted string,
        # with a value of a list of anagrams.
        # Or can use Counter(), or other functions
        anagrams = defaultdict(list) # string : list of strings
        
        for s in strs:
            sorted_s = "".join(sorted(s)) # sorted is a list a characters, need to join to make a string
            anagrams[sorted_s].append(s)

        return list(anagrams.values()) # Need to cast values to a list
