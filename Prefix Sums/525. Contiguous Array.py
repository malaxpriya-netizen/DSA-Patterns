class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        freq=defaultdict(int)
        zero=0
        one=0
        res=0

        for i in range(0,len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff==0:
                res=max(res,i+1)
                continue
            
            if diff not in freq:
                freq[diff]=i
            
            else:
                idx=freq[diff]
                leng=i-idx
                res=max(leng,res)
        
        return res

