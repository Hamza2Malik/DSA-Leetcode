class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        
        costs.sort()
         
        
        count = 0
        
        for i in costs:
            if i > coins:
                return count
            else:
                count+=1
                coins -= i
        return count