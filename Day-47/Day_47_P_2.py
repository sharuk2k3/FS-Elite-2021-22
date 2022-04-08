'''

Venkatadri is a maths teacher.
He is teaching matrices to his students.
He is given a matrix of size m*n, and it contains only positive numbers.
He has given a task to his students to find the special matrix, 
in the iven matrix A[m][n].
A special matrix has following property:
	- The sum of elements in each row, each column and the two diagonals are equal.
	- Every 1*1 matrix is called as a special matrix.
	- The size of the special matrix should be a square, i.e., P*P.

Your task is to help the students to find the speical matrix  with max size P.


Input Format:
-------------
Line-1: Two space separated integers M and N, size of the matrix.
Next M lines: N space separated integers m and n.

Output Format:
--------------
Print an integer, maximum size P of the special matrix.


Sample Input-1:
---------------
5 5
7 8 3 5 6
3 5 1 6 7
3 5 4 3 1
6 2 7 3 2
5 4 7 6 2

Sample Output-1:
----------------
3

Explanation:
------------
The special matrix is:
5 1 6
5 4 3
2 7 3


Sample Input-2:
---------------
4 4
7 8 3 5
3 2 1 6
3 2 3 3
6 2 3 3

Sample Output-2:
----------------
2

Explanation:
------------
The special matrix is:
3 3
3 3


'''
def SpecialMatrix(grid):
    m=len(grid)
    n=len(grid[0])
    
    # Row sum matrix
    rowPrefixSum=[[0]*(n+1) for r in range(m)]
    for r in range(m):
        for c in range(n):
            rowPrefixSum[r][c+1]=rowPrefixSum[r][c] + grid[r][c]
            
    #column sum Matrix        
    columnPrefixSum=[[0]*(m+1) for c in range(n)]
    for c in range(n):
        for r in range(m):
            columnPrefixSum[c][r+1]=columnPrefixSum[c][r] + grid[r][c]

    k=min(m,n)
    while 1<k:
        for r in range(m-k+1):
            for c in range(n-k+1):
                z=rowPrefixSum[r][c+k] - rowPrefixSum[r][c]
                ok=1
                for i in range(k):
                    if z!=rowPrefixSum[r+i][c+k]-rowPrefixSum[r+i][c] or z!=columnPrefixSum[c+i][r+k]-columnPrefixSum[c+i][r]:
                        ok=0
                        break
                if ok: 
                    # check both diagonals
                    diagZ1=0
                    diagZ2=0
                    for i in range(k):
                        diagZ1+=grid[r+i][c+i]
                        diagZ2+=grid[r+i][c+k-i-1]
                    if z==diagZ1==diagZ2: return k
        k-=1
    return 1
    
m, n = map(int, input().split())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))
print(SpecialMatrix(grid))