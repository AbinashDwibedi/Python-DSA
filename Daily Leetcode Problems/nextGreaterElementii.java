class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Stack<Integer> st = new Stack<>();

        for(int i = 2*n - 1; i>=0 ;i--){
            int num = nums[i%n];
            while (!st.isEmpty() && num >= st.peek()){
                st.pop();
            }

            if (i<n){
                result[i] = st.isEmpty()? -1 : st.peek();
            }

            st.push(num);
        }
        return result;
    }
}