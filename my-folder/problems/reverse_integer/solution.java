class Solution {
    public int reverse(int x) {
     
        int reverse=0;
        int result=0;
        int size = String.valueOf(x).length();
        if(x<0){size=size-1;}
        for(int i=0; i<size; i++){
             if (result> Integer.MAX_VALUE / 10 || result < Integer.MIN_VALUE / 10){
                return 0;
            }
           int temp= x%10;
            result=(result*10)+temp;
            x=x/10;
       }
        
       // System.out.println(2^31);
        return result;
    }
}