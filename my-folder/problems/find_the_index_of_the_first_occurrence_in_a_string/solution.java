class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length()==0){
            return 0;
        }
        if(needle.length()>haystack.length()){
            return -1;
        }
        
        if(needle.length()==haystack.length()&& needle.equals(haystack)){
            return 0;
        }
        
        for(int i=0; i<=(haystack.length()-needle.length()); i++){
            String s=haystack.substring(i, i+needle.length());
            //System.out.println(s);
            if(s.equals(needle)){
                return i;
            }
        }
        return -1;
    }
}