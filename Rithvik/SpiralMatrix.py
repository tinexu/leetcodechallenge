class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        nums = []
        numCols = len(matrix[0])
        numRows = len(matrix)
        currRow = 0
        currCol = 0
        numSquares = numRows * numCols
        visited = set()
        while True:
            while currCol != numCols and (currRow, currCol) not in visited:
                visited.add((currRow, currCol))
                nums.append(matrix[currRow][currCol])
                currCol += 1
            if len(visited) >= numSquares:
                break
            currCol -= 1
            currRow += 1
            while currRow != numRows and (currRow, currCol) not in visited:
                visited.add((currRow, currCol))
                nums.append(matrix[currRow][currCol])
                currRow += 1
            if len(visited) >= numSquares:
                break
            currRow -= 1
            currCol -= 1
            while currCol != -1 and (currRow, currCol) not in visited:
                visited.add((currRow, currCol))
                nums.append(matrix[currRow][currCol])
                currCol -= 1
            if len(visited) >= numSquares:
                break
            currCol += 1
            currRow -= 1
            while currRow != -1 and (currRow, currCol) not in visited:
                visited.add((currRow, currCol))
                nums.append(matrix[currRow][currCol])
                currRow -= 1
            if len(visited) >= numSquares:
                break
            currRow += 1
            currCol += 1
        return nums



                

        
