class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        n = len(temperatures)-1    
        
        st = []
        
        for i in range(n, -1, -1):
            
            
            while st  and temperatures[i] >= temperatures[st[-1]]:
                
                st.pop()
            
            if( not st):
                res[i] = 0
            else:
                res[i] = st[-1] - i
            
            st.append(i)
        
        return res