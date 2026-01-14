def splitArray(nums, k) :
        left = max(nums)
        right = sum(nums)
        mini = -1

        def possible(mid):
            count = 1
            summ = 0
            for num in nums:
                if (summ+num) <= mid:
                    summ+=num
                else:
                    summ = num
                    count += 1
                    if count > k :
                        return False
            return True

        while left <= right:
            mid = (left+right) //2
            if possible(mid):
                mini = mid
                right = mid-1
            else:
                left = mid+1
        return mini