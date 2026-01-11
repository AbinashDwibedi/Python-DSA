def nthRoot(n, m):
        left = 0
        right = m
        while left<=right:
            mid = (left+right)//2
            temp = 1
            for _ in range(n):
                temp *= mid
                if temp > m:
                    break
            if temp == m:
                return mid
            elif temp > m:
                right = mid-1
            else:
                left = mid+1
        return -1