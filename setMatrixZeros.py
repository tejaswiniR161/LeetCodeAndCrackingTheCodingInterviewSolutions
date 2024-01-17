#CTCI question number 1.8
#LC question link - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows={}
        columns={}
        r=len(matrix)
        c=len(matrix[0])
        for i in range(0,r):
            for j in range(0,c):
                if(matrix[i][j]==0):
                    print(i,j)
                    columns[j]=0
                    rows[i]=0
        for i in range(0,r):
            for j in range(0,c):
                if i in rows:
                    matrix[i][j]=0
                if j in columns:
                    matrix[i][j]=0