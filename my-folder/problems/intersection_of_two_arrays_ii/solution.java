class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
      HashMap<Integer, Integer> arr= new HashMap<Integer, Integer>();
        List<Integer> uni= new ArrayList<Integer>();
        
        for(int e:nums1){
            if(arr.containsKey(e)){
                arr.put(e, arr.get(e)+1);
            }else{
                 arr.put(e, 1);
            }
        }
        
        for(int e: nums2){
            if(arr.containsKey(e) && arr.get(e)>0){
                uni.add(e);
                arr.put(e, arr.get(e)-1);
            }
        }
        
        int arr1[]= new int[uni.size()];
        int i=0;
        for(int e: uni ){
            arr1[i]=e;
            i++;
        }
       
        return arr1;
    }
}