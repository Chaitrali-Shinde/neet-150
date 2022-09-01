class Solution {
    int febo(int nums[], int i){
        int ans=0;
        for(int j=0; j<=i; j++){
            ans+= nums[j];
        }
        return ans;
    }
    public int[] runningSum(int[] nums) {
        int [] result= new int[nums.length];
        result[0]= nums[0];
        for(int i=1; i<nums.length; i++){
            result[i]= febo(nums,i);
        }
        
        return result;
    }
}