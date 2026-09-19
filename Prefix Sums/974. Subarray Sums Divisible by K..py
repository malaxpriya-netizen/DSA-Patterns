class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        frequency = defaultdict(int)
        frequency[0] = 1

        sums=0
        res=0

        for i in range(0,len(nums)):
            sums+=nums[i]
            rem=sums%k
            if rem<0:
                rem=rem+k
            
            res+=frequency[rem]
            frequency[rem]+=1
        
        return res