'''


You will be given the matrix of size R*C,

You have to return the matrix in special order as shown in the sample tescases.
 

Input Format:
-------------
Line-1 -> Two integers R and C, size of matrix.
Next R-Lines -> C space separated integers

Output Format:
--------------
Print R-Lines -> C space separated integers, in special order.


Sample Input-1:
---------------
3 3
1 2 3
4 5 6
7 8 9

Sample Output-1:
----------------
1 2 3
6 9 8
7 4 5


Sample Input-2:
---------------
3 4
1 2 3 4
5 6 7 8
9 10 11 12

Sample Output-2:
----------------
1 2 3 4
8 12 11 10
9 5 6 7





'''

def spiralMat(matrix):
    res = []
    while matrix:
            # first row
        res.extend(matrix.pop(0))
        if not matrix:
            break
            # last column
        res.extend(row.pop() for row in matrix if row)
        if not matrix:
                break
            # last row (reverse order)
        res.extend(matrix.pop()[::-1])
        if not matrix:
            break
            # first column (reverse order)
        res.extend(row.pop(0) for row in matrix[::-1]
                    if row)
    return res


r,c=map(int,input().split())
matrix=[]
for i in range(r):
    matrix.append(list(map(int,input().split())))
print(*spiralMat(matrix))
