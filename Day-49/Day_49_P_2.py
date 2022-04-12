'''

You have given a bagful of N colored balls, the color codes of the balls 
are distinct. Your task is to print "true", if and only if the number of balls
having different color codes in the bag are distinct. Otherwise, print "false".

Input Format:
-------------
Line-1: An integer N, number of balls.
Line-2: N space separated integers, the color codes of the balls.

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
6
1 2 2 1 1 3

Sample Output-1:
----------------
true

Explanation:
------------
The number of balls in the bag having color code-1 are 3,
The number of balls in the bag having color code-2 are 2,
The number of balls in the bag having color code-3 are 1.
The count of balls having distinct color codes are not same.


Sample Input-2:
---------------
3
1 2 3

Sample Output-2:
----------------
false


'''

#Solution:


from collections import defaultdict
def distinctColor(n, arr):
    #d = {}
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
        
    s = set()
    for i, j in d.items():
        if j not in s:
            s.add(j)
        else:
            return False
    return True
        
n=int(input())
arr=list(map(int,input().split()))
print(distinctColor(n,arr))