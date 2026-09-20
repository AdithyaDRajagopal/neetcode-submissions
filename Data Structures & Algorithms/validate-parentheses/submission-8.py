class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = { '(': ')', '[': ']', '{': '}' }
        stack = []
        for c in s:
            if c in hashMap:
                stack.append(c)
                continue
            
            if len(stack) and c == hashMap[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0