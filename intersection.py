class Solution:
    def intersection(self, nums1, nums2) :
        # set1 = set(nums1)
        # set2 = set(nums2)

        # set3 = set1.intersection(set2)
        # return list(set3)

        # Two pointer approach
        nums1.sort()
        nums2.sort()
        result = set()
        i,j = 0,0
        while i < len(nums1) and j<len(nums2):
            if  nums1[i] == nums2[j]:
                result.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return list(result)
