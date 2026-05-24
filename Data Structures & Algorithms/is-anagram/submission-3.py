class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # -------------------- SOLUTION 1 ---------------------
        # # Use a hashmap to hold the number of times a letter occurs
        # # and see if that matches the hashmap for the 2nd string
        # # Time complexity: O(s + t) or basically O(n)
        # # Edge case. Ensure same length
        # if (len(s) != len(t)): 
        #     return False
        # sMap = {} # char : count
        # tMap = {} # char : count
        # for c in s:
        #     if c in sMap.keys():
        #         sMap[c] += 1
        #     else:
        #         sMap[c] = 0
        # for c in t:
        #     if c in tMap.keys():
        #         tMap[c] += 1
        #     else:
        #         tMap[c] = 0
        # for key in sMap.keys():
        #     if key in tMap.keys() and sMap[key] == tMap[key]:
        #         continue # Matches
        #     if key not in tMap.keys() or sMap[key] != tMap[key]:
        #         return False
        # return True

        # -------------------- SOLUTION 2 ---------------------
        # # Time complexity: O(n)
        # if (len(s) != len(t)): 
        #     return False
        # sMap = {} # char : count
        # tMap = {} # char : count
        # # Rather than the 2 for loops above, can iterate at the same time
        # # because the lists are ensured to be the same length.
        # # Use .get to avoid needing if statements I did above.
        # for i in range(len(s)):
        #     sMap[s[i]] = 1 + sMap.get(s[i], 0)
        #     tMap[t[i]] = 1 + tMap.get(t[i], 0)
        # # Check that counts of each character matches
        # for c in sMap:
        #     if sMap[c] != tMap.get(c, 0): # Use .get incase character doesnt exist in tMap
        #         return False
        # return True

        # -------------------- SOLUTION 3 ---------------------
        # # Time complexity: O(n)
        # return Counter(s) == Counter(t)

        # -------------------- SOLUTION 4 ---------------------
        # Memory complexity: O(1), Time complexity: O(nlogn)
        # Just need to sort the strings! Then check if they are equal.
        # So rather than counting each character, just check that every char now matches up
        # and is in same place
        return sorted(s) == sorted(t)