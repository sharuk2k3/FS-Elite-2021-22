"""

Mounika is creating the binary strings using P 1's and Q 0's.
A binary string contains only 0's and 1's.
She has given a list of binary strings binStr[] to be formed.

Her task is to find, the maximum number of binary strings can be formed, 
with given P no.of 1's and Q no.of 0's only. She cannot use any more 1's or 0's.

Input Format:
-------------
Line-1 -> A single line of space separated binary strings, binStr[].
Line-2 -> Two integers P and Q, P number of 1's and Q number of 0's


Output Format:
--------------
Print an integer as output, maximum number of binary strings can be formed.


Sample Input-1:
---------------
10 0001 111001 1 0
3 5

Sample Output-1:
----------------
4

Explanation:
------------
She can form 4 strings by the using of 3 1's and 5 0's
strings are 10, 0001, 1, 0.


Sample Input-2:
---------------
10 1 0
1 1

Sample Output-2:
----------------
2

Explanation:
------------
She can form 2 strings by the using of 1 1's and 1 0's
strings are 1, 0.



"""

#Solution:

#DP-Bottom Up

def MaxBinStr(binStr,P,Q):
    dp = [[0] * (Q + 1) for _ in range(P + 1)]

    for s in binStr:
        zero = s.count('0')
        one = s.count('1')

        for i in range(P,-1,-1):
            for j in range(Q,-1,-1):
                if zero <= i and one <= j:
                    dp[i][j] = max( dp[i][j] ,1 + dp[i-zero][j-one])
                
    return dp[-1][-1]

if __name__ == '__main__':
    binStr =list(map(str, input().strip().split())) 
    P, Q = map(int, input().split())
print(MaxBinStr(binStr,P,Q))