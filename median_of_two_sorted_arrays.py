#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).

#code:

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        numList = nums1 + nums2
        numList.sort()
        l = int(len(numList)/2)
        
        if len(numList)%2 == 0:
            median = (numList[l - 1] + numList[l])/2
            
        else:
            median = numList[l]
        
        return median
        
