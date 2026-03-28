class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> st = new Stack<>();
        int sum = 0;

        for (String s : operations) {
            if (s.equals("D")) {
                int val = 2 * st.peek();
                st.push(val);
                sum += val;
            } 
            else if (s.equals("C")) {
                sum -= st.pop();
            } 
            else if (s.equals("+")) {
                int a = st.pop();
                int b = st.peek();
                st.push(a);

                int val = a + b;
                st.push(val);
                sum += val;
            } 
            else {
                int val = Integer.parseInt(s);
                st.push(val);
                sum += val;
            }
        }

        return sum;
    }
}