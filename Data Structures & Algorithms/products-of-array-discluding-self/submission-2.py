class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # *********** SOLUTION 1 *******************
        # O(n^2) - nested for loops
        # Time taken is too long for a very large list
        # n = len(nums)
        # res = [0] * n
        # for i in range(n):
        #     ans = 1;
        #     for j in range(n):
        #         if j != i:
        #             ans *= nums[j]
        #     res[i] = ans
        # return res

        # ************** SOLUTION 2 *****************
        # Division operator - multiply all nums, then divide by nums[i]

        # ************** SOLUTION 3 ********************
        # O(n)
        # Get the product of all values before nums[i] and product of all values after nums[i]
        # Then multiply both together. We can use the idea of prefix and postfix arrays
        # where the elements hold the product of elements in nums before i. Though,
        # we can also just do it directly in the output array, by first going forwards and
        # storing the prefix product for i, then similarly go backwards and multply the output array.
        res = [1] * len(nums)

        # Go forwards. So if nums=[1,2,3,4], our res is becomes [1,1,2,6]
        # because we put in the prefix, then update it for the next loop (multiply by the nums element)
        prefix = 1 # Default value
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Go backwards. We update array (need to multiply, not just put into array like the previous for loop)
        # Then we update postfix
        # So our res now becomes [24, 12, 8, 6]
        postfix = 1 # Default value
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res