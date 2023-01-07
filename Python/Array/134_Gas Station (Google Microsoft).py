######################## Brute Force #######################

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        for i in range(n):
            if(gas[i] < cost[i]):
                continue
            j = (i+1)%n
            currtotal = gas[i] - cost[i] + gas[j]
            
            while(j != i):
                if(currtotal < cost[j]):
                    break;
                
                newcost = cost[j]
                j = (j+1)%n
                currtotal = currtotal - newcost + gas[j]
                
                
            
            if(i==j):
                return i
            
        return -1
        

############################## Greedy###############################

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        totalgas = sum(gas)
        totalcost = sum(cost)
        
        if(totalgas < totalcost):
            return -1
        
        total = 0
        index = 0
        for i in range(n):
            total += gas[i] - cost[i]
            
            if(total <0):
                index = i+1
                total = 0
        
        return index
        

