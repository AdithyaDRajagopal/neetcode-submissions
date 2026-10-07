class Solution:
    def compute(self, op1: int, op2: int, operator: str) -> int:
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        else:
            return int(op1/op2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                res = self.compute(op1, op2, token)
                stack.append(res)
        
        return stack.pop()