class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        n=len(s)

        for i in range(0,n):
            if s[i]=="(" or s[i] == "{" or s[i]== "[":
                stack.append(s[i])

            else:
                if not stack:
                    return False

                

                top = stack.pop()
                
                if s[i] == ")" and top != "(":
                    return False
                if s[i] == "}" and top != "{":
                    return False
                if s[i] == "]" and top != "[":
                    return False
        return len(stack) == 0