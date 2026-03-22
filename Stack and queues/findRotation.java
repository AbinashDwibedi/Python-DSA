class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;
        for(int i = 0;i<4;i++){
            if(compare(mat,target,n)){
                return true;
            }
            rotate(mat,n);
        }
        return false;
    }
    public static void rotate(int[][] mat,int n){
        for(int i = 0;i<n;i++){
            for(int j = i+1;j<n;j++){
                int temp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = temp;
            }
        }
        for(int i = 0;i<n;i++){
            for(int j =0; j<n/2 ;j++){
                int temp = mat[i][j];
                mat[i][j] = mat[i][n-j-1];
                mat[i][n-j-1] = temp;
            }
        }
    }
    public static boolean compare(int[][] mat1,int[][] mat2,int n){
        for(int i = 0;i<n;i++){
            for(int j =0;j<n;j++){
                if(mat1[i][j] != mat2[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
}