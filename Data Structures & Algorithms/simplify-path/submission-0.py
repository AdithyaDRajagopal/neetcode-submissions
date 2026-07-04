class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for folder in path.split('/'):
            if folder == '..':
                if stack:
                    stack.pop()
            elif folder != '.' and folder:
                stack.append(folder)

        return '/' + '/'.join(stack)