class Solution:
    def checkIfExist(self, arr):
        i = 0
        arr_len = len(arr)
        while(i < arr_len):
            j = i + 1
            while(j < arr_len):
                if (2 * arr[i]) == arr[j] or (2 * arr[j]) == arr[i]:
                    return True
                j += 1
            i += 1
        
        return False

sol = Solution()
print(sol.checkIfExist([10,2,5,3]))