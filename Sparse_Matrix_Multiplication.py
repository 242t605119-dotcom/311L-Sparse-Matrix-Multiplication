class Solution:
    def multiply(self, mat1, mat2):
        m = len(mat1)
        n = len(mat2[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for k in range(len(mat2)):
                if mat1[i][k] != 0:
                    for j in range(n):
                        if mat2[k][j] != 0:
                            result[i][j] += mat1[i][k] * mat2[k][j]

        return result
