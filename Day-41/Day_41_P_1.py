'''

Amith decided go on a holiday trip. 
Given a map of N holiday spots numbered 0,1,2,.. N-1, map shows the connecting 
routes between the holiday sopts, the routes are bidirectional, and
the connecting routes are indicates as routes[i] = [from , to , distance ]. 
He can travel only a certian distance D.

Your task is to find the holiday spot H with the smallest number of holiday-spots
that are reachable from H and whose distance is at most D, 

If there are multiple holiday spots, return H with the greatest number.


Input Format:
-------------
Line-1 : Three integers, N number of holiday spots, R is the number of connecting 
        routes and D is the distance can travel.
Next R lines : Three space separated integers, from , to and distance.

Output Format:
--------------
Print an integer, holiday spot.


Sample Input-1:
---------------
4 4 4
0 1 3
1 2 1
1 3 4
2 3 1

Sample Output-1:
----------------
3


Explanation:
------------
Distance can travel= 4,

From			Reachable sopts
-------------------------------------
Holiday-spot 0 -> [Holiday-spot 1, Holiday-spot 2] 
Holiday-spot 1 -> [Holiday-spot 0, Holiday-spot 2, Holiday-spot 3] 
Holiday-spot 2 -> [Holiday-spot 0, Holiday-spot 1, Holiday-spot 3] 
Holiday-spot 3 -> [Holiday-spot 1, Holiday-spot 2] 

Holiday-spots 0 and 3 have 2 reachable Holiday-spots at a distance = 4, 
but we have to return Holiday-spot 3 since it has the greatest number.


Sample Input-2:
---------------
5 6 2
0 1 2
0 4 8
1 2 3
1 4 2
2 3 1
3 4 1

Sample Output-2:
----------------
0

Explanation:
------------
Distance can travel= 2,

From			Reachable sopts
-------------------------------------
Holiday-spot 0 -> [Holiday-spot 1] 
Holiday-spot 1 -> [Holiday-spot 0, Holiday-spot 4] 
Holiday-spot 2 -> [Holiday-spot 3, Holiday-spot 4] 
Holiday-spot 3 -> [Holiday-spot 2, Holiday-spot 4]
Holiday-spot 4 -> [Holiday-spot 1, Holiday-spot 2, Holiday-spot 3]

Holiday-spots 0 has 1 reachable Holiday-spot at a distance = 2, 


'''

import heapq

def findHolidaySpot(n, holidaySpots, d,r):
    graph = {i:dict() for i in range(n)}
    for u,v,w in holidaySpots:
        graph[u][v] = w
        graph[v][u] = w
    
    neighbors = [0]*n
        
    for k in range(n):
        dist = [float('inf')]*n
        dist[k] = 0
        visited = [False]*n
            
        queue = [(0, k)]
        heapq.heapify(queue)
            
        count = -1

        while len(queue):
            minVal, minNode = heapq.heappop(queue)
            if minVal > d: break
            if visited[minNode]: continue
            visited[minNode] = True
            count += 1
            for node in graph[minNode]:
                if not visited[node] and dist[minNode] + graph[minNode][node] < dist[node]:
                    dist[node] = dist[minNode] + graph[minNode][node]
                    heapq.heappush(queue, (dist[node], node))

        neighbors[k] = count
            
    curMin = neighbors[0]
    ans = 0
    for i in range(n):
        if neighbors[i] <= curMin:
            ans = i
            curMin = neighbors[i]

    return ans
    
n,r,d=map(int,input().split())
holidaySpots=[]
for _ in range(r):
    holidaySpots.append(list(map(int,input().split())))

if __name__=="__main__":
    print(findHolidaySpot(n, holidaySpots, d,r))
    