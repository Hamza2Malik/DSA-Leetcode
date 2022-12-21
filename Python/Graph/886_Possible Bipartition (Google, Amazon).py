########################## DFS ##############################
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def dfs(source, nodecolor):
            
            color[source] = nodecolor
            
                
            for nei in adj[source]:
                if(color[nei]==color[source]): return False
                if(color[nei]==-1):
                    
                    if not dfs(nei, 1-nodecolor):
                        return False
            return True
        
        adj = [[] for _ in range(n+1)]
        
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        color = [-1] * (n+1)
        
        for i in range(1, n+1):
            if color[i]==-1:
                if not (dfs(i,0)):
                    return False
        return True



########################## BFS ##############################

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(source):
            q = deque([source])
            color[source] = 0
            while q:
                node = q.popleft()
                
                for nei in adj[node]:
                    if(color[nei]==color[node]): return False
                    if(color[nei]==-1):
                        color[nei] = 1 - color[node]
                        q.append(nei)
            return True
        
        adj = [[] for _ in range(n+1)]
        
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        color = [-1] * (n+1)
        
        for i in range(1, n+1):
            if color[i]==-1:
                if not (bfs(i)):
                    return False
        return True