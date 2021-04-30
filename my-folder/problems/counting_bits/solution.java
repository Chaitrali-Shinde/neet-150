class Solution {

    
    public int[] countBits(int num) {
        int binary[]= new int[num+1];
        for(int i=0; i<=num; i++){
            int ans=0;
           for(int j=i; j>0;  j=j/2){
              ans+=j%2;     
           }
           binary[i]=ans;
        }
        return binary;
    }
}