############### dp ################
class Solution {
public:
    long mod = 1e9 + 7;   
    
    int numTilings(int n) {
        vector <int> dp(1001, -1);
        dp[0]=1, dp[1]=1, dp[2] =2;
        
        for(int i = 3;i<=n;i++){
            dp[i] = (2 * dp[i-1] % mod + dp[i-3]%mod)% mod;
        }
        
        return dp[n];
        
    }
};

################ Memoization  ###############
class Solution {
public:
    long mod = 1e9 + 7;
    int solve(vector <int> &dp, int n){
        if(dp[n] != -1){
            return dp[n];
        }
        
        return dp[n] = (2 * solve(dp,n-1) % mod + solve(dp, n-3)%mod)% mod;
    }
    
    
    int numTilings(int n) {
        vector <int> dp(1001, -1);
        dp[0]=1, dp[1]=1, dp[2] =2;
        return solve(dp, n);
        
        
        
    }
};