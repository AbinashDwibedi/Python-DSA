import java.util.*;
class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> st = new Stack<>();
        for (int i = 0;i<num.length();i++){
            while(!st.isEmpty() && k>0 && (st.peek() - '0') >  (num.charAt(i) - '0')){
                st.pop();
                k = k-1;
            }
            st.push(num.charAt(i));
        }
        while (k>0 && !st.isEmpty()){
            st.pop();
            k--;
        }
        if (st.isEmpty()) return "0";
        StringBuilder result = new StringBuilder();
        while(!st.empty()){
            result.append(st.pop());
        }
        result.reverse();
        while(result.length() >0 && result.charAt(0) == '0'){
            result.deleteCharAt(0);
        }

        if (result.length()==0) return "0";
        return result.toString();
    }
}