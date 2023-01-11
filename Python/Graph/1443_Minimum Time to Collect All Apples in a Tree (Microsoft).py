class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(graph, hasApple, node, parent):
            totalTime = 0
            childTime = 0
            
            for child in graph[node]:
                if child == parent:
                    continue
                childTime = dfs(graph, hasApple, child, node)
                    
                if(childTime > 0 or hasApple[child]):
                    totalTime += 2+ childTime
                
            return totalTime
        
        
        return dfs(graph, hasApple, 0, -1)
                    