'''

A merchant has two types of idols, gold and silver.
He has arranged the idols in the form of m*n grid, 
	- the gold idols are represented as 1's 
	- the silver idols are represented as 0's.

Your task is to find the longest consecutive arrangement of gold idols, 
The arrangement can be either horizontal, vertical, diagonal or 
antidiagonal, but not the combination of these.


Input Format:
-------------
Line-1: Two space separated integers m and n, grid size.
Next m lines : n space separated integers, arrangement of idols.

Output Format:
--------------
Print an integer, longest arranement of gold idols.


Sample Input:
---------------
4 5
1 0 1 1 1
0 1 0 1 0
1 0 1 0 1
1 1 0 1 1

Sample Output:
----------------
4


'''

# Pure Vanilla DP Problem XD (Neil Sir) SOLUTION 

def longestGoldIdols(grid):
    if len(grid) == 0:
        return 0
        
    n = len(grid)
    m = len(grid[0])
    ans = 0
    
    dp = [[[0]*4 for i in range(0, m)] for j in range(0, n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            for k in range(4):
                dp[i][j][k] = 1
            if i - 1 >= 0:
                dp[i][j][0] += dp[i - 1][j][0]
            if j - 1 >= 0:
                dp[i][j][1] += dp[i][j - 1][1]
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j][2] += dp[i - 1][j - 1][2]
            if i - 1 >= 0 and j + 1 < m:
                dp[i][j][3] += dp[i - 1][j + 1][3]
            ans = max(ans, max(dp[i][j][0], dp[i][j][1]))
            ans = max(ans, max(dp[i][j][2], dp[i][j][3]))
            
    return ans
if __name__=="__main__":
    r,c=map(int,input().split())
    grid=[]
    for i in range(r):
        row=list(map(int,input().split()))
        grid.append(row)
    print(longestGoldIdols(grid))