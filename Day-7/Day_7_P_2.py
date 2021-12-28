'''

KCR Chief Minister of Telangana Government has passed a new G.O to Telangana police for
safety of Telangana people. In this regard he announced new Vehicles to be released for all
the stations working for this mission especially.
Here we have a 2D mesh, there are P police officers and V vehicles, with P<=V.
Each police officer and vehicle is a 2D coordinate on this mesh.
Here the government has assigned a unique vehicle to each police officer.

Now create a method which prints the minimum possible sum of distances between each
police officer and their assigned vehicle.

Here the distance is between police officer Pi and vehicle Vi assigned to him.
And distance between Pi, Vi is calculated as follows: |Pi.x - Vi.x| + |Pi.y - Vi.y|


Input Format:
-------------
Line-1: Two integers P and V, number of police officers and vehicles.
Next P lines: Two space separated integers co-ordinates of Police officers.
Next V lines: Two space separated integers co-ordinates of Vehicles.

Output Format:
--------------
Print an integer, the minimum possible sum of distances.


Sample Input-1:
---------------
3 3
0 1		// co-ordinates of police
1 2
1 3
4 5		// co-ordinates of vehicles
2 5
3 6

Sample Output-1:
----------------
17


Sample Input-2:
---------------
2 2
0 0		// co-ordinates of police
2 1
1 2		// co-ordinates of vehicles
3 3

Sample Output-2:
----------------
6


case =1
input =2 2
0 0
2 1
1 2
3 3
output =6

case =2
input =3 3
0 1
1 2
1 3
4 5
2 5
3 6
output =17

case =3
input =2 3
0 1
1 2
4 5
2 5
3 6
output =12

case =4
input =3 3
0 0
1 1
2 0
1 0
2 2
2 1
output =4

case =5
input =5 5
0 0
1 0
2 0
3 0
4 0
0 999
1 999
2 999
3 999
4 999
output =4995

case =6
input =6 8
0 0
1 7
12 20
23 660
564 23
729 81
999 999
49 1
33 144
26 476
555 666
666 777
777 888
888 999
output =2938

case =7
input =8 8
1 100
2 200
3 300
4 400
5 500
6 600
7 700
8 800
900 99
800 88
700 77
600 66
500 55
400 44
300 33
200 22
output =7480

case =8
input =5 7
1 100
2 200
3 300
4 400
5 500
200 22
300 33
400 44
500 55
600 66
700 77
800 88
output =3265


'''

#SOLUTION

import heapq
def assignVehicle(Police,Vehicle):
    def dis(i, j):
        return abs(Police[i][0] - Vehicle[j][0]) + abs(Police[i][1] - Vehicle[j][1])
        
    h = [[0, 0, 0]]
    seen = set()
    while True:
        cost, i, taken = heapq.heappop(h)
        if (i, taken) in seen: continue
        seen.add((i, taken))
        if i == len(Police):
            return cost
        for j in range(len(Vehicle)):
            if taken & (1 << j) == 0:
                heapq.heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])

p, v = map(int, input().split())

Police = []
Vehicle = []
setv = set()

for _ in range(p):
    x, y = map(int, input().split())
    Police.append((x, y))
for _ in range(v):
    x, y = map(int, input().split())
    Vehicle.append((x, y))
    
    
if __name__=="__main__":
    print(assignVehicle(Police,Vehicle))