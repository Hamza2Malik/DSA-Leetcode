################### Trick Solution ###################

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        no_of_ones = 0
        flip = 0
        
        for ch in s:
            if ch == "1":
                no_of_ones += 1
            else:
                flip = min(flip+1, no_of_ones)
        
        return flip

################### Memoziation ###################
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        #dp = [[-1 for i in range(2)] for i in range(n)]
        dp ={}
        
        def solve(curr_index, prev):
            
            if curr_index >= n:
                return 0
            
            if (curr_index,prev) in dp:
                return dp[(curr_index,prev)]
            
            flip = float('inf')
            noflip = float('inf')
            
            if(s[curr_index]=='0'):
                
                if(prev == 1):
                    
                    flip = 1 + solve(curr_index+1, 1)
                
                else:
                    
                    flip = 1 + solve(curr_index+1,1)
                    noflip = solve(curr_index+1,0)
                
            
            elif(s[curr_index]=='1'):                
                if prev == 1:
                    noflip = solve(curr_index+1,1)
                else:
                    flip = 1+solve(curr_index+1,0)
                    noflip = solve(curr_index+1,1)
            
            value = min(flip, noflip)
            dp[(curr_index,prev)] = value
            
            return dp[(curr_index,prev)]
        
        
        return solve(0,0)
        
                    
################### Memoziation ###################

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        dp = [[-1 for i in range(2)] for i in range(n)]
        
        def solve(curr_index, prev):
            
            if curr_index >= n:
                return 0
            
            if dp[curr_index][prev] != -1:
                return dp[curr_index][prev]
            
            flip = float('inf')
            noflip = float('inf')
            
            if(s[curr_index]=='0'):
                
                if(prev == 1):
                    
                    flip = 1 + solve(curr_index+1, 1)
                
                else:
                    
                    flip = 1 + solve(curr_index+1,1)
                    noflip = solve(curr_index+1,0)
                
            
            elif(s[curr_index]=='1'):                
                if prev == 1:
                    noflip = solve(curr_index+1,1)
                else:
                    flip = 1+solve(curr_index+1,0)
                    noflip = solve(curr_index+1,1)
            
            dp[curr_index][prev] = min(flip, noflip)
            return dp[curr_index][prev]
        
        
        return solve(0,0)


################### Recursive ##################
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
       
        
        def solve(curr_index, prev):
            
            if curr_index >= n:
                return 0
            
            flip = float('inf')
            noflip = float('inf')
            
            if(s[curr_index]=='0'):
                
                if(prev == 1):
                    
                    flip = 1 + solve(curr_index+1, 1)
                
                else:
                    
                    flip = 1 + solve(curr_index+1,1)
                    noflip = solve(curr_index+1,0)
                
            
            elif(s[curr_index]=='1'):                
                if prev == 1:
                    noflip = solve(curr_index+1,1)
                else:
                    flip = 1+solve(curr_index+1,0)
                    noflip = solve(curr_index+1,1)
            return min(flip, noflip)
        
        
        return solve(0,0)
        