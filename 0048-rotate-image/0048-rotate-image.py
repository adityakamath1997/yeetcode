class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = 0
        bot = n - 1

        while top < bot:
            for col in range(n):
                matrix[top][col], matrix[bot][col] = matrix[bot][col], matrix[top][col]
            top += 1
            bot -= 1
        
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        return matrix
        