class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ************* SOLUTION 1 **************
        # Remove spaces and special characters, lowercase all, check if forward = reverse
        # O(n) most likely

        # s = s.lower()
        # s = s.replace(" ", "") # Remove spaces. Don't use .strip() as it only does outer edges

        # # Only keep alphanumeric chars
        # newS = "".join([ch for ch in s if ch.isalnum()])

        # # Compare string to reversed string
        # rev = newS[::-1]
        # if rev == newS:
        #     return True
        # return False

        # **************** SOLUTION 2 *******************
        # Same but simplified slightly
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]