class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int currmin = 0;
        int currmax = 0;
        
        int globmin = nums[0];
        int globmax = nums[0];
        int total = 0;
        
        for(int n: nums){
            currmin = min(currmin + n, n);
            currmax = max(currmax + n, n);
            globmin = min(globmin, currmin);
            globmax = max(globmax, currmax);
            total += n;
            
        }
        
        return globmax > 0? max(globmax, total - globmin) : globmax;
    }
};