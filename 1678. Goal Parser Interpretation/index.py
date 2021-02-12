class Solution:
    def interpret(self, command: str) -> str:
        str_length = len(command)
        i = 0
        result = ''
        while(i < str_length):
            if command[i] == '(' and command[i + 1] == ')':
                result += 'o'
                i += 2
            elif command[i] != '(':
                result += command[i]
                i += 1
            else:
                result += 'al'
                i += 4

        return result

sol = Solution()
print(sol.interpret("G()(al)"))