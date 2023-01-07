////////////////////////// Brute Force ///////////////////

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        for(int i =0; i<n;i++){
            if(gas[i] < cost[i])
                continue;
            int j = (i+1)%n;
            
            int currCost = gas[i] - cost[i] + gas[j];
            
            while(j !=i){
                if(currCost < cost[j])
                    break;
                
                
                int costOfnew = cost[j];
                
                
                j = (j+1)%n;
                currCost = currCost - costOfnew + gas[j];
            }
            
            if(j==i)
                return i;
        }
        
        return -1;
        
    }
};

//////////////////////////// Greedy /////////////////////////

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int totalgas = accumulate(begin(gas), end(gas),0);
        int totalcost = accumulate(begin(cost), end(cost), 0);
        if(totalgas < totalcost){
            return -1;
        }
        
        int total = 0;
        int index = 0;
        for(int i = 0; i<n;i++){
            total += gas[i] - cost[i];
            
            if(total<0){
                index = i+1;
                total = 0;
            }
        }
        
        return index;
        
        
    }
};