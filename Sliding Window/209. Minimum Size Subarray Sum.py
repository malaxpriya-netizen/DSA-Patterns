class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left=0
        n=len(nums)
        window=0
        lens=float('inf')

        for right in range(0,n):
            window+=nums[right]

            while window>=target:
                 lens=min(lens,right-left+1)
                 window-=nums[left]
                 left+=1
        
        if lens==float('inf'):
            return 0
        else:
            return lens
      