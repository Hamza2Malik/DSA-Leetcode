class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> nxtask;
        
        vector<array<int, 3>> sortedTasks;
        for(int i = 0 ; i< tasks.size(); i++){
            int enqueTime = tasks[i][0];
            int processingtime = tasks[i][1];
            sortedTasks.push_back({enqueTime, processingtime, i});
        }
        
        sort(begin(sortedTasks), end(sortedTasks));
        vector<int> res;
        
        int taskIndex = 0;
        long long currTime= 0;
        
        while(taskIndex < tasks.size() || !nxtask.empty()){
            if (nxtask.empty() && currTime < sortedTasks[taskIndex][0]) {
               
                currTime = sortedTasks[taskIndex][0];
            }
            
            while(taskIndex < tasks.size() && currTime >= sortedTasks[taskIndex][0]){
                nxtask.push({sortedTasks[taskIndex][1], sortedTasks[taskIndex][2]});
                taskIndex++;
            }
            
            auto [processTime, index] = nxtask.top();
            nxtask.pop();

            
            currTime += processTime;
            res.push_back(index);        
            
            }
        
        
        return res;
    }
};