################ Brute Force #################

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        if(n==1):
            return 1
        
        
        result = 0 
        
        for i in range(n):
            for j in range(i+1, n):
                count = 2
                
                dx = points[j][0] -  points[i][0]
                dy = points[j][1] -  points[i][1]
                
                for k in range(n):
                    if k==i or k==j:
                        continue
                    
                    dx_ = points[k][0] -  points[i][0]
                    dy_ = points[k][1] -  points[i][1]
                
                    if(dx*dy_==dy*dx_):
                        count +=1
                result = max(result, count)
        
        return result

############## Approach 2 ######################

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        if(n==1):
            return 1
        
        
        result = 0 
        
        for i in range(n):
            mp = {}
            for j in range(n):
                if(i==j):
                    continue
                
                dx = points[j][0] -  points[i][0]
                dy = points[j][1] -  points[i][1]
                
                theta = math.atan2(dy,dx)
                
                mp[theta] = 1 + mp.get(theta,0)
            result = max(result, max(mp.values())+1)
        
        return result

########## Approach 3 ##############

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        if(n==1):
            return 1
        
        
        result = 0 
        
        for i in range(n):
            mp = {}
            for j in range(n):
                if(i==j):
                    continue
                
                dx = points[j][0] -  points[i][0]
                dy = points[j][1] -  points[i][1]
                
                gc = gcd(dy, dx)
                
                key = str(dy/gc) + "_" + str(dx/gc)
                
                mp[key] = 1 + mp.get(key,0)
            result = max(result, max(mp.values())+1)
        
        return result