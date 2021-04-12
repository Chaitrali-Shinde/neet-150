class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int cnt=numBottles;
        int temp=0;
        while(numBottles>=numExchange){
            temp+=numBottles/numExchange; 
            numBottles=numBottles/numExchange + numBottles%numExchange; 
        }
        cnt+=temp;
        return cnt;
        
    }
}