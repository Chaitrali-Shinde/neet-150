class Solution {
    
    public int removeDuplicates(int[] nums) {
            int prev=nums[0];
        for(int i=1; i<nums.length; i++){
            if(nums[i]==prev && nums[i]!=Integer.MAX_VALUE){
                nums[i]= Integer.MAX_VALUE;
            }else if(nums[i]!= Integer.MAX_VALUE){
                prev=nums[i];
            }
        }
        Arrays.sort(nums);
        int count=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]!= Integer.MAX_VALUE){
               count++;
            }
        }
        return count;
    }
}  