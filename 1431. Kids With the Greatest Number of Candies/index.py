class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        maxCandies = max(candies)
        result = [candy + extraCandies >= maxCandies for candy in candies]
        return result
        

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3], 3))
