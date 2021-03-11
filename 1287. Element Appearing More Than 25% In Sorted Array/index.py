class Solution:
    def findSpecialInteger(self, arr):
        charObj = {}
        k = len(arr)/4

        for val in arr:
            if val in charObj:
                charObj[val] += 1
            else:
                charObj[val] = 1

            if charObj[val] > k:
                return val

sol = Solution()
print(sol.findSpecialInteger([1,2,2,6,6,6,6,7,10]))