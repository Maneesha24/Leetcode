class Solution:
    def twoSum(self, nums, target: int):
        result_arr = []
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                if nums[i] + nums[j] == target:
                    result_arr.append(i)
                    result_arr.append(j)
                    return result_arr
                j += 1
            i += 1
        

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))