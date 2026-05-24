class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use a hashmap to hold the number of times a letter occurs
        # and see if that matches the hashmap for the 2nd string

        # Edge case
        if (len(s) != len(t)): 
            return False

        sMap = {}
        tMap = {}

        for c in s:
            if c in sMap.keys():
                sMap[c] += 1
            else:
                sMap[c] = 0
        
        for c in t:
            if c in tMap.keys():
                tMap[c] += 1
            else:
                tMap[c] = 0
        
        for key in sMap.keys():
            if key in tMap.keys() and sMap[key] == tMap[key]:
                continue # Matches
            if key not in tMap.keys() or sMap[key] != tMap[key]:
                return False

        return True