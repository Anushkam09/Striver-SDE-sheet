#calculate row (LC 119)
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = []
        ans = 1
        row.append(ans)
        for i in range(1,rowIndex+1):
            ans = ans*(rowIndex-i+1)//i
            row.append(ans)
        return row


#find triangle (LC 118)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        final = []
        for rowIndex in range(numRows):
            row = []
            ans = 1
            row.append(ans)
            for i in range(1,rowIndex+1):
                ans = ans*(rowIndex-i+1)//i
                row.append(ans)
            final.append(row)
        return final