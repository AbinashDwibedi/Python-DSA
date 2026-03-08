class Solution {
    public int trap(int[] height) {
        // int n = height.length;

        // int[] leftMax = prefixMax(height);
        // int[] rightMax = suffixMax(height);

        // int water = 0;

        // for(int i = 0; i < n; i++){
        //     water += Math.min(leftMax[i], rightMax[i]) - height[i];
        // }

        // return water;

        int left = 0;
        int right = height.length-1;
        int leftMax = height[left];
        int rightMax = height[right];
        int result = 0;

        while(left < right) {
            if (leftMax < rightMax){
                left ++;
                leftMax = Math.max(leftMax, height[left]);
                result += leftMax - height[left];
            }
            else{
                right --;
                rightMax = Math.max(rightMax,height[right]);
                result += rightMax - height[right];
            }
        }
        return result;
    }

    // public static int[] prefixMax(int[] h){
    //     int[] pm = new int[h.length];
    //     pm[0] = h[0];

    //     for(int i = 1; i < h.length; i++){
    //         pm[i] = Math.max(pm[i-1], h[i]);
    //     }

    //     return pm;
    // }

    // public static int[] suffixMax(int[] h){
    //     int n = h.length;
    //     int[] sm = new int[n];
    //     sm[n-1] = h[n-1];

    //     for(int i = n-2; i >= 0; i--){
    //         sm[i] = Math.max(sm[i+1], h[i]);
    //     }

    //     return sm;
    // }
}