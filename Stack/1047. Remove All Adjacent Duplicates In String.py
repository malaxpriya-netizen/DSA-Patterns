class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = deque()
        n=len(s)
        res=str()

        for i in range(0,n):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if stack[-1]==s[i]:
                stack.pop()
                continue
            stack.append(s[i])

        return "".join(stack)


from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        n = len(s)
        res = ""  # Initialized as empty string literal

        for i in range(0, n):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if stack[-1] == s[i]:
                stack.pop()
                continue
            stack.append(s[i])

        # Pop one by one and add to the front of the string
        while stack:
            item = stack.pop()
            res = item + res  # Prepend to keep the correct order

        return re