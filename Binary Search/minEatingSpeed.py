def minEatingSpeed(piles, h) :
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left+right)//2
            temp = 0
            for pile in piles:
                temp += (pile+mid-1)//mid
            if temp <= h:
                ans = mid
                right = mid-1
                
            else:
                left = mid+1
                
        return ans