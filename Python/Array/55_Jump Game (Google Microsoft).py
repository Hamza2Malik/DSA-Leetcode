############# Memoization ##############
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n
        
        def solve(idx):
            if(idx ==n-1):
                return True
            
            if(dp[idx] != -1):
                return dp[idx]
            for i in range(1, nums[idx]+1):
                if solve(idx+i):
                    dp[idx]= True
                    return dp[idx]
            dp[idx] = False
            return dp[idx]
        
        return solve(0)
        


######################## Dp ######################
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [False] * n
        dp[0] = True
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if(dp[j]==True and j+nums[j]>=i):
                    dp[i]= True        
                    break
        return dp[n-1]

################### Pattern 1 ####################
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        maxReachable = 0
        
        for i in range (n):
            if(i > maxReachable):
                return False
            maxReachable = max(maxReachable, i+nums[i])
        
        return True
################### Pattern 3 ########################


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        goal = n-1
        
        for i in range (n-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
            
        
        return True if goal==0 else False 




