class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m, n = len(matrix), len(matrix[0])
        result = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            result.append(row)

        return result

        