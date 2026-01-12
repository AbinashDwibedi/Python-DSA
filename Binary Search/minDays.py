def minDays(bloomDay, m, k):
        n = len(bloomDay)
        if m*k > n:
            return -1
        def possible(day):
            count = 0
            tot = 0
            for num in bloomDay:
                if num<=day:
                    count +=1
                else:
                    tot += count//k
                    count = 0
            tot+= count//k
            if tot >= m:
                return True
            else:
                return False
        
        left = min(bloomDay)
        right = max(bloomDay)
        minDay = right

        while left <= right:
            mid = (left+right)//2

            if possible(mid):
                minDay = mid
                right = mid-1
            else:
                left = mid +1
        return minDay