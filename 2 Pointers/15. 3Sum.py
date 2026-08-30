class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        res=[]

        n=len(nums)

        for i in range(0,n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            add= -1 * nums[i]

            while left<right:
                s=nums[left]+nums[right]
                if s==add:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                     
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                
                elif s<add:
                    left+=1
                    
                else:
                    right-=1
                
        return res        
            

                
            
          
            

            