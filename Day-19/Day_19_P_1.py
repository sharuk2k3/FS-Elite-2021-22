'''

Mahalakshmi participated in a treasure-hunt conatins N boxes in it.
Each box is numbered from 0,1,2,3,...,N-1. 
All the boxes are intially locked with the passcodes, except Box-0.
The passcode is written in a envolope and marked with its concern box number.

Each box in the treasure hunt contains a list of envelopes, which has 
passcodes to open the other boxes. You can open the boxes in any order, 
but you have to start from box-0 intially.

The rule to win the treasure-hunt is to open all the boxes.
Your task is to find out, whether Mahalakshmi win the treasure hunt or not.
If she win, print "Win".
Otherwise, print "Lost"

Input Format:
-------------
Line-1: An integer, number of boxes.
Next N lines: space separated integers, box numbers.

Output Format:
--------------
Print a string value, Win or Lost


Sample Input-1:
---------------
5
1
2
3
4
3

Sample Output-1:
----------------
Win

Sample Input-2:
---------------
4
1 3
3 0 1
2
0

Sample Output-2:
----------------
Lost

case =1
input =4
1
2
3
0
output ="Win"

case =2
input =4
1 3
3 0 1
2
0
output ="Lost"

case =3
input =5                                                                                                                     
1                                                                                                              
2 3                                                                                                                
4 0                                                                                                                    
2 4                                                                                                                     
3
output ="Win"

case =4
input =6                                                                                                            
0                                                                                                              
2 3                                                                                                                
4 0 5                                                                                                                  
2 4                                                                                                                     
3
1 4
output ="Lost"

case =6
input =12
11 1 2
10 3
9 
8
7
6 4 2 1
1
5
2 1 8 5 4 0
4
3
0
output ="Win"

case =7
input =9
1
2
3
0
2 5
4 6 7
5 8
7
6 2 1
output ="Lost"

case =8
input =9
1
2
3
4
2 5
4 6 5
5 8
7
6 2 7
output ="Win"

'''


#SOLUTION

from collections import defaultdict
def canVisitAll(boxes):
    adjacency_dict=defaultdict(list)
        
    for i,node in enumerate(boxes):
        if len(node)==0:
            adjacency_dict[i].append(i)
        else:
            for rm_key in node:
                adjacency_dict[i].append(rm_key)
    visited=set()
    while adjacency_dict:
        stack=[next(iter(adjacency_dict))]
        while stack:
            cur_rm=stack.pop()
                
            if cur_rm not in visited:
                visited.add(cur_rm)
                    
                for cnnctd_rm in adjacency_dict[cur_rm]:
                    stack.append(cnnctd_rm)
                del(adjacency_dict[cur_rm])
        if adjacency_dict:
            return "Lost"
            
    return "Win"
n = int(input())
boxes = []
for i in range(n):
    lst=list(map(int,input().split()))
    boxes.append(lst)
print(canVisitAll(boxes))

'''
#Test Case 8 Failing
def rep(L, i):
    
    for k in L[i]:
        if mark[k]:
            return
        mark[k] = 1
        rep(L, k)
        
    return

n = int(input())
L = []
mark = [0 for i in range(n)]
for i in range(n):
    L.append(list(map(int, input().split())))
rep(L, 0)
mark[0] = 1
f = 0
for i in mark:
    if i == 0:
        f = 1
        break
if f:
    print("Lost")
else:
    print("Win")
'''