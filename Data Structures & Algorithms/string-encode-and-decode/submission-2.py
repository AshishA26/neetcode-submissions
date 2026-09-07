class Solution:

    def encode(self, strs: List[str]) -> str:
        # Add in a symbol to represent seperation, and then count
        # so that we know how far to check for the word
        retstr = ""
        for s in strs:
            count = len(s)
            retstr += f"#{count}#{s}"
        return retstr

    def decode(self, s: str) -> List[str]:
        # loop through string characters
        strings = []
        i = 0
        while (i < len(s)):
            # When we reach the # symbol, we attempt to get the number after it (by going until next # and then
            # trying to convert to int)
            if s[i] == "#":
                try:
                    # Get the full number
                    j = i+1
                    while s[j] != "#":
                        j += 1
                    count_str = s[i+1 : j]
                    # Try to cast to int
                    count = int(count_str)
                    wordidx = j+1
                    new_string = s[wordidx : wordidx+count]
                    strings.append(new_string)
                    i = wordidx+count
                except:
                    i += 1
                    continue
            else:
                i += 1
        return strings