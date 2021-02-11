class Solution:
    def runningSum(self, nums):
        i = 0
        # Iterate over the nums list
        while(i < len(nums)):
            # If the index is not 0, we add i - 1 to i, else stays the same
            if i != 0:
                nums[i] = nums[i] + nums[i - 1]
            i +=1
        return nums


sol = Solution()
print(sol.runningSum([1,2,3,4]))
