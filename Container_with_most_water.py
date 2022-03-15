#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

#Example:
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: 
#The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#Code:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 #start point
        j = len(height) - 1 #endpoint
        area1 = 0
        
        while (i < j):
            area = (j - i)*(min(height[j],height[i]))
            area1 = max(area1, area)
            
            if height[i] <= height[j]:
                i = i + 1
            else:
                j = j - 1
                
        return area1
            
