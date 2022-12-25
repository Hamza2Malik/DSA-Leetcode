################ Memoziation ##########################
class Solution {
public:
    int t[5001][2];
    int solve(vector<int> prices, int day, int n, bool buy){
        if(day >= n)
            return 0;
        
        if(t[day][buy]!= -1){
            return t[day][buy];
        }
        int profit = 0;
        if(buy){
            int take = solve(prices,day+1, n, false) - prices[day];  // function call for selling then sell - buy = profit
            int nottake = solve(prices,day+1, n, true);
            profit = max({profit, take, nottake});
        }
        else{
            int sell = prices[day] + solve(prices, day+2,n,true);
            int notsell = solve(prices, day+1,n,false);
            profit = max({profit, sell,notsell});
        }
        return t[day][buy] = profit;
    }
    
    
    
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        bool buy = true;
        memset(t,-1,sizeof(t));
        return solve(prices, 0, n,buy);
    }
};


######################### DP #####################

class Solution {
public:  
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n==0 || n==1)
            return 0;
        
        vector<int> t(n,0);
        
        t[0] = 0;
        t[1] = max(prices[1]-prices[0],0);
        
        for(int i = 2; i<n;i++){
            t[i] = t[i-1];
            for(int j = 0; j<=i-1;j++){
                int today_profit = prices[i] - prices[j];
                int prevPro = j >= 2? t[j-2]: 0;
                
                t[i] = max(t[i], today_profit + prevPro);
            }    
        }
            return t[n-1];
        
    }
};