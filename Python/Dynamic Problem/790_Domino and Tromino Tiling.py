############# DP ###########
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        dp =  [-1] * (1001)
        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            dp[i] = (2*dp[i-1]%mod + dp[i-3]%mod) % mod
            
        return dp[n]

############ Memoziation ##########

class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        dp =  [-1] * (1001)
        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        def solve(n):
            if dp[n] != -1:
                return dp[n]
            dp[n] = (2*solve(n-1)%mod + solve(n-3)%mod) % mod
            
            return dp[n]
        return solve(n)