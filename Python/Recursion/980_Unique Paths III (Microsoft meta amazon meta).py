class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.result = 0
        nonObs = 0
        directions = [[1,0], [-1,0],[0,1],[0,-1]]
        
        start_x = 0
        start_y = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    nonObs += 1
                elif grid[i][j] == 1:
                    start_x = i
                    start_y = j
                    nonObs+=1
        
        
        def dfs(count, i, j):
            if i < 0 or i >= m or j <0 or j >= n or grid[i][j] == -1:
                return
            if grid[i][j]==2:
                if count == nonObs:
                    self.result +=1
                return
            
            
            grid[i][j] = -1
            
           
            dfs(count+1, i +1, j)
            dfs(count+1, i -1, j)
            dfs(count+1, i, j+1)
            dfs(count+1, i, j-1)
                
            grid[i][j] = 0
            
        dfs(0, start_x, start_y)
        
        return self.result