class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = { '(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in hashMap:
                stack.append(c)
            elif not len(stack):
                return False
            else:
                top = stack.pop()
                if hashMap[top] != c:
                    return False
        
        return len(stack) == 0
        