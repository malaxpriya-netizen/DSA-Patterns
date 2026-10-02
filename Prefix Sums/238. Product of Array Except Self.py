class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n=len(nums)

        countzer=0
        inderxzer=-1
        prod=1

        for i in range(0,n):
            if nums[i]==0:
                countzer+=1
                inderxzer=i
            
            else:
                prod*=nums[i]
        
        out=[0]*n

        if countzer==0:
            for i in range(0,n):
                out[i]=prod//nums[i]
            
        elif countzer==1:
            out[inderxzer]=prod
        
        return out
