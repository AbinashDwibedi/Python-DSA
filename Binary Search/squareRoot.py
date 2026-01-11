def squareRoot(n, p):
        left = 0
        right = n
        ans = -1
        while left <= right :
            mid = (left + right)//2
            
            if mid*mid > n:
                right = mid-1
            else:
                left = mid+1
                ans = mid
        # floating part
        result = float(ans)
        increment = 0.1
        
        for _ in range(p):
            
            while (result+increment)*(result+increment) <= n:
                result+= increment
            increment/=10
        return round(result,p)
        