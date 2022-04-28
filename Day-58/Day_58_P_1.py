'''

Prasad is given a list of integers nums[].
He like odd numbers, so he wanted to form  
the odd length consecutive subsets possible.

Now your task is to help Prasad, to form the odd length subsets,
and to compute and print the sum of all such subsets.

Input Format:
-------------
Line-1: An integer N, number of integers.
Line-2: N space separated integers, nums[].

Output Format:
--------------
Print an integer, the sum.


Sample Input:
---------------
5
1 4 2 5 3

Sample Output:
----------------
58

Explanation:
------------
From the given list of integers, possible subsets are.
[1] = 1, [4] = 4, [2] = 2, [5] = 5, [3] = 3,
[1,4,2] = 7,	[4,2,5] = 11,	[2,5,3] = 10
[1,4,2,5,3] = 15
Finally, total sum is:  1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


'''

def sumOddLengthSubarrays(arr):
    size = len(arr)
    res = 0
    for i in range(size):
        tmp = 0
        j = 0
        while i + j < size:
            tmp += sum(arr[i:i + j + 1])
            j += 2
        res += tmp
    return res

n=int(input())
arr=list(map(int,input().split()))
print(sumOddLengthSubarrays(arr))