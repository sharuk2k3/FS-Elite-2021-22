'''

There are some bulbs arranged in the form of grid on a wall,
Each bulb can emit either blue light or red light, where blue light 
indicates with 0 and red light indicates with 1.
You are given the initial arrangement of the bulbs.

You are allowed to perform the following toggle operation, 
- You can choose any row or column of bulbs 
- You can toggle each bulb color in that row or column 
(i.e., changing all blue to red[0's to 1's] and red to blue [ 1's to 0's]).

Your task is to return 'true' if it is possible to toggle all the bulbs in
the arrangement to emit blue light, by using any number of toggle operations 
or 'false' otherwise.

NOTE: It is a rectangular grid.

Input Format:
-------------
Line-1: Two space separated integers M and N, size of the grid
Next M lines: N space separated integers, either 0 or 1.

Output Format:
--------------
Print a boolean value


Sample Input-1:
---------------
3 3
1 0 1
0 1 0
1 0 1

Sample Output-1:
----------------
true

Explanation: 
------------
Toggle the bulbs in column-1 and column-3
Now, The arrangement looks like
0,0,0
1,1,1
0,0,0

Now toggle the bulbd in row-2, So that all the bulbs emit blue color only.
0,0,0
0,0,0
0,0,0


Sample Input-2:
---------------
3 3
1 0 0
0 1 0
0 0 0

Sample Output-2:
----------------
false



'''

#Solution

def ToggleBlueOnes(grid):
    #r = [a ^ 1 for a in grid[0]]
    #return all(row == grid[0] or row == r for row in grid)
    return all(grid[i] == grid[0] or all(grid[i][j] != grid[0][j] for j in range(len(grid[0]))) for i in range(1, len(grid)))

m,n=map(int,input().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))
    
print(ToggleBlueOnes(grid))
    
