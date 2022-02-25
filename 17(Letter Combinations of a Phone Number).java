
class Solution {
    
    public HashMap<Integer, String[]> LetterDict = new HashMap<Integer, String[]>();
    
    public List<String> S = new ArrayList<String>();
    
    // Define constructor to Initialize Hashmap 
    Solution(){
        
        
        this.LetterDict.put(2, new String[]  {"a","b", "c"});
        this.LetterDict.put(3, new String[] {"d","e","f"});
        this.LetterDict.put(4, new String[] {"g","h","i"});
        this.LetterDict.put(5, new String[] {"j","k","l"});
        this.LetterDict.put(6, new String[] {"m","n","o"});
        this.LetterDict.put(7, new String[] {"p","q","r","s"});
        this.LetterDict.put(8, new String[] {"t","u","v"});
        this.LetterDict.put(9, new String[] {"w","x","y","z"});
        
    }
    
    //Create a function for recursion
    public void Permutations(String Words, String digits){
        
        String Word;
        char d;
        String w[] = new String [4];
        //Add Words to the list
        if(digits.length()==0){
            Word = Words;
            this.S.add(Word);  
        }
        else{
            
            d = digits.charAt(0);
            System.out.println(d);
            digits = digits.substring(1);
            
            w = this.LetterDict.get(Character.getNumericValue(d));
           
            if(d == '7' || d=='9'){
            Words = Words + w[0];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);
            Words = Words + w[1];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);
            Words = Words + w[2];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);
            Words = Words + w[3];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);
                
                
            }else{
            
            Words = Words + w[0];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);
            Words = Words + w[1];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);
            Words = Words + w[2];
            Permutations(Words, digits);
            Words = Words.substring(0,Words.length()-1);}
        }
        
        return;
        
    }
    
    
    public List<String> letterCombinations(String digits) {
        
        
        String Words;
        Words = "";
        // check if the given string is empty
        if(digits.length() == 0){
                return S;
        }
        else{
            
            
            //Do something
            Permutations(Words, digits);
            
            
        }
        
        
        
        
        
        
            
        return S;
        
    }
}
