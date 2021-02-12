class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        val = (int(value) for value in str(n))
        sum = 0
        prod = 1
        for char in val:
            sum += char
            prod *= char
        return prod - sum

sol = Solution()
print(sol.subtractProductAndSum(234))