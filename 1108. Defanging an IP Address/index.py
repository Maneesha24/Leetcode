class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = 0
        result_str = ''
        while(i < len(address)):
            if address[i] == '.':
                result_str += '[.]'
            else:
                result_str += address[i]
            i += 1

        return result_str


sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))
