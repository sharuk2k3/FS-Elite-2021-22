'''


Giridhar went to a bank to get 1-rupee coins for N rupees.
In the cash counter, there are unlimited CoinBags, 
each bag contains square number of coins (i.e, 1,4,9,16,...)

The clerk in the cash counter needs to provide the CoinBags,
Find the minimum number of CoinBags to give to Giridhar, whose total value equals N rupees.

Input Format:
-------------
An integer N.

Output Format:
--------------
Print an integer, minimum number of bags.


Sample Input-1:
---------------
13

Sample Output-1:
----------------
2

Explanation: 13 = 9 + 4

Sample Input-2:
---------------
21

Sample Output-2:
----------------
3

Explanation: 21 = 16+4+1.
'''


def func(n):
    T = [[i, -1] for i in range(n+1)]
    # T = [0] * (n + 1)
    for i in range(n + 1):
        j = 1
        while j*j <= i:
            T[i] = min(T[i], 1 + T[i - j*j])
            j += 1
    return T[n]
if __name__ == '__main__':

    n = int(input())
    
    print(func(n))