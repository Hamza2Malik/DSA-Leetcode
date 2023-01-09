/////////////////// Recursive /////////////////

class Solution {
public:
    vector<int> ans;
    vector<int> preorderTraversal(TreeNode* root) {
        if(root != NULL){
            ans.push_back(root->val);
            preorderTraversal(root->left);
            preorderTraversal(root->right);
        }
        return ans;
    }
};

/////////////////// iteravtive ///////////////////

class Solution {
public:

    vector<int> preorderTraversal(TreeNode* root) {
      vector<int> ans;
      stack<TreeNode*> st;
        st.push(root);
        
        while(!st.empty()){
            TreeNode* temp = st.top();
            st.pop();
            if(temp != nullptr){
                ans.push_back(temp->val);
                st.push(temp->right);
                st.push(temp->left);
            }
            
        }
        
        return ans;
    }
};


///////////////////////////// Moris Traversal //////////////////////////

class Solution {
public:

    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> preorder;
        
        TreeNode* curr = root;
        while(curr != nullptr){
            if(curr->left == nullptr){
                preorder.push_back(curr->val);
                curr = curr->right;
            }
            else{
                TreeNode* prev = curr->left;
                while(prev->right && prev->right != curr){
                    prev = prev->right;
                }
                
                if(prev->right == nullptr){
                    prev ->right = curr;
                    preorder.push_back(curr->val);
                    curr = curr->left;
                }
                else{
                    prev->right = nullptr;
                    curr = curr->right;
                }
    
            }
 
        }
        return preorder;
          
    }
};