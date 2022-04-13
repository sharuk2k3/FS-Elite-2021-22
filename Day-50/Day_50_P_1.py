'''

Skandhanshi Infra Township constructed N Villas in a row.
They planned to paint the villas with three colors, 
snow-white, sky-blue and light-green. 
And adjacent villas should not paint with same color.

You are given the cost of painting each villa with these colors, cost[N][3].
cost[i][0] is cost of painting with snow-white.
cost[i][1] is cost of painting with sky-blue.
cost[i][2] is cost of painting with light-green.
where, 0 <= i < N.

Your task is to find the minimum cost to paint all the villas.

Input Format:
-------------
Line-1: An integer N, number of villas.
Next N lines: 3 space separated integers, cost to paint the villas.

Output Format:
--------------
Print an integer, minimum cost to paint all the villas.


Sample Input:
---------------
3
17 2 17
16 4 5
14 3 19

Sample Output:
----------------
10

Explanation: 
------------
1st Villa painted with sky-blue, 2nd Villa painted with light-green,
3rd Villa painted with sky-blue.
Minimum cost: 2 + 5 + 3 = 10.




'''



#Solution:

def minCost(costs):
    size=len(costs)
    if size == 0: 
        return 0
    if size == 1: 
        return min(costs[0])
    for i in range(1,size):
        costs[i][0]+=min(costs[i-1][1],costs[i-1][2])
        costs[i][1]+=min(costs[i-1][0],costs[i-1][2])
        costs[i][2]+=min(costs[i-1][1],costs[i-1][0])
    return min(costs[-1])
r=int(input())
costs=[]
for i in range(r):
    row=list(map(int,input().split()))
    costs.append(row)
print(minCost(costs))