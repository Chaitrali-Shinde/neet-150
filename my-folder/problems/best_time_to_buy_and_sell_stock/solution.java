class Solution {
    public int maxProfit(int[] prices) {
        int min=0, max=0;
        /*min=prices[0];
        for(int i=1; i<prices.length; i++){
            if(min>prices[i]){
                min=prices[i];
                position=i;
            }
        }
        
        if(position==prices.length-1){
            return 0;
        }else{
            max= position;
            for(int i=position+1; i<prices.length; i++){
                if(max<prices[i]){
                    max=prices[i];
                }
            }
        }*/
        int i=1;
        min= prices[0];
        while(i< prices.length){
          if(min>prices[i]){
              min=prices[i];
          }else if(prices[i]-min>max){
              max= prices[i]-min;
          }
            
            i++;
        }
        return (max);
    }
}