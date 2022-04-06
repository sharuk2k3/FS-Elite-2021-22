'''

Shaggy Rogers is working with numbers.
He is given a number N, 
He wants to replace all occurrences of a digit in the number N,
with another digit between [0-9]. May be with same number too.

But there should not be any leading zeros in the number after the replacement,
Or the number should not become zero.

Rogers can perform the replacement of the occurrences of the digit in N for two 
times, He will generate two new numbers P and Q, such that the value of |P-Q| 
should be Maximum.

Your task is to help Shaggy Roers to find the maximum difference of P and Q possible.


Input Format:
-------------
An integer N, the number

Output Format:
--------------
Print an integer, the maximum difference of P and Q


Sample Input-1:
---------------
123

Sample Output-1:
----------------
820

Explanation:
------------
Replacement-1: replace 1 with 9 you will get P as 923
Replacement-2: replace 2 with 0 you will get Q as 103
So Max difference is 820.


Sample Input-2:
---------------
4254

Sample Output-2:
----------------
8008

Explanation:
------------
Replacement-1: replace 4 with 9 you will get P as 9259
Replacement-2: replace 4 with 1 you will get Q as 1259
So Max difference is 8008.


'''

#Solution:

def ReplaceDigits(n):
    s = str(n)
    max_num = float('-inf')
    for i in range(len(s)):                        
        n1 = int(s.replace(s[i], '9'))
        max_num = max(max_num, n1 - int(s.replace(s[0], '1')))
        for j in range(1, len(s)):
            if s[0] != s[j]:
                n2 = int(s.replace(s[j], '0'))
                max_num = max(max_num, n1 - n2)
    return max_num

if __name__ == '__main__':
    n = int(input())
    print(ReplaceDigits(n))