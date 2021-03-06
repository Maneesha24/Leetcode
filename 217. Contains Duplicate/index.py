class Solution:
    def containsDuplicate(self, nums):
        charObj = {}
        for val in nums:
            if val in charObj:
                return True
            else:
                charObj[val] = 1
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))