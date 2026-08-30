class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        off=0
        res=1
        cm=1

        while cm<len(nums):
            if nums[cm] == nums[cm-1]:
                cm+=1
                continue
            else:
                nums[off+1]=nums[cm]
                off+=1
                res+=1
                cm+=1
        
        return res

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = dict()
        n = len(nums)  # define n inside the method
        
        for i in range(n):
            seen[nums[i]] = 0
        
        j = 0
        for k in seen:
            nums[j] = k
            j += 1
        
        return j



"""