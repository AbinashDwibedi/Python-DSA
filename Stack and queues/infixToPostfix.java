import java.util.Stack;

class Solution {
    public static int precedence(char ch){
        if (ch == '-' || ch == '+') return 1;
        else if (ch == '*' || ch == '/') return 2;
        else if (ch == '^') return 3;
        else return -1;
    }
    public static String infixToPostfix(String s) {
        String ans = new String("");
        Stack<Character> st = new Stack<>();
        
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch>='0' && ch<='9')){
                ans+=ch;
            }
            else if(ch == '('){
                st.push(ch);
            }
            else if(ch == ')'){
                while (!st.empty() && st.peek() != '('){
                    ans += st.pop();
                }
                st.pop();
            }
            else{
                while (!st.empty() && (precedence(ch) < precedence(st.peek())||((precedence(st.peek())==precedence(ch)) && ch != '^'))){
                    ans += st.pop();
                }
                st.push(ch);
            }
        }
        while (!st.empty()){
            ans += st.pop();
        }
        return ans;
    }
}