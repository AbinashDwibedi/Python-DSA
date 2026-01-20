# arr = [34, 7, 23, 32, 5, 62, 3, 18]
arr = arr = [4, 2, 5, 2, 3, 2]
# len(arr) will give me 8 now if i divide it with 2 it will give me 4 which is element 5

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    leftMerge = mergeSort(leftArr)
    rightMerge = mergeSort(rightArr)

    return merge(leftMerge,rightMerge)

def merge(lArr,rArr):
    m = len(lArr)
    n = len(rArr)
    result = []

    l = 0
    r = 0

    while l<m and r<n:
        if lArr[l] < rArr[r]:
            result.append(lArr[l])
            l+=1
        else:
            result.append(rArr[r])
            r+=1

    result.extend(lArr[l:])
    result.extend(rArr[r:])
    return result

print(mergeSort(arr))
