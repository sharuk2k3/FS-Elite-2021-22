'''

Mr Bilahari is working with Binary String BS,
He is given an integer D.
Your task is to find the length of the subsequence of BS whose decimal value is 
less than or equal to D, whihc is maximum in length.

Note: The subsequence can contain leading zeroes


Input Format:
-------------
Line-1: A binary string, bs
Line-2: An integer, D

Output Format:
--------------
An integer result.


Sample Input-1:
---------------
1000110010
5

Sample Output-1:
----------------
7

Explanation: 
------------
The longest binary sub sequence is 0000010 which is 2 less than 5


Sample Input-2:
---------------
1001010
6

Sample Output-2:
----------------
5

Explanation: 
------------
The longest binary sub sequence are 00010, 00100, or 00101 the values are less than 6.



'''
#Solution:

'''

#Greedy approach

We need to take all zeros.
zero, one for '0', '1' count.
maxOne for the max amount of 1 we can take
loop from back to front, once we meet "1", we add the value 1<<(zero+one) to total.
If total<=k, we can take the "1", then we update maxOne
The answer is the amount of maxOne plus the amount of zero


'''

def maxSubsequence(s):
    zero = 0
    total = 0
    one = 0
    ans = 0
    maxOne = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='0':
            zero+=1
        else:
            total |= 1<<(zero+one)
            one+=1
            if total<=d:
                maxOne = one
    return zero+maxOne

if __name__=="__main__":
    s=input()
    d=int(input())
    print(maxSubsequence(s))