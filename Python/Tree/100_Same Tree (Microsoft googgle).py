#################### DFS ###################

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        def dfs(p,q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            
            if(q.val != p.val):
                return False
            ans = dfs(p.left, q.left) and dfs(p.right, q.right)    
            
            
            return ans
        
        return dfs(p,q)






################## BFS ############################
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False           
            if(q.val != p.val):
                return False
            return True
        
        deq = deque([(p,q),])
        
        while deq:
            pp, qq = deq.popleft()
            if not dfs(pp, qq):
                return False
            if pp:
                deq.append((pp.left, qq.left))
                deq.append((pp.right, qq.right))
        
        return True
         