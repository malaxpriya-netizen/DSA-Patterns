class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n=len(arr)
        
        sums=0
        high=k-1
        low=0
        for i in range(low,high):
            sums+=arr[i]
        
        sums+=arr[high]
        res=sums
        while high<n:
                res=max(res,sums)
                low+=1
                high+=1
                
                if high==n:
                    break
                sums=sums-arr[low-1]
                sums = sums+arr[high]
        
        return res