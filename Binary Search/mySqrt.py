def mySqrt(x) :
        left = 0
        right = x
        ans = -1

        while left <= right :
            mid = (left+right) //2 
            
            if mid*mid > x:
                right = mid-1
            else:
                left = mid+1
                ans = max(ans,mid)
        return ans