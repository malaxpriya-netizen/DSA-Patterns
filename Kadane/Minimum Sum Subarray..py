class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        best = arr[0]
        ans = arr[0]
        for i in range(1, len(arr)):
            best = min(best + arr[i], arr[i])
            ans = min(ans, best)
        return ans
