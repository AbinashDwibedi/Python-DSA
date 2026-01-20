arr = [34, 7, 23, 32, 5, 62, 3, 18]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        miniIdx = i
        for j in range(i+1,n):
            if arr[miniIdx] > arr[j]:
                miniIdx = j
        arr[i],arr[miniIdx] = arr[miniIdx],arr[i]
    return arr
print(selectionSort(arr))