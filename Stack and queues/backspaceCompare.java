class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> s1 = new Stack<>();
        Stack<Character> s2 = new Stack<>();
        int i = 0;
        while(i!=s.length()){
            if(s.charAt(i) == '#'){
                if(!s1.isEmpty()) s1.pop();
            }
            else{
                s1.push(s.charAt(i));
            }
            i++;
        }
        i = 0;
        while(i!=t.length()){
            if(t.charAt(i) == '#'){
                if(!s2.isEmpty()) s2.pop();
            }
            else{
                s2.push(t.charAt(i));
            }
            i++;
        }
        while(!s1.isEmpty() && !s2.isEmpty()){
            if (s1.pop()!=s2.pop()){
                return false;
            }
        }
        return s1.isEmpty() && s2.isEmpty();
    }
}