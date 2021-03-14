class Solution:
    def createTargetArray(self, nums, index):
        i = 0
        result_arr = []
        while(i < len(nums)):
            result_arr = result_arr[:index[i]] + [nums[i]] + result_arr[index[i]:]
            i += 1
        return result_arr
                
sol = Solution()
print(sol.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))