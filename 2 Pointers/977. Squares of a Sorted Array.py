class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        a=[]
        b=[]
        res=[]
        for i in range(0,len(nums)):
            if nums[i]<0:
                a.append(nums[i])
            else:
                b.append(nums[i])


        if len(a)==0:
            for i in range(0,len(b)):
                b[i]=b[i]*b[i]
            return b
        
        if len(b)==0:
            for i in range(0,len(a)):
                a[i]=a[i]*a[i]
            a=a[::-1]
            return a
                
        
        for i in range(0,len(b)):
            b[i]=b[i]*b[i]

        for i in range(0,len(a)):
            a[i]=a[i]*a[i]
             
        a=a[::-1]
        n=len(a)
        m=len(b)

        i=j=0

        while i<n and j<m:
            if a[i]<=b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        
        while j<m:
            res.append(b[j])
            j+=1

        while i<n:
            res.append(a[i])
            i+=1

        return res   



