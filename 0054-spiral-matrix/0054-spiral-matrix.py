class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = matrix
        T = 0
        B = len(matrix)

        L = 0
        R = len(matrix[0])

        ans = []
        while T < B and L < R:
            for i in range(L, R):
                ans.append(nums[T][i])
            T += 1
            for i in range(T, B):
                ans.append(nums[i][R - 1])
            R -= 1

            if T >= B or L >= R:
                break

            for i in range(R - 1, L - 1, - 1):
                ans.append(nums[B - 1][i])
            
            B -= 1

            for i in range(B - 1, T - 1, -1):
                ans.append(nums[i][L])
            
            L += 1
        return ans
        