class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        res=arr[0]
        nodel=arr[0]
        onedel=float('-inf')

        for i in range(1,len(arr)):
            prevnod=nodel
            nodel=max(arr[i],nodel+arr[i])
            onedel=max(prevnod,onedel+arr[i])
            res=max(res,max(nodel,onedel))
        
        return res