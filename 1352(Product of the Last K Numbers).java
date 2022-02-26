class ProductOfNumbers {
    
    public ArrayList<Integer> stack = new ArrayList<Integer>();

    public ProductOfNumbers() {
        
        //Do Nothing
        
        
    }
    
    public void add(int num) {
        
        this.stack.add(num);
        
        
    }
    
    public int getProduct(int k) {
        
        
        int res = 1;
     
        for (int i= 1; i <= k ; i++){
            
            res = res * this.stack.get(this.stack.size() - i);
        }
     
            
            
            
            
        
         return res;
        }
    
   
        
    }


/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
