class Solution {
    public int percentageLetter(String s, char letter) {
        int total= s.length();
        int count=0;
        for(int i=0; i<s.length(); i++){
            char s1= s.charAt(i);
           // System.out.println(s1);
            if(s1==letter){
               count++; 
            } 
        }
        if(count==0) return 0;
                    
       // System.out.println(count);
       // System.out.println(total);
        
        int percent= (count*100)/total;
        //System.out.println(percent);
        return percent;
    }
}