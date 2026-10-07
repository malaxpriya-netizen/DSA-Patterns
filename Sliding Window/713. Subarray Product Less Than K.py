class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        l=0
        prod=1
        ans=0
        for r in range(0,len(nums)):
            prod*=nums[r]
            while prod>=k:
                prod=prod//nums[l]
                l+=1
            ans+=r-l+1
        
        return ans