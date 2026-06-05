class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not len(stack):
                stack.append(i)
                continue
            
            while len(stack) and temp > temperatures[stack[-1]]:
                top = stack.pop()
                res[top] = i - top
            
            stack.append(i)

        return res
                