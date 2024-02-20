class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def fun(i,j):
            for k in range(len(matrix)):
                matrix[k][j]=0
            for k in range(len(matrix[0])):
                matrix[i][k]=0
        set1=set()   
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    set1.add((i,j))

        for i,j in set1:
            fun(i,j)
            

            
        
