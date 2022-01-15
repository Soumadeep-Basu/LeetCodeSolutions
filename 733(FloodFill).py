class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
       
        visited = []
        
        def fill(posx, posy, colour, image, check):
            
            if(posx > len(image)-1 or posy > len(image[0])-1 or image[posx][posy]!=check or posx<0 or posy<0 or visited.count([posx,posy])==1):
                return image
            else:
                if(image[posx][posy] == check):
                    image[posx][posy] = colour
                    temp = [posx, posy]
                    visited.append(temp)
                    
                    image = fill(posx+1 , posy, colour, image, check)
                    image = fill(posx-1 , posy, colour, image, check)
                    image = fill(posx , posy+1, colour, image, check)
                    image = fill(posx , posy-1, colour, image, check)
                    
                    
            return image
        
        check = image[sr][sc]
        
        image = fill(sr, sc, newColor, image, check)
        
        return image
