class Solution:
    def findComplement(self, num):

        num_complement = ''
        while(num > 0):
            num_complement += f'{num%2}'
            num = num//2
        
        complement_val = self.complement(num_complement)
        decimal_val = self.decimalNum(complement_val)
        return decimal_val

    def complement(self, value):
        comp = ''
        value = str(value)
        for val in value:
            if val == '0':
                comp += '1'
            else:
                comp += '0'
        
        return comp

    def decimalNum(self, value):
        length = len(value)
        prod = 0
        i = 0
        while(i < length):
            if value[i] == '1':
                prod += self.power(i)
            i += 1
        return prod

    def power(self, pow):
        prod = 1
        i = 0
        while(i < pow):
            prod *= 2
            i += 1
        return prod

sol = Solution()
print(sol.findComplement(5))