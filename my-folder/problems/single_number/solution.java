class Solution {
    
    boolean contains(int[] nums, int position, int x){
        for(int i=0; i<nums.length; i++){
            if(position!=i){
                if(x==nums[i]){
                   return true;
                }
            }
        }
       return false;
    }
    
    public int singleNumber(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
    
        for(int i=0; i<nums.length; i++){
            if(!contains(nums, i, nums[i])){
                return nums[i];
            }
        }
        return 0;
    }
}