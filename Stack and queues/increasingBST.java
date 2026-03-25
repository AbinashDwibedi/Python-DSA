/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    TreeNode tail;
    public TreeNode increasingBST(TreeNode root) {
        TreeNode dummy = new TreeNode(0);
        tail = dummy;
        inorder(root);
        return dummy.right;
    }
    private void inorder(TreeNode root){
        if(root == null) return; 
        inorder(root.left);
        tail.right = new TreeNode(root.val);
        tail = tail.right;
        inorder(root.right);
    }
}