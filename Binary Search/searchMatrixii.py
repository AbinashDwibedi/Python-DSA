class Solution:
    def searchMatrix(self, matrix, target) :
        # brute force
        # m = len(matrix)
        # n = len(matrix[0])

        # def bs(arr,target):
        #     l = 0
        #     r = len(arr)-1
        #     while l <= r:
        #         mid = (l+r)//2
        #         if arr[mid] == target:
        #             return True
        #         elif arr[mid] > target:
        #             r = mid-1
        #         else:
        #             l = mid+1
        #     return False

        # for i in range(m):
        #     if bs(matrix[i],target):
        #         return True
        # return False

        l,r = 0, (len(matrix[0])-1)
        while l < len(matrix) and (r >= 0):
            if matrix[l][r] == target :
                return True
            elif matrix[l][r] > target :
                r -= 1
            else:
                l += 1
        return False