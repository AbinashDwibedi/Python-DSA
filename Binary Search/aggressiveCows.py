def aggressiveCows(stalls, k):
        stalls.sort()
        n = len(stalls)
        left = 1
        right = stalls[n-1]-stalls[0]
        maxi = left
        def possible(minD):
            count = 1
            prev = stalls[0]
            for i in range(1,n):
                if (stalls[i] - prev) >= minD:
                    count += 1
                    prev = stalls[i]
                    if count == k:
                        return True
            return False
        while left <= right:
            mid = (left+right) // 2
            if possible(mid):
                maxi = mid
                left = mid+1
            else:
                right = mid-1
        
        return maxi