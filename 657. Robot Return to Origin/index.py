class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_axis = 0
        y_axis = 0
        for char in moves:
            if char == 'U':
                x_axis += 1
            
            elif char == 'D':
                x_axis -= 1

            elif char == 'L':
                y_axis -= 1

            else:
                y_axis += 1
        
        return  x_axis == 0 and  y_axis == 0

sol = Solution()
print(sol.judgeCircle('UD'))