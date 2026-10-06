class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        left=0
        zeroc=0
        n=len(nums)
        for r in range(0,n):
            if nums[r]==0:
                zeroc+=1
            
            if zeroc>k:
                if nums[left]==0:
                    zeroc-=1
                left+=1
            
            
        
        return n-left