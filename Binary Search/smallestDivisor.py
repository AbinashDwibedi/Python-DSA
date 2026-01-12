def smallestDivisor(nums , threshold) :
        left = 1
        right = max(nums)
        mini = float("inf")

        while left <= right :
            mid = (left+right) // 2
            temp = 0
            for num in nums:
                temp += (num+mid-1)//mid
            if temp > threshold:
                left = mid+1
            else:
                mini = mid
                right = mid-1
        return mini