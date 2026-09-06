class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        res=0
        n=len(s)
        freq=dict()

        for right in range(0,n):
            freq[s[right]]=freq.get(s[right],0)+1
            maxcnt= max(freq.values()) if freq else 0

            winlen=right-left+1
            diff=winlen-maxcnt

            while diff>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1

                maxcnt=max(freq.values()) if freq else 0
                winlen=right-left+1
                diff=winlen-maxcnt
            res=max(res,right-left+1)
        return res