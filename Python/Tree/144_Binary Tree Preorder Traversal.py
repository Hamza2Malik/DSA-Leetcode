////////////// iterative  ////////////////////////

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        stack = [root]
        
        while stack:
            curr_node = stack.pop()
            if curr_node:
                ans.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)
        return ans

//////////////////  Recursive //////////////

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res


////////////////// Moris Traversal ////////////////

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        
        curr = root
        
        while curr:
            if(curr.left == None):
                preorder.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                
                while last.right and last.right != curr:
                    last = last.right
                    
                    
                if(last.right == None):
                    preorder.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right
        return preorder
                    
