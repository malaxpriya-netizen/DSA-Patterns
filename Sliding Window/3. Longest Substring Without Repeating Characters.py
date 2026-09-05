class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        res=-1
        n=len(s)
        freq=dict()

        if n==0:
            return 0

        for right in range(0,n):
            freq[s[right]]=freq.get(s[right],0)+1
            k=right-left+1

            while len(freq)<k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
                k=right-left+1
            if len(freq)==k:
                res=max(res,right-left+1)
            
        return res
            


          
