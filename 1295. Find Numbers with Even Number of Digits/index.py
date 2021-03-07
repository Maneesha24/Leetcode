class Solution:
    def findNumbers(self, nums):
        count = 0
        arr_len = len(nums)
        i = 0
        while(i < arr_len):
            if len(str(nums[i]))%2 == 0:
                count += 1
            i += 1
        
        return count

sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]))