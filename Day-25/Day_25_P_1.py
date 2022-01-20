'''

Aravind went to a forest, he stuck inside the forest and He is blind.
The forest is given as a square grid. The forest grid is filled with trees 
and empty cells. He can move upwards, downwadrs, left and right, 
but he cannot stop until he touches the tree. Once he touches a tree, 
he can choose the next direction to move. Intially Aravind is at poistion A, 
and he is trying to reach a safe-point at position S.

You will be given the forest grid filled with 1's and 0's, 1 means tree 
and 0 means empty cell. And initial position of Aravind, safe-point S.

Your task is to find the minimum distance travelled by Aravind to reach 
the safe-point, If he cannot stop at the safe-point, return -1.

You may assume that the borders of the forest are all trees.


Input Format:
-------------
Line-1: An integer N, size of the grid.
Next N lines: N space separated integers
Next line:  two space separated integers, initial position of Aravind
Next line:  two space separated integers, position of safe-point.

Output Format:
--------------
Print an integer, minimum distance travelled by Aravind to reah safe-point.


Sample Input-1:
---------------
5
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 0 1
0 0 0 0 0
2 4
4 0

Sample Output-1:
----------------
10

Explanation:
------------
For Picture look at hint.
The minimum path is : up -> left -> down -> left.

Sample Input-2:
---------------
5
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 0 1
0 0 0 0 0
0 3
3 3

Sample Output-2:
----------------
-1

Explanation: 
------------
Aravind cannot stop at safe-point.



'''

#SOLUTION
import heapq

def FoolBlindManPlease(grid, arvind, safe_point):
    m, n = len(grid), len(grid[0])
    arvind, safe_point = tuple(arvind), tuple(safe_point)
    q, visited = [(0, arvind)], set(arvind)

    def dfs(x, y):
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            i, j, d = x, y, 0
            while 0 <= i + direction[0] < m and 0 <= j + direction[1] < n and grid[i + direction[0]][j + direction[1]] == 0:
                i += direction[0]
                j += direction[1]
                d += 1
                
            yield (i, j), d

    while q:
        d, curr = heapq.heappop(q)
        if curr == safe_point:
            return d
            
        if curr in visited: continue
        visited.add(curr)
        
        for neighbor, distance in dfs(*curr):
            heapq.heappush(q, (d + distance, neighbor))
            
    return -1
    
if __name__=="__main__":    
    r=int(input())
    grid=[]
    for i in range(r):
        row=list(map(int,input().split()))
        grid.append(row)
    arvind=map(int,input().split())
    safe_point=map(int,input().split())

    print(FoolBlindManPlease(grid, arvind, safe_point))
