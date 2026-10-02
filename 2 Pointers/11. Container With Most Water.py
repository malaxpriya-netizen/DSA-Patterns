class Solution:
    def maxArea(self, height: list[int]) -> int:

        n=len(height)
        lp=0
        rp=n-1
        ans=0

        while lp<rp:
            w=rp-lp
            ht=min(height[lp],height[rp])
            wt=w*ht
            ans=max(wt,ans)

            if height[lp]<height[rp]:
                lp+=1
            else:
                rp-=1
        
        return ans
