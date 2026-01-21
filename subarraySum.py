# Only for posive integers 
#  n = len(nums)
#         count = 0
#         summ = 0
#         l = 0
#         for r in range(n):
#             summ += nums[r]
#             while summ > k:
#                 summ -= nums[l]
#                 l+=1
#             if summ == k:
#                 count +=1
            
            
#         return count

# For both positive and negative integers 
def subarraySum(nums, k) :
            n = len(nums)
            counts = {0:1}
            prefix = 0
            result = 0
            i = 0
            while i<n:
                prefix += nums[i]
                if prefix -k in counts:
                    result += counts[prefix-k]
                counts[prefix] = counts.get(prefix,0)+1
                i+=1
            return result
