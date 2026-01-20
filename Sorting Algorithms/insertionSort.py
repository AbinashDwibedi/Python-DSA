arr = [34, 7, 23, 32, 5, 62, 3, 18]

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
    return arr

print(insertionSort(arr))
