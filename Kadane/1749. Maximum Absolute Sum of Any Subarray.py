class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        maxend=0
        minend=0
        max_sum=float('-inf')
        min_sum=float('inf')

        for i in range(0,len(nums)):
            maxend=max(nums[i],maxend+nums[i])
            max_sum=max(max_sum,maxend)

            minend=min(nums[i],minend+nums[i])
            min_sum=min(min_sum,minend)
        
        return max(abs(max_sum),abs(min_sum))