class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> heap(piles.begin(),piles.end());
        int totalSum = accumulate(begin(piles), end(piles),0);
        
        for(int i = 0;i< k;i++){
            int maxi = heap.top();
            heap.pop();
            
            int remove = maxi/2;
            totalSum -= remove;
            heap.push(maxi-remove);
        }
        
        return totalSum;
    }
};