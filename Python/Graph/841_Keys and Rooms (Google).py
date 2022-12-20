##################### DFS #####################
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False] * len(rooms)
        visited[0] = True
        
        def dfs(room):
            for val in rooms[room]:
                
                if(not visited[val]):
                    visited[val] = True
                    dfs(val)
        dfs(0)
        
        return all(visited)

################### BFS ####################3

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        
        q = deque([0])
        
        while q:
            node = q.popleft()
            
            
            for val in rooms[node]:
                if not visited[val]:
                    visited[val] = True
                    
                    q.append(val)
        return all(visited)