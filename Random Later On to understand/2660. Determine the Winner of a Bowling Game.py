class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:


        sums=0
        sums1=0

        for i in range(0,len(player1)):

            if (i > 0 and player1[i-1] == 10) or (i > 1 and player1[i-2] == 10):
                 sums += 2 * player1[i]

                   
            else:
                sums += player1[i]
                    
        
        for j in range(0,len(player2)):
             if (j > 0 and player2[j-1] == 10) or (j > 1 and player2[j-2] == 10):
                 sums1 += 2 * player2[j]
                   
             else:
                sums1 += player2[j]
                    

            
        if sums>sums1:
            return 1
        elif sums<sums1:

            return 2
        else:
            return 0
            


        
      