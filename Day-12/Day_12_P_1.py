'''
Swiss Castle bakers has recivied P orders of cakes, and each cake has 
to filled with Q types of creams. To prepare varieties of creams, each 
variety takes different amounts of time in minutes, where i-th variety 
takes time[i] minutes.

You need to prepare P cakes. To prepare a cake, you need to use Q adjacent 
creams from the cook. The cook can prepare N varieties of creams, the i-th 
variety will be ready in time[i] minutes, and then you can use it to fill 
the cake.  [ Note: you can use each variety only once ].
 
Your task is to find and return the minimum time (in minutes) required, 
to prepare P cakes filled with Q types of creams. If it is impossible to 
prepare P cakes, print -1.


Input Format:
-------------
Line-1: Three space separated integers, N, P and Q.
Line-2: N space separated integers, time[].

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
6 2 2
3 7 2 2 4 8

Sample Output-1:
----------------
7

Explanation:
-------------
* means not ready, R means ready.
Minute-1: * * * * * *
Minute-2: * * R R * *
Minute-3: R * R R * *
Minute-4: R * R R R *
Minute-5: R * R R R *
Minute-6: R * R R R *
Minute-7: R R R R R *
Now you can create two cakes with two varieties of fillings
Cake-1 can use variety-2 and variety-3
Cake-2 can use variety-0 and variety-1.

Sample Input-2:
---------------
5 3 2
2 3 5 3 4

Sample Output-2:
----------------
-1

Explanation:
------------
We need 6 varieties of creams to prepare 3 cakes.
We have only 5 varieties, so not possible. Print -1.


'''

from sys import exit
import math
def func(n, p):
    
    global q
    
    L = ["*" for i in range(len(l))]
    for i in range(len(l)):
        if l[i] <= n:
            L[i] = "R"
            
            
    L = "".join(L)
    while "R"*q in L:
        L = L.replace("R"*q, "-1", 1)
        p -= 1
    L = [i for i in L]
#     print("p=", p, "\t", *L)
    
    if p <= 0:
        ans.append(n)
        return 1
    else:
        return 0 

def binarySearch(n, p):
    
    s = 1
    e = n
    
    while s<=e:
        
        mid = math.ceil((s+e)/2)
        
        if func(mid, p):
            e = mid-1  
        else:
            s = mid+1
    
n, p, q = map(int, input().split())
l = list(map(int, input().split()))
if p*q > n:
    print(-1)
    exit(0)
t = max(l)
ans = []
binarySearch(t, p)
print(min(ans))







