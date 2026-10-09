from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # 1. Create a padded 2D prefix sum matrix of size (m+1) x (n+1)
        # pref[i][j] stores the sum of mat[0..i-1][0..j-1]
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                pref[r + 1][c + 1] = mat[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]
        
        # 2. Allocate the result matrix
        ans = [[0] * n for _ in range(m)]
        
        # 3. Calculate block sums using 1-indexed coordinates
        for r in range(m):
            # Define 0-indexed boundaries clamped to matrix limits
            r1, r2 = max(0, r - k), min(m - 1, r + k)
            
            for c in range(n):
                c1, c2 = max(0, c - k), min(n - 1, c + k)
                
                # Convert boundaries to 1-indexed for the prefix matrix query
                # Box sum = pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
                ans[r][c] = pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
                
        return ans