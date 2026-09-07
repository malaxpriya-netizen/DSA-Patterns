class Solution:

    def fun(self, have: dict, need: dict) -> bool:
        for char, count in need.items():
            if have.get(char, 0) < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        m = len(t)
        have = dict()
        need = dict()
        if n < m:
            return ""
        for i in range(0, m):
            need[t[i]] = need.get(t[i], 0) + 1

        low = 0

        res = float("inf")
        start = -1

        for high in range(0, n):
            have[s[high]] = have.get(s[high], 0) + 1

            while self.fun(have, need):
                length = high - low + 1
                if res > length:
                    res = length
                    start = low

                have[s[low]] -= 1
                low += 1

        if res == float("inf"):
            return ""
        return s[start : start + res]