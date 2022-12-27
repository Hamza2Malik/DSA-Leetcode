class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        
        int n = capacity.size();
        
        vector<int> diff(n,0);
        
        for(int i = 0;i<n;i++){
            diff[i] = capacity[i] - rocks[i];
        }
        
        int count = 0;
        sort(begin(diff), end(diff));
        
        for(int i = 0;i<n;i++){
            if(additionalRocks >= diff[i]){
                additionalRocks -= diff[i];
                count++;
            }
            else{
                break;
            }
        }
        
        return count;
    }
};