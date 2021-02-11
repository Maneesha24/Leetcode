class Solution:
    def sumOfUnique(self, nums) -> int:
        
        unique_nums = {}
        sum = 0
        for num in nums:
            if num in unique_nums:
                unique_nums[num] += 1
            else:
                unique_nums[num] = 1

        for num in unique_nums:
            if unique_nums[num] == 1:
                sum += num

        return sum

sol = Solution()
print(sol.sumOfUnique([1,2,2,3]))