class Solution {
    public int xorOperation(int n, int start) {
        int result=0, i=0;
        while(i<n){
            result^=start;
            start+=2;
            i++;
        }
        return result;
    }
}