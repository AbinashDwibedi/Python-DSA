class Solution {
    public int celebrity(int mat[][]) {
        int n = mat.length;
        int[] knowMe = new int[n];
        int[] iKnow = new int[n];
        for(int i = 0;i<n;i++){
            for(int j =0;j<n;j++){
                if(i==j) continue;
                if(mat[i][j] == 1){
                    knowMe[j]++;
                    iKnow[i]++;
                }
            }
        }
        for(int i = 0;i<n;i++){
            if(knowMe[i] == n-1 && iKnow[i] == 0){
                return i;
            }
        }
        return -1;
    }
}