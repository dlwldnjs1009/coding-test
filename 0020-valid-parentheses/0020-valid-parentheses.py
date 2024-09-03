# 꺼낼때 확인하는 과정을 거쳐야 하는데
# stack = [], a= '('
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            a = 0
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == '[':
                stack.append(char)
            elif char == ']':
                if not stack:
                    return False
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == '{':
                stack.append(char)
            elif char == '}':
                if not stack:
                    return False
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    return False
                    
        if not stack:
            return True
        else:
            return False
        