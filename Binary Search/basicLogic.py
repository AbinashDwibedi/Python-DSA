nums = [-1,0,3,5,9,12]
target = 9
def bs(nums,target,left,right):
    if left> right :
        return -1
    mid = (left+right)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return bs(nums,target,left,mid-1)
    else:
        return bs(nums,target,mid+1 , right)
    
print(bs(nums,target,0,len(nums)-1))

#output 4