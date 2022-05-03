class Solution {
    
     boolean contains(char item, String s, int i){
            
            for(int j=0; j<s.length(); j++){
             if(s.charAt(j)==item && j!=i){
                 return true;
             }   
            }
            
            return false;
        }
        
    
    public int firstUniqChar(String s) {
        
        int i=0;
        for(i=0; i<s.length(); i++){
            if(!contains(s.charAt(i), s, i)){
                return i;
            }
        }
        return -1;
    }
}