arr = [2,34,53,32,212,532]

def reverseArr(arr,i,j):
    if i>=j:
        return
    arr[i],arr[j] = arr[j],arr[i]
    reverseArr(arr,i+1,j-1)

print(arr)
reverseArr(arr,0,len(arr)-1)
print(arr)