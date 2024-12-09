# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     stack = []
#     for c in s:
#         if c == '(' or c == '{' or c == '[':
#             stack.append(c)
#         elif c == ')':
#             if len(stack) == 0 or stack.pop() != '(':
#                 return False
#         elif c == '}':
#             if len(stack) == 0 or stack.pop() != '{':
#                 return False
#         elif c == ']':
#             if len(stack) == 0 or stack.pop() != '[':
#                 return False
#     return len(stack) == 0


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
        return len(stack) == 0

# Ejemplo de uso:
sol = Solution()
print(sol.isValid("(){}[]"))  # Debería devolver True
print(sol.isValid("([)]"))    # Debería devolver False
