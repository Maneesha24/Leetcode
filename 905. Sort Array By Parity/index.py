class Solution:
    def sortArrayByParity (self, A):
        result_arr = []
        for val in A:
            if val%2 != 0:
                result_arr.append(val)
            else:
                result_arr.insert(0, val)

        return result_arr       

sol = Solution()
print(sol.sortArrayByParity([3,1,2,4]))