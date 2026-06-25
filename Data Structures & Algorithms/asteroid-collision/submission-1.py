class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(ast) > abs(top):
                    stack.pop()
                elif abs(ast) < abs(top):
                    ast = 0
                else:
                    stack.pop()
                    ast = 0
            
            if ast:
                stack.append(ast)
        
        return stack