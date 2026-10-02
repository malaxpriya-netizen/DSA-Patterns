class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True


        
        n=len(s)-1
        i=0

        while i<n:
            if s[i]!=s[n]:
                return isPalindrome(i + 1, n) or isPalindrome(i, n - 1)
                
            i+=1
            n-=1
        
        return True



