class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = { '[': ']', '(': ')', '{': '}' }
        stack = []

        for p in s:
            if p in hashMap:
                stack.append(p)
            else:
                if not len(stack):
                    return False
                
                top = stack.pop()
                if p != hashMap[top]:
                    return False
        
        return len(stack) == 0