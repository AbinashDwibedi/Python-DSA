class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # brute force 
        l = 0
        r = 0
        nums3 = []
        while l<len(nums1) and r <len(nums2):
            if nums1[l] <nums2[r]:
                nums3.append(nums1[l])
                l += 1
            else:
                nums3.append(nums2[r])
                r += 1
        while l < len(nums1):
            nums3.append(nums1[l])
            l += 1
        while r < len(nums2):
            nums3.append(nums2[r])
            r+=1
        
        n = len(nums3)
        if n % 2 == 0:
            return (nums3[n//2 -1]+nums3[n//2])/ 2
        return nums3[n//2]