'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

#Solution:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag = True
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if j == 0 and matrix[i][j] == 0:
                    flag = False
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if j == 0:
                    if flag == False:
                        matrix[i][j] = 0
                    
                elif matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
