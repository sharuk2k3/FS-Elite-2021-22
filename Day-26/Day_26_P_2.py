'''

Thomas constructing a Tree of N nodes, nodes labelled as 0, 1, 2, .. ,n-1.
He is given a list of N-1 edges[], where edge[i]=[v1, v2], is an undirected 
edge between v1 and v2.

He can construct the tree by selecting any node as root node. Your task is
to find out the trees with the smallest height, among all the trees. 
Print the root nodes of all the smallest height trees in ascending order.

NOTE: A Tree, is a connected graph without simple cycles.

Input Format:
-------------
Line-1: An integer N, number of nodes.
Next N-1 lines: Two integers, represent an edge.

Output Format:
--------------
Print the list of root nodes of Smallest Height Trees in ascending order


Sample Input-1:
---------------
4
0 1
2 1
1 3

Sample Output-1:
----------------
[1]

Explanation:
-------------
For Tree Combinations look at the hint.


Sample Input-2:
---------------
6
3 0
1 3
3 2
4 3
5 4

Sample Output-2:
----------------
[3, 4]


'''

#SOLUTION

import collections

def SmallHeightTrees(n, nodes):
    if n <= 1:
        return [0]
    g = collections.defaultdict(list)
    d = [0] * n
    
    for a, b in nodes:
        g[a].append(b)
        g[b].append(a)
        d[a] += 1
        d[b] += 1
        
    q = [ n for n in range(n) if d[n]==1 ]
    
    while q:
        tmp = []
        ans = q
        for l in q:
            for i in g[l]:
                d[i] -= 1
                if d[i] == 1:
                    tmp.append(i)
        q = tmp
        
    return ans
    
    
if __name__=="__main__":    
    n=int(input())
    nodes=[]
    for i in range(n-1):
        row=list(map(int,input().split()))
        nodes.append(row)
    print(SmallHeightTrees(n, nodes))