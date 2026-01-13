def findKthPositive(arr, k) :
        ans = arr[0] - 1
        if ans >= k:
            return k
        k -= ans
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] > 1:
                temp = arr[i] - arr[i-1] -1
                if temp > k:
                    return arr[i-1] + k
                elif temp < k:
                    k -= temp
                else:
                    return arr[i]-1
        return arr[len(arr)-1] + k