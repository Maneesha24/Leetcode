class Solution:
    def repeatedNTimes(self, A) -> int:
        n = len(A)/2
        char_count_obj = {}

        for num in A:
            if num in char_count_obj:
                char_count_obj[num] += 1
            else:
                char_count_obj[num] = 1

            if char_count_obj[num] == n:
                return num

sol = Solution()
print(sol.repeatedNTimes([1,2,3,3]))