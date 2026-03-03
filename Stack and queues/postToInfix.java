// User function Template for Java
import java.util.Stack;
class Solution {
    static String postToInfix(String exp) {
        Stack<String> st = new Stack<>();
        for(int i = 0;i<exp.length();i++){
            char ch = exp.charAt(i);
            if ((ch >= 'A' && ch <= 'Z') || (ch>='a' && ch<='z') || (ch>='0' && ch>='9')){
                st.push(""+ch);
            }
            else{
                String a = st.pop();
                String b = st.pop();
                String newStr = "(" + b + ch + a + ")";
                st.push(newStr);
            }
        }
        return st.peek();
    }
}
