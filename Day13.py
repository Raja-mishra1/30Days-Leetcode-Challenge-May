class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for idx in range(len(num)):
            while stack and k > 0:
                if num[idx] < stack[-1]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[idx])
        
        while k != 0:
            stack.pop()
            k -= 1
        
        while stack:
            if stack[0] == '0':
                stack = stack[1:]
            else:
                break
        
        return ''.join(stack) or '0'
