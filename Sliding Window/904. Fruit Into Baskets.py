class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        k=2

        left=0
        freq=dict()
        max_len=0
        n=len(fruits)

        for right in range(0,n):
            freq[fruits[right]]=freq.get(fruits[right],0)+1

            while len(freq)>k:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        
        return max_len
