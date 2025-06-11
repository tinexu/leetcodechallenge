class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowZeroes = []
        colZeroes = []
        numRows = len(matrix)
        numCols = len(matrix[0])
        for i in range(numRows):
            addedRow = False
            for j in range(numCols):
                if matrix[i][j] == 0:
                    if not addedRow:
                        rowZeroes.append(i)
                        addedRow = True
                    colZes.append(j)
        for row in rowZeroes:
            for i in range(numCols):
                matrix[row][i] = 0
        for col in colZeroes:
            for i in range(numRows):
                matrix[i][col] = 0
        

        
