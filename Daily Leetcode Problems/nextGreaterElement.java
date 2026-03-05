// class Solution {
//     public int[] nextGreaterElement(int[] nums1, int[] nums2) {
//         int m = nums1.length;
//         int n = nums2.length;
//         int[] result = new int[m];
//         for (int i = 0;i<m;i++){
//             int idx = -1;
//             for (int j = 0; j<n;j++){
//                 if (nums1[i]==nums2[j]){
//                     idx = j;
//                     break;
//                 }
//             }

//             result[i] = -1;
//             for (int j = idx+1;j<n;j++){
//                 if (nums1[i]<nums2[j]){
//                     result[i] = nums2[j];
//                     break;
//                 }
//             }
//         }
//         return result;
//     }
// }

//monotonic stack solution
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        Stack<Integer> st = new Stack<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[m];
        for (int i = n-1;i>=0;i--){
            
            while(!st.isEmpty() && nums2[i]> st.peek()){
                st.pop();
            }
            if (st.isEmpty()){
                map.put(nums2[i],-1);
            }
            else{
                map.put(nums2[i],st.peek());
            }
            st.push(nums2[i]);
        }
        
        for(int i = 0;i<m;i++){
            result[i] = map.get(nums1[i]);
        }
        return result;

    }
}