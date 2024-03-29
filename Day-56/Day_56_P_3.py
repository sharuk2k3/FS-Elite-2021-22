'''

A courier company has to deliver N items with different heights.
All the items have to deliver to one building only.

The building has K rooms inside indexed 0,1,...,K-1, and the heights of 
the rooms are different. All the rooms connected with each other and has 
two entry points, one entry is at frontside and other entry is at backside of 
the building . e.g, you can reach room-1 from room-0 only, room-2 from 
room-1 only, ..so on, and vice-versa.

Now the task of the delivery agent is to keep the items inside the building.

To keep the items into the rooms, delivery agent has to follow these rules:
 - Agent can't keep, two goods in one room.
 - Agent can enter into the building either from frontside or from back side,
   If the height of some room is less than the height of an item,
   then the item will be stopped before that room, so are the items behind it.
 - Agent can rearrange the order of items to keep them inside the building.
   
Your task is to return the maximum number of items, the delivery agent can keep 
inside the building.

Input Format:
-------------
Line-1 -> two integers N and K, number of items and number of rooms.
Line-2 -> N space separated integers, heights of the items.
Line-3 -> K space separated integers, heights of the rooms.

Output Format:
--------------
Print an integer as result.


Sample Input-1:
---------------
5 4
2 3 3 4 5
4 5 2 3

Sample Output-1:
----------------
4

Explanation:
------------
We can first keep the item of height 2 in room 2. 
Then we can keep the item of height 3 in room 3.
Then we can keep the item of height 3 in room 1.
Then we can keep the item of height 4 in room 0.


Sample Input-2:
---------------
4 5
4 6 6 3
3 2 4 5 6

Sample Output-2:
----------------
3

Explanation:
------------
Notice that it's not possible to keep the two items of height 6 into the building,
since there's only 1 room of height >= 6
Other valid solutions are to put the item with height 4 in room 2 or 
to put the item with height 3 in room 2 or room 0 before putting 
the the item with height 4 and 6.




'''

import sys
n, k = map(int, input().split())
hi = list(map(int, input().split()))
hr = list(map(int, input().split()))
l1 = []
l2 = []
m = sys.maxsize
for i in hr:
    m = min(i, m)
    l1.append(m)
m = sys.maxsize
for i in hr[::-1]:
    m = min(i, m)
    l2.append(m)
l2 = l2[::-1]
ansList = []
for i, j in zip(l1, l2):
    ansList.append(max(i, j))
hi.sort()
hi = hi[::-1]
ans = 0
for i in hi:
    for j in range(len(ansList)):
        if ansList[j] >= i:
            ansList[j] = -1
            ans += 1
            break
print(ans)