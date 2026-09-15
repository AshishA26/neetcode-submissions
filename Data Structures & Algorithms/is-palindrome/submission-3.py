class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ************* SOLUTION 1 **************
        # Remove spaces and special characters, lowercase all, check if forward = reverse
        # O(n)

        s = s.lower()
        s = s.replace(" ", "") # Remove spaces. Don't use .strip() as it only does outer edges

        # Only keep alphanumeric chars
        s = "".join([ch for ch in s if ch.isalnum()])

        # Compare string to reversed string
        rev = s[::-1]
        if rev == s:
            return True
        return False

        # **************** SOLUTION 2 *******************
        # Same but simplified slightly
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

        # **************** SOLUTION 3 *******************
        # Can use 2 pointers. 1 starts at the left end, moves right. 2 starts at
        # the right end, move left. Check they always are equal as they move to see
        # if palindrome.
        # If there are spaces, then move the pointer further more. While not alnum, do L++ for ex.
        # If can't use built in functions, we can use ascii values (which are contiguous)
        # O(n) time, but O(1) memory bc no extra strings.
        # Loop until they have met or crossed each other.

    #     l = 0
    #     r = len(s) - 1

    #     while l < r:
    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1
    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l += 1
    #         r -= 1
    #     return True
    
    # def alphaNum(self, c):
    #     return (
    #         ord('A') <= ord(c) <= ord('Z') or 
    #         ord('a') <= ord(c) <= ord('z') or
    #         ord('0') <= ord(c) <= ord('9')
    #     )
