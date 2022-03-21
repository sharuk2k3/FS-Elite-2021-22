'''

A forest is represented as a square grid consist of 0's an 1's only. Few people
stuck in the forest, where 1's indicate people, and 0's indicate trees. 
The people cannot pass through the tree.

Your target is to save people, a person can be saved, if he/she connected
to other person who is at the boundary of forest, like as follows:
    - If 'a' is connected to 'b' and 'b' is connected to 'c',
      then you can consider that 'a' is also connected to 'c'. 
    - The people can connect each other in 4 directions only. 
      (up, right, left and down)

You need to find out the number of persons, who cannot be saved from the forest.


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
In the given grid, 1's at (2,2), (3,1), (3,2) positions are not connected to
the boundary. So, number of people cannot be saved are 3.


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

def Forest(i, j, n, l):
    if i<0 or j<0 or i>=n or j>=n:
        return
    
    if l[i][j] == 1:
        l[i][j] = 0
        Forest(i+1, j, n, l)
        Forest(i-1, j, n, l)
        Forest(i, j+1, n, l)
        Forest(i, j-1, n, l)

n = int(input())
l = []
for _ in range(n):
    l.append([int(i) for i in input().split()])

for i in range(n):
    Forest(i, 0, n, l)
    Forest(0, i, n, l)
    Forest(n-1, i, n, l)
    Forest(i, n-1, n, l)

c = 0
for i in l:
    for j in i:
        if j == 1:
            c += 1
print(c)
