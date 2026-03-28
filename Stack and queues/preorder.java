/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        // Stack<Integer> st = new Stack<>();
        
        List<Integer> list = new ArrayList<>();
        poHelper(root,list);
        return list;
    }
    private static void poHelper(Node root,List<Integer> list){
        if(root == null) return;
        list.addLast(root.val);
        for(Node child: root.children){
            poHelper(child,list);
        }
    }
}