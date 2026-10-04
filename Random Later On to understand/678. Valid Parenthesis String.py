class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_open tracks the minimum possible open brackets we MUST match.
        # max_open tracks the maximum possible open brackets we COULD have.
        min_open = 0
        max_open = 0
        
        for i in range(0, len(s)):
            if s[i] == '(':
                min_open += 1
                max_open += 1
            elif s[i] == ')':
                min_open -= 1
                max_open -= 1
            else:  # s[i] == '*'
                # If '*' is ')', open brackets decrease
                min_open -= 1
                # If '*' is '(', open brackets increase
                max_open += 1
            
            # If max_open drops below 0, we have too many close brackets ')'.
            # No amount of wildcards can fix this, so it's instantly invalid.
            if max_open < 0:
                return False
                
            # min_open can never realistically drop below 0. 
            # If it does, it just means we utilized a '*' as a ')' unnecessarily. We reset it to 0.
            if min_open < 0:
                min_open = 0
                
        # If min_open is 0, it means all required open brackets were successfully closed.
        return min_open == 0