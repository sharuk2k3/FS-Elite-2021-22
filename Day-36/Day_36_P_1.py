'''

For Siddarth's Birthday his friends planned cake cutting.
On top of the cake there are two lines of candles, 
all the candles with different heights. 
The lines are parallel lines, line-P and line-Q .
Siddarth has to blow all the candles in one go.

So, he can swap one candle at a time, from P and Q and 
the position of the candles in their line should be same.

At the end of the swaps, The candles in set P and set Q, 
should be in ascending order of their heights.

You will be heights of the candles initially in P and Q, after placing in parallel lines.

Your task is to find the minimum number of swaps required
to arrange the candles in P and Q in ascending orer.

Note: It is guaranteed that the answer is always possible.

Input Format:
-------------
Line-1: An integer N, num of candles in P and Q.
Line-2: N space separated integers, heights of the candles in Line-P.
Line-3: N space separated integers, heights of the candles in Line-Q.

Output Format:
--------------
Print an integer, minimum number of swaps required.


Sample Input-1:
---------------
4
1 3 5 4
1 2 3 7

Sample Output-1:
----------------
1

Explanation:
------------
Swap the 4th candle in P and Q. 
Then the heights of the candles in P = [1, 3, 5, 7],  Q = [1, 2, 3, 4]
Both are in ascending order.


Sample Input-2:
---------------
7
1 3 5 8 14 13 14
2 5 7 6 11 15 16

Sample Output-2:
----------------
2

Explanation:
------------
Swap the 4th, 5th candles in P and Q. 
Then the heights of the candles in 
P = [1, 3, 5, 6, 11, 13, 14],  
Q = [2, 5, 7, 8, 14, 15, 16]
Both are in ascending order.


'''

#Solution

def SwapArrays(p,q):
    swap, keep, n = 1, 0, len(p)
    for i in range(1, n):  
        new_swap = new_keep = n  
        if p[i] > p[i-1] and q[i] > q[i-1]:  
            new_keep = keep if keep < new_keep else new_keep
            new_swap = swap+1 if swap+1 < new_swap else new_swap
        if p[i] > q[i-1] and q[i] > p[i-1]: 
            new_keep = swap if swap < new_keep else new_keep
            new_swap = keep+1 if keep+1 < new_swap else new_swap
        swap, keep = new_swap, new_keep
    return min(swap, keep)

n=int(input())
p=list(map(int,input().split()))[:n]
q=list(map(int,input().split()))[:n]
print(SwapArrays(p,q))