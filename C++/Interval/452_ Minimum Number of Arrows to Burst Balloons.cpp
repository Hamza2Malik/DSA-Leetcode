class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int n = points.size();
        
        sort(begin(points), end(points));
        
        vector<int> prev = points[0];
        
        int count = 1;
        for (int i = 1; i<n;i++){
            int currSp = points[i][0];
            int currEp = points[i][1];
            
            int prevSp = prev[0];
            int prevEp = prev[1];
            
            if(currSp > prevEp){
                count++;
                
                prev = points[i];
            }
            else{
                prev[0] = max(prevSp, currSp);
                prev[1] = min(prevEp, currEp);
                
            }
            
            
        }
        
        return count;
    }
};