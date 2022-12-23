################ Memoziation ##########################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = {}
        
        def solve(day, buy):
            
            if(day >= n):
                return 0;
            
            if (day, buy) in dp:
                return dp[(day,buy)]
            
            profit = 0
            if buy:
                take = solve(day+1, not buy) - prices[day]
                not_take = solve(day+1, buy)
                profit = max(profit, take, not_take)
            else:
                sell = prices[day] + solve(day+2, not buy)
                not_sell = solve(day+1, buy)
                profit = max(profit, sell, not_sell)
            
            dp[(day,buy)] = profit
            return dp[(day,buy)]
        
        return solve(0, True)


######################### DP #####################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n==0 or n==1):
            return 0
        dp = [0] * n
        
        dp[0] = 0
        dp[1] = max(prices[1]-prices[0],0)
        
        for i in range(2, len(prices)):
            dp[i] = dp[i-1]
            for j in range(0, i):
                today_profit = prices[i] - prices[j]
                prevpro = dp[j-2] if j>= 2 else 0
                
                dp[i] = max(dp[i], today_profit + prevpro)
        return dp[n-1]