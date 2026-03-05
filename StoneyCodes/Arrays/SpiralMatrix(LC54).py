class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m=len(matrix)
        n=len(matrix[0])
        colStart,colEnd=0,n-1
        rowStart,rowEnd=0,m-1
        while len(res)<=m*n:
            for i in range(colStart,colEnd+1):
                res.append(matrix[rowStart][i])
            rowStart+=1

            if len(res)==m*n:
                break
            
            for i in range(rowStart,rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd-=1

            if len(res)==m*n:
                break

            for i in range(colEnd,colStart-1,-1):
                res.append(matrix[rowEnd][i])
            rowEnd-=1

            if len(res)==m*n:
                break

            for i in range(rowEnd,rowStart-1,-1):
                res.append(matrix[i][colStart])
            colStart+=1

        return res



