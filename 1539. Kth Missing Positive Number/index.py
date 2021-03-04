class Solution:
    def findKthPositive(self, arr, k):
        i = 0
        arr_len = arr[len(arr) - 1] + k
        result_arr = []

        while(i < arr_len):
            if i < arr[len(arr) - 1]:
                if i + 1 not in arr:
                    result_arr.append(i + 1)
            else:
                result_arr.append(i + 1)

            if len(result_arr) == k:
                return result_arr[k - 1]

            i += 1

sol = Solution()
print(sol.findKthPositive([2,3,4,7,11], 5))