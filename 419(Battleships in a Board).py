class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
       
        Ship_Coordinates_y = {}
        
        ship_count = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if(board[i][j] == "X"):
                    
                    if(j==0 and i==0):
                        ship_count+=1
                    elif(i>0 and j>0):
                        if(board[i][j-1]=="X" or board[i-1][j]=="X"):
                            continue
                        else:
                            ship_count+=1
                    elif(j==0 and i>0):
                        if(board[i-1][j]=="X"):
                            continue
                        else:
                            ship_count+=1
                    elif(j>0 and i==0):
                        if(board[i][j-1]=="X"):
                            continue
                        else:
                            ship_count+=1
                        
                            
        
        return ship_count
                        
                    
