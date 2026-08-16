/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        TreeNode* curr = root;

        while (curr) {
            if (curr->left == NULL) {
                res.push_back(curr->val);
                curr = curr -> right;
            } else {
                // Find the inorder predecessor
                TreeNode* IP = curr->left;
                while (IP->right && IP->right != curr) {
                    IP = IP->right;
                }

                if (IP->right == NULL) {
                    IP->right = curr;
                    curr = curr->left;
                } else {
                    IP->right = NULL;
                    res.push_back(curr->val);
                    curr = curr->right;
                }
            }
        }

        return res;
    }
};