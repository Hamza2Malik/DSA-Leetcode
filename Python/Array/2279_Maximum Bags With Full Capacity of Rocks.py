class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        rem_cap = [cap-roc for cap, roc in zip(capacity, rocks)]
        
        rem_cap.sort();
        
        full = 0
        
        for curr in rem_cap:
            if additionalRocks >= curr:
                additionalRocks -= curr
                full +=1
            else:
                break
        
        
        return full