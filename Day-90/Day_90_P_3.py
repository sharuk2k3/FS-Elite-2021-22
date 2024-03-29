'''

Mr Ashoka planted N trees in a land around the Flag Post which is at the center 
of the land, i.e., (0,0) position. You will be given the positions of N trees
as trees[], where tree[i]=[Xi,Yi], where Xi, Yi are the positions of i-th tree
with respect to X-axis and Y-axis. And you are also an integer C.

The distance between any two trees on the land plane is the Euclidean distance 
(i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2).

Your task is to return positions of the C trees Nearest to the Flag post. 
The answer is supposed to be sorted based on distance, if the distances 
are same keep the original order of the trees[].


Input Format:
-------------
Line-1: Two space separate integers, N and C
Next N Lines: Two space separated integers, x,y

Output Format:
--------------
Print the positionf of C Nearest Trees.

Sample Input-1:
---------------
4 4
-3 -3
3 -3
3 3
-3 3

Sample Output-1:
----------------
[-3, -3] [3, -3] [3, 3] [-3, 3]


Sample Input-2:
---------------
4 3
2 -1
1 2
2 4
3 2

Sample Output-2:
----------------
[2, -1] [1, 2] [3, 2]



'''

#Solution
import heapq

def kClosest(points, k):
    h=[]
    heapify(h)
    for pt in points:
        heappush(h, (pt[0]**2 + pt[1]**2,pt))
    l=[]
    while k>0:
        ele = heappop(h)
        l.append(ele[1])
        k-=1
    return(l)

if __name__ == '__main__':
    n,k=map(int,input().split())
    points=[]
    for _ in range(n):
        l=list(map(int,input().split()))
        points.append(l)
    print(kClosest(points, k))