// User function Template for Java
import java.util.Stack;
class Solution {
    static String postToPre(String post_exp) {
        Stack<String> st = new Stack<>();
        
        for(int i = 0;i<post_exp.length();i++){
            char ch = post_exp.charAt(i);
            if ((ch>='A' && ch<='Z') || (ch>='a' && ch<='z') || (ch>='0' && ch<='9')){
                st.push(""+ch);
            }
            else{
                String a = st.pop();
                String b = st.pop();
                st.push(""+ch+b+a);
            }
        }
        return st.peek();
    }
}
