// User function Template for Java
import java.util.Stack;
class Solution {
    static String preToPost(String pre_exp) {
        Stack<String> st = new Stack<>();
        int n = pre_exp.length();
        for(int i=n-1;i>=0;i--){
            char ch = pre_exp.charAt(i);
            if ((ch>='a' && ch<='z') || (ch>='A'&& ch<='Z') || (ch>='0' && ch<='9')){
                st.push(""+ch);
            }
            else{
                String a = st.pop();
                String b = st.pop();
                st.push(a+b+ch);
            }
        }
        return st.peek();
    }
}
