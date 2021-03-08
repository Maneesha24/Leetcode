class Solution:
    def numIdenticalPairs(self, nums) -> int:
        i = 0
        count = 0
        arr_len = len(nums)

        while(i < arr_len):
           j = i + 1
           while(j < arr_len):
               if nums[i] == nums[j]:
                   count += 1
               j += 1

           i += 1

        return count


sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))