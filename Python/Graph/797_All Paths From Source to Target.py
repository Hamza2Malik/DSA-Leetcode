##################### DFS ######################
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(curr, path):
            if curr == len(graph)-1:
                res.append(path)
            else:
                for i in graph[curr]:
                    dfs(i, path + [i])
                    
        res= []
        
        dfs(0,[0])
        return res


##################### BFS ##########################

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, q = [], deque([[0]])
        while q:
            path = q.popleft()
            if path[-1] == len(graph)-1: ans.append(path)
            else:
                q.extend(path + [child] for child in graph[path[-1]])
        return ans
