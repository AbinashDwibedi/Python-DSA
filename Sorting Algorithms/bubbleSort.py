arr = [34, 7, 23, 32, 5, 62, 3, 18]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr

print(selectionSort(arr))