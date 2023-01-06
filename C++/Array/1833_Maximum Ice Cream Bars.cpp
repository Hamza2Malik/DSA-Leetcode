class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(begin(costs), end(costs));
            
        int count = 0;
        
        for(auto it:costs){
            if(it > coins){
                return count;
            }
            else{
                coins -= it;
                    
                count++;
            }
        }
        
        return count;
    }
};