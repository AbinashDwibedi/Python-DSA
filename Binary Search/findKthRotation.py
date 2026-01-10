def findKRotation(arr):
        left = 0
        right = len(arr)-1
        min = [float("inf"),-1]
        while left<= right:
            mid = (left+right)//2
            if arr[left] <= arr[mid]:
                if arr[left] <= min[0]:
                    min[0]=arr[left]
                    min[1]= left
                left = mid+1
            else:
                if arr[mid]<=min[0]:
                    min[0] = arr[mid]
                    min[1] = mid
                right = mid-1
        return min[1]