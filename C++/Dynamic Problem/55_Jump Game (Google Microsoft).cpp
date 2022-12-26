############# Memoization ##############
class Solution {
public:
    int t[1001];
    bool solve(vector<int> nums, int n, int idx){
        if(idx == n-1)
            return true;
        
        if(t[idx] != -1)
            return t[idx];
        for(int i =1;i<=nums[idx];i++){
            if(solve(nums, n, idx+i)==true)
                return true;
        }
        
        return false;
    }
    
    
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        memset(t, -1, sizeof(t));
        return solve(nums, n, 0);
    }
};
        


######################## Dp ######################
class Solution {
public:   
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<bool> dp(n,false);
        dp[0] = true;
        
        for(int i = 1; i < n;i++){
            for(int j = i-1; j >= 0; j--){
                if(dp[j]==true && j + nums[j] >= i){
                    dp[i] = true;
                    break;}
            }
        }
        
        return dp[n-1];
        
      
        
    }
};

################### Pattern 1 ####################
class Solution {
public:   
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int maxRea = 0;
        
        for(int i = 0; i < n;i++){
            if(i > maxRea){
                return false;
            }
            maxRea = max(maxRea, i+nums[i]);
        }
        
        return true;
        
        
    }
};
################### Pattern 3 ########################


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        goal = n-1
        
        for i in range (n-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
            
        
        return True if goal==0 else False 
            



