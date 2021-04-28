class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int time=0;
        for(int i=0; i<points.length-1; i++){
           
            int sub1=Math.abs(points[i][0]-points[i+1][0]);
            int sub2=Math.abs(points[i][1]-points[i+1][1]);
            int ans= Math.max(sub1, sub2);
            time+=ans;
            
        }
        return time;
    }
}