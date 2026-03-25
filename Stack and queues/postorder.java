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
}
*/
import java.util.*;
// class Solution {
//     public List<Integer> postorder(Node root) {
//         List<Integer> list = new ArrayList<>();
//         poHelper(root,list);
//         return list;
//     }
//     private static void poHelper(Node root , List<Integer> list){
//         if (root == null) return ;
//         for(Node child:root.children){
//             poHelper(child,list);
//         }
//         list.addLast(root.val);
//     }
// }

// Iterative solution 

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
}
*/

class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> list= new LinkedList<>();
        if (root == null) return list;
        Stack<Node> st = new Stack<>();
        st.push(root);
        while (!st.isEmpty()){
            Node temp = st.pop();
            list.addFirst(temp.val);
            for(Node child:temp.children){
                if(child!=null) st.push(child);
            }
        }
        return list;
    }

}