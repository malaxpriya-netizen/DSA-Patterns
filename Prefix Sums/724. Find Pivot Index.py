class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left=0

        sum=0

        for i in range(0,len(nums)):
            sum+=nums[i]
        
        for j in range(0,len(nums)):
            
            right=sum-nums[j]-left
            if left==right:
                return j
            left+=nums[j]
        
        return -1