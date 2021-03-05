class Solution:
    def shuffle(self, nums, n: int):
        n = round(len(nums)/2)
        result_arr = []
        i = 0

        while(i < n):
            result_arr.append(nums[i])
            result_arr.append(nums[ n + i])
            i += 1
        
        return result_arr

sol = Solution()
print(sol.shuffle([2,5,1,3,4,7], 3))