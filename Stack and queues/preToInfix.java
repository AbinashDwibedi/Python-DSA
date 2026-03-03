// User function Template for Java
import java.util.Stack;
class Solution {
    static String preToInfix(String pre_exp) {
        Stack<String> st = new Stack<>();
        for(int i = pre_exp.length()-1; i>=0;i--){
            char ch = pre_exp.charAt(i);
            if ((ch>='a' && ch<='z') || (ch>='A' && ch <='Z') || (ch>='0' && ch<='9')){
                st.push(""+ch);
            }
            else{
                String a = st.pop();
                String b = st.pop();
                st.push("(" + a + ch + b + ")");
            }
        }
        return st.peek();
    }
}
