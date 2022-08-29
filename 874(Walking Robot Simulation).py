class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        #create dicts for x and y axis:
        obs = {}
        
        for i in obstacles:
            obs[(i[0],i[1])] = 1
            
        #create list for result:
        result = []
        
        
        
        #Function that facilitates movement
        def Move(self, Orientation, x , y, Steps):
            count = 0
            while(count < Steps):
                if(Orientation =='U'):
                    y += 1
                    count+=1
                    if (x,y) in obs:
                        y-=1
                        break
                if(Orientation =='D'):
                    y -= 1
                    count+=1
                    if (x,y) in obs:
                        y+=1
                        break
                if(Orientation =='L'):
                    x -= 1
                    count+=1
                    if (x,y) in obs:
                        x+=1
                        break
                if(Orientation == 'R'):
                    x += 1
                    count+=1
                    if (x,y) in obs:
                        x-=1
                        break

            return [x,y]
        
        
        #Start Co-Ordinaties 
        x,y = 0,0
        
        #Set the Initial Orientation
        Orientation = 'U'
        
        for cmd in commands:
             # If the command is to move ahead by a particular number of steps
                if cmd > 0:
                    
                    print(cmd,Orientation, x,y)
                    
                    ans = Move(self,Orientation, x, y, cmd)
                    x,y = ans[0],ans[1]
                    #Calculate distance
                    total_dist = x**2 + y**2
                    result.append(total_dist)
                    
                    
                else:
                    if(Orientation == 'U' and cmd == -1):
                        Orientation = 'R'
                    elif(Orientation == 'U' and cmd == -2):
                        Orientation = 'L'
                    elif(Orientation == 'D' and cmd == -1):
                        Orientation = 'L'
                    elif(Orientation == 'D' and cmd == -2):
                        Orientation = 'R'
                    elif(Orientation == 'R' and cmd == -1):
                        Orientation = 'D'
                    elif(Orientation == 'R' and cmd == -2):
                        Orientation = 'U'
                    elif(Orientation == 'L' and cmd == -1):
                        Orientation = 'U'
                    elif(Orientation == 'L' and cmd == -2):
                        Orientation = 'D'
          
   
        
        result.sort(reverse=True)
        return result[0]
                        
                        
                            
                            
                            
                
               
                        
                        
                    
                
                
            
        
            
        
        
        
        
        
        
