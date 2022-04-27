'''


Karthik is going on a world tour, He prefers to travel in airplanes.
He is given a list of planes avaialble , where a plane[i]=[src-i, dest-i].
i.e, plane[i] indiactes airplane from source city to destination city.

Your task is to findout in which city karthk will end up his world tour.
end up the tour means, he cannot travel further from that city.

Note: It is guaranteed that there is no loop. 

Input Format:
-------------
Line-1: An integer N, number of airplanes routes.
next N lines: two comma (',') separated Strings, source and destination.

Output Format:
--------------
Print a string, City Name.


Sample Input:
---------------
3
London,New York
New York,Sydney
Sydney,New Delhi

Sample Output:
----------------
New Delhi




'''

n = int(input())
dict1 = {}
for i in range(n):
    l = input().split(",")
    dict1[l[0]] = dict1.get(l[0],0)+1
    dict1[l[1]] = dict1.get(l[1],0)
for i in dict1:
    if dict1[i] == 0:
        print(i)