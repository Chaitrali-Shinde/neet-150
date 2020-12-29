class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int temp=0, flag=0;
        temp= nums[0];
        for(int i=1; i<nums.length; i++){
            if(temp==nums[i]){
                flag=1;
                return temp;
            }else{
                temp= nums[i];
            }
        }
        return flag;
    }
}