'''

A forest is represented as a square grid consist of 0's an 1's only.
Few people stuck in the forest, where 1's are indicate people, 
and 0's are indicate as trees. A person cannot move from the tree.

You want to save people, a person can be saved, if he/she connected to other 
person who is at the boundary of forest.
If 'a' is connected to 'b' and 'b' is connected to 'c',
then you can consider that 'a' is also connected to 'c'. 
They can connected in 4 directions only (up, right, left and down).

You need to find out the number of persons, whom cannot be saved from 
the given forest grid.


Input Format:
-------------
Line-1 -> An integer N, size of the grid N*N
next N lines -> N space separated integers(0's and 1's)

Output Format:
--------------
Print an integer as your result


Sample Input-1:
---------------
5
0 0 1 1 0
1 0 0 1 0
0 0 1 0 0
0 1 1 0 1
1 0 0 1 0

Sample Output-1:
----------------
3

Explanation:
------------
In the given grid, 1's at (2,2), (3,1), (3,2) positions are not connected 
to the boundary. So, number of people cannot be saved are 3

Sample Input-2:
---------------
5
0 0 1 1 0
1 0 0 1 0
0 0 1 1 0
0 1 1 0 1
1 0 0 1 0

Sample Output-2:
----------------
0

Explanation:
------------
In the given grid, each 1 is either at the boundary or connceted to 1 at boundary.
So, number of people cannot be saved are '0'



'''
#Solution:
#Using DFS
def numEnclaves(grid) :
    res = 0
    m = len(grid)
    n = len(grid[0])
   
    def dfs(grid, i, j):
        
        if i < 0 or j < 0 or i >= m or j >= n:
            return
         
        if grid[i][j] == 0:
            return
        
        grid[i][j] = 0
         
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)
        
    for j in range(n):
        dfs(grid, 0, j)
        dfs(grid, m - 1, j)
    
    for i in range(m):
        dfs(grid, i, 0)
        dfs(grid, i, n - 1)
        
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res += 1
    return res

n=int(input())
grid = []
for _ in range(n):
    row=list(map(int,input().split()))
    grid.append(row)
print(numEnclaves(grid))