####################### DFS ######################
from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        def help(i,p):
            t=d[labels[i]]
            for j in g[i]:
                if j!=p:
                    help(j,i)
            d[labels[i]]+=1
            arr[i]=d[labels[i]]-t
        

        d={}
        for i in labels:
            d[i]=0


        arr=[0]*n

        g=defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)
        

        help(0,-1)
        return arr

######################## BFS ##################
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        c = [0] * n
        v = set([0])

        g = {k: [] for k in range(n)}
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        self.collect(0, g, c, v, labels)
        return c

    def collect(self, k, g, c, v, labels):
        m = {}
        for p in g[k]:
            if p not in v:
                v.add(p)
                m1 = self.collect(p, g, c, v, labels)
                for (ch, cn) in m1.items():
                    m[ch] = (m[ch] if ch in m else 0) + cn

        m[labels[k]] = (m[labels[k]] if labels[k] in m else 0) + 1
        c[k] = m[labels[k]]

        return m