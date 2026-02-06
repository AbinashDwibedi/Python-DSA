def subarraysWithSumK(arr,k):
    prefix = 0
    mp = {0:[-1]}
    result = []
    for i,num in enumerate(arr):
        prefix += num
        if prefix -k in mp:
            for j in mp[prefix-k]:
                result.append(arr[j+1:i+1])
        
        if prefix not in mp:
            mp[prefix] = []
        mp[prefix].append(i)
    return result

print(subarraysWithSumK([1,2,3],3))