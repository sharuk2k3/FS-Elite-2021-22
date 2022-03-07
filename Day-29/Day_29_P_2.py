'''

The Kolar Gold Fields (KGF) is in the form of a m*n grid,
Each field, contains some amount of Gold in it.
 
You can mine the gold in the KGF in the following way.
	- You can start at any position in the grid, never visit a cell with no gold.
	- each time you visit a cell, you will grab all the gold in it.
	- You can move one step to the left, right, up or down.
	- You can't visit the same cell more than once.
	- You can stop at any cell.
	
Your task is to find the maximum amount of gold you can collect.

Input Format:
-------------
Line-1: Two integers M and N size of the KGF grid.
Next M lines: N space separated integers, gold in each row of the grid.

Output Format:
--------------
Print an integer, maximum amount of gold.


Sample Input-1:
---------------
3 3
0 6 0
5 8 7
0 9 0

Sample Output-1:
----------------
24

Explanation:
-------------
You can grab the gold in KGF grid as follows:
You can obtain like as follows: 9 -> 8 -> 7.

Sample Input-2:
---------------
5 3
1 0 7
2 0 6
3 4 5
0 3 0
9 0 20

Sample Output-2:
----------------
28

Explanation:
-------------
You can grab the gold in KGF grid as follows:
You can obtain like as follows: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

'''

# Solution:

def KGF(grid):
        
    def dfs(i, j, g):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return g

        if grid[i][j] == "#":
            return g
            
        g += grid[i][j]
            
        temp = grid[i][j]
        grid[i][j] = "#"

        g = max(dfs(i+1, j, g), dfs(i-1, j, g), dfs(i, j+1, g), dfs(i, j-1, g))

        grid[i][j] = temp

        return g
    
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            ans = max(ans, dfs(i, j, 0))
              
    return ans
    
if __name__=="__main__":
    m,n=map(int,input().split())
    grid=[]
    for i in range(m):
        row=list(map(int,input().split()))
        grid.append(row)
    print(KGF(grid))