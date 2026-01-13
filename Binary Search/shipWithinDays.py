# sumArr = []
        # acc = 0
        # for weight in weights:
        #     sumArr.append(acc+weight)
        #     acc += weight
        # left = 0
        # n= len(sumArr)
        # right = n-1
        # mini = right
        # while left <= right:
        #     mid = (left+right)//2
        #     if sumArr[mid]*days >= sumArr[n-1]:
        #         mini = mid
        #         right = mid-1
        #     else:
        #         left = mid+1
        # return mini

def shipWithinDays(weights, days):
        # left = max(weights)
        # right = sum(weights)
        left = float("-inf")
        right = 0
        for wt in weights:
            left = max(left,wt)
            right += wt
        mini = right
        while left <= right:
            mid = (left+right)//2

            if possible(weights,days,mid):
                mini = mid
                right = mid -1
            else:
                left = mid+1
        return mini
        
def possible(self,weights,days,capacity):
        day = 1
        val = 0
        for wt in weights:
            if (val+wt) <= capacity:
                val+=wt
            else:
                day +=1
                val = wt
                if day > days:
                    return False
        return True

        