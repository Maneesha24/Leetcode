class Solution:
    def maximumWealth(self, accounts):
        i = 0
        customerData = []
        while(i < len(accounts)):
            j = 0
            customerWealth = 0
            while (j < len(accounts[i])):
                customerWealth += accounts[i][j]
                j += 1
            
            i += 1
            customerData.append(customerWealth)

        return max(customerData)


sol = Solution()
print(sol.maximumWealth([[1,2,3],[3,2,1]]))