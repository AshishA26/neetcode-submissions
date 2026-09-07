class Solution:

    # ********** SOLUTION 1 **************

    # def encode(self, strs: List[str]) -> str:
    #     # Add in a symbol to represent seperation, and then count
    #     # so that we know how far to check for the word
    #     retstr = ""
    #     for s in strs:
    #         count = len(s)
    #         retstr += f"#{count}#{s}"
    #     return retstr

    # def decode(self, s: str) -> List[str]:
    #     # loop through string characters
    #     strings = []
    #     i = 0
    #     while (i < len(s)):
    #         # Wait till we reach the # symbol
    #         if s[i] == "#":
    #             # Put in try except statement in case number conversion fails
    #             try:
    #                 # Get the full number
    #                 j = i+1
    #                 while s[j] != "#":
    #                     j += 1
    #                 count_str = s[i+1 : j]
    #                 # Try to cast to int
    #                 count = int(count_str)
    #                 wordidx = j+1
    #                 # Get the string
    #                 new_string = s[wordidx : wordidx+count]
    #                 strings.append(new_string)
    #                 i = wordidx+count
                
    #             # Count conversion failed, thus wasn't what we were looking for
    #             except:
    #                 i += 1
    #                 continue
            
    #         # Not a # symbol, continue
    #         else:
    #             i += 1

    #     return strings


    # *************** SOLUTION 2 **********************
    # O(n) for both functions - n is total number of characters given in list of words
    # Dont need #4#word for example. Only need 4#word.
    # Why? - Because we are starting off which the 4# gaurunteed
    #        we are making the encoded string!
    # This also prevents us from needing a try statement, because
    # we know the first few things before # are ints!

    # The # acts as the delimter to tell where count ends and word starts

    def encode(self, strs: List[str]) -> str:
        # Each word has a int and then `#` infront
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res