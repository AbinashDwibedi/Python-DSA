class Solution {
    public static ArrayList<Integer> prevSmaller(int[] arr) {
        // code here
        int n = arr.length;
        Stack<Integer> st = new Stack<>();
        ArrayList<Integer> result = new ArrayList<>();
        for(int i = 0 ;i<n;i++){
            
            while(!st.isEmpty() && st.peek() >= arr[i]){
                st.pop();
            }
            
            result.add(!st.isEmpty()? st.peek():-1);
            
            st.push(arr[i]);
        }
        return result;
    }
}