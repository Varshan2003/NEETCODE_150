class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(numRows-1):
            row = []
            for j in range(1,len(res[-1])):
                row.append(res[-1][j]+res[-1][j-1])
            row.insert(0,1)
            row.append(1)
            res.append(row)
        return res
