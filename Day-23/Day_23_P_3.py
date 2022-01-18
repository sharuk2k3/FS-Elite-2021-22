'''

The decoration on the wall, made up of led bulbs. 
When the bulbs turned on they emit either bule color light
or white color light. The leds bulbs decorated in the form of a grid
of size m*n. And when you turned on the bulbs, the bulbs are emiting
the light in blue color (1) and white color (0).

You are given the current state of the decorated wall of size M*N,
Your task is to find the biggest square can be formed using blue colored bulbs,
and return its area.

Input Format:
-------------
Line-1: Two space separated integers, M and N size of the decoration grid.
Next M lines: N space separated integers ( either 0 or 1 only).

Output Format:
--------------
Print an integer, area of the biggest square grid of blue colored bulbs.


Sample Input:
-------------
5 6
1 0 0 1 0 1
0 1 1 1 1 1
1 1 1 1 0 1
0 1 1 1 0 1
1 0 1 0 1 1 

Sample Output:
--------------
9


'''

#SOLUTION

def Square(matrix):
    if len(matrix) == 0:
        return 0
        
    m , n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]   
    maxLength = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                maxLength = max(maxLength, dp[i][j])
        
    return maxLength**2
    
M,N=map(int,input().split())
matrix=[]
for i in range(M):
    row=list(map(str,input().split()))
    matrix.append(row)
print(Square(matrix))
