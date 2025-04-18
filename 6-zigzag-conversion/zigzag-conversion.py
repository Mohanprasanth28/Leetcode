class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        i = 0
        d = 1

        row = [[] for _ in range(numRows)]

        for ch in s:
            row[i].append(ch)
            if i == 0:
                d = 1
            elif i == numRows -1:
                d = -1
            i += d

        res = ""
        for i in range(numRows):
            res += ''.join(row[i])

        return res
        