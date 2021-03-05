class Solution:
    def smallerNumbersThanCurrent(self, nums):

        i = 0
        arr_len = len(nums)
        result_arr = []

        while(i < arr_len):
            count = 0
            j = 0
            while(j < arr_len):
               if nums[i] > nums[j]:
                   count += 1
               j += 1

            result_arr.append(count)
            i += 1

        return result_arr


sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))