class Solution {
    public int maxArea(int[] height) {
        
 
        int l1= 0;
        int l2= height.length - 1;
        int max = Math.min(height[l1],height[l2])*(l2-l1);
        
        while(l1 < l2){
            
            
            int res = Math.min(height[l1],height[l2])*(l2-l1);
            
            if(res > max){
                max = res;
            }
          
            
            
            if(Math.min(height[l1],height[l2]) == height[l1]){
                int temp_max = height[l1];
                while(height[l1] <= temp_max ){
                    if(l1 == height.length-1){
                        break;
                    }
                    l1 = l1 + 1;
                }
            }
            else if(Math.min(height[l1],height[l2]) == height[l2]){
                int temp_max = height[l2];
                while(height[l2] <= temp_max){
                    if(l2 == 0){
                        break;
                    }
                    l2 = l2 - 1;
                }
            }
            
            
        }
 
                     return max;       
                }
                
    
  
                
            }
   
        
        


