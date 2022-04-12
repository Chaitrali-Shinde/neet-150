class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        ArrayList<Integer> arr= new ArrayList<Integer>();
        while(x!=0){
            arr.add(x%10);
            x=x/10;
        }
        int size= arr.size();
        for(int i=0; i<size; i++){
            size--;
            if(arr.get(i)!=arr.get(size)){
                return false;
            }
        }
        return true;
    }
}