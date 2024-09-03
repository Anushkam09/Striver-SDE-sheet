#Brute force approach
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        def markrow(row):
            for i in range(len(matrix[row])):  
                if matrix[row][i] != 0:
                    matrix[row][i] = "a"

        def markcol(col):
            for i in range(len(matrix)):  
                if matrix[i][col] != 0:
                    matrix[i][col] = "a"

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    markrow(i)
                    markcol(j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0

        print(matrix)

#Better approach
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)  #rows
        m = len(matrix[0]) #cols
        rows = ["a"]*n
        cols = ["a"]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    #i: row, j:col
                    rows[i] = "b"
                    cols[j] = "b"
        for i in range(n):
            for j in range(m):
                if rows[i] == "b" or cols[j] =="b":
                    matrix[i][j] = 0

#Optimal approach
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)  #rows
        m = len(matrix[0]) #cols
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    #i: row, j:col
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0= 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] != 0:
                    if matrix[i][0]  ==0 or  matrix[0][j]==0:
                        matrix[i][j] = 0
        
        if matrix[0][0]== 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

               