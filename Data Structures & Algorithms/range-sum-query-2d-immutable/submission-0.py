class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.precomp = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                if r == 0:
                    self.precomp[r][c] = prefix
                else:
                    self.precomp[r][c] = prefix + self.precomp[r-1][c]

        
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = 0 if col1 == 0 else self.precomp[row2][col1-1]
        up = 0 if row1 == 0 else self.precomp[row1-1][col2] 
        inex = 0 if row1 == 0 or col1 == 0 else self.precomp[row1-1][col1-1]
        return self.precomp[row2][col2] - up - left + inex
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)