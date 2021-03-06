class Solution:
    def maxProduct (self, nums):
        max_prod = 0
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                if (nums[i] - 1) * (nums[j] - 1) > max_prod:
                    max_prod = (nums[i] - 1) * (nums[j] - 1)
                j += 1
            i += 1 

        return max_prod

sol = Solution()
print(sol.maxProduct([3,4,5,2]))