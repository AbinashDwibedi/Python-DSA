def minimumPairRemoval(nums):
        def is_non_decreasing(arr):
            for i in range(1,len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        
        count = 0
        
        while not is_non_decreasing(nums):   
            idx = 0
            minSum = float("inf")
            count +=1
            for i in range(len(nums)-1):
                s = nums[i]+nums[i+1]
                if s < minSum:
                    minSum = s
                    idx = i
            nums = nums[:idx]+[minSum] + nums[idx+2:]
        return count