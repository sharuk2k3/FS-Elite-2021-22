'''

Sampoornesh Babu is learning arithmatics.
His teacher given him a task to find the minimum number of operations
required to convert a given integer I to 1.

Sampoornesh is allowed to perform the following operations:
	- If I is even, convert I with I/2 .
	- In I is odd, convert I with either I+1 or I-1.

Now it's your task to help Sampoornesh Babu to find and print
the minimum number of operations required.

Input Format:
-------------
An integer I.

Output Format:
--------------
Print an integer, the minimum number of operations required.


Sample Input-1:
---------------
10

Sample Output-1:
----------------
4

Explanation:
------------
10 -> 5 -> 4-> 2 -> 1.


Sample Input-2:
---------------
15

Sample Output-2:
----------------
5

Explanation:
------------
15 -> 16 -> 8 -> 4 -> 2 -> 1.


'''

#SOLUTION

import sys
def ConvertTo1(n, c):
    
    global ans
    
    if n == 1:
        ans = min(c,ans)
        return
    
    if n%2 == 0:
        n //= 2
        ConvertTo1(n, c+1)
    
    else:
        ConvertTo1(n-1, c+1)
        ConvertTo1(n+1, c+1)
if __name__=="__main__":
    n = int(input())
    ans = sys.maxsize
    ConvertTo1(n, 0)
    print(ans)
