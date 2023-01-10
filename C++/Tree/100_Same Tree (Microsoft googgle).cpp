//////////////////////// DFS ////////////////

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p==NULL && q==NULL){
            return true;
        }
        if(p==NULL or q==NULL){
            return false;
        }
        
        if(p->val != q->val){
            return false;
        }
        
        return isSameTree(p->left, q->left) && isSameTree(p->right,q->right);
    }
};



/////////////////////// BFS //////////////////

class Solution {
public:
    
     bool isSame(TreeNode* p, TreeNode* q){
          if(p==NULL && q==NULL){
            return true;
        }
        if(p==NULL or q==NULL){
            return false;
        }
        
        if(p->val != q->val){
            return false;
        }
         return true;
     }
    
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> qp;
        queue<TreeNode*> qq;
        
        qp.push(p);
        qq.push(q);
        
        while(!qp.empty() && !qq.empty()){
            TreeNode* node1 = qp.front();
            qp.pop();
            TreeNode* node2 = qq.front();
            qq.pop();
            
            if(!isSame(node1, node2)){
                return false;
            }
            
            if(node1 != NULL){
                qp.push(node1->left);
                qq.push(node2->left);
                qp.push(node1->right);
                qq.push(node2->right);
            }
            
        }
        
        return true;

        
            }
};