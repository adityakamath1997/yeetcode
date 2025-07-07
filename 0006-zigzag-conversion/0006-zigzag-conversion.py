class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = []
        for row in range(numRows):
            rows.append(list())

        idx = 0
        d = 1
        for c in s:
            rows[idx].append(c)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1

            idx += d
    
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        ans = ''.join(rows)
        return ans
