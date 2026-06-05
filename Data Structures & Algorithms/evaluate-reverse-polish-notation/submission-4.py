class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def compute(op1, op2, operator):
            if operator == '+':
                return op2 + op1
            elif operator == '-':
                return op2 - op1
            elif operator == '*':
                return op2 * op1
            elif operator == '/':
                return int(op2/op1)

        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(compute(op1, op2, token))
        
        return stack[0]