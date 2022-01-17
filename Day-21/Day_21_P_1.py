'''

Aziz is given a set of integers SOI[], consists of both +ve and -ve integers.

Aziz wants to find the maximum sum of contiguous subset of the SOI, with a twist.

You have to perform the following operation before finding the maximum sum:
- You are allowed to replace exactly one integer X, with its square value (X*X).

Can you please help Aziz to find out the maximum sum of contiguous subset.


Input Format:
-------------
Single line of space separated integers, values of the array.

Output Format:
--------------
Print an integer value as result.


Sample Input-1:
---------------
-5 -3 1 2 -3 4 -4 3

Sample Output-1:
----------------
26

Explanation:
------------
max sum is: (-5)^2 + (-3) + 1 + 2 + (-3) + 4 = 26


Sample Input-2:
---------------
2 -2 2 2 -2 -2 2

Sample Output-2:
----------------
10

Explanation:
------------
max sum is: 2 +(-2)^2 + 2 + 2 = 10


'''

#SOLUTION

def maxSum(l):
    prev_with_square = prev_without_square = 0
    ans = 0
    for i in l:
        without_square = max(i, i+prev_without_square)
        with_square = max(i*i, i*i+prev_without_square, i+prev_with_square)
        ans = max(ans, with_square)
        prev_with_square, prev_without_square = with_square, without_square
    return ans
    
if __name__=="__main__":
    l=list(map(int,input().split()))
    print(maxSum(l))