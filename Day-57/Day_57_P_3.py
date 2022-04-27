'''


Ashok is given a list of integers nums[].
His task is to find the longest contiguous sublist of S, 
the product of all the numbers in the sublist should be positive.

Your task is to return the length of longest contiguous sublist.

Input Format:
-------------
Space separated integers nums[], list of numbers.

Output Format:
--------------
Print the length of the longest contiguous sublist


Sample Input-1:
---------------
1 -1 2 -2

Sample Output-1:
----------------
4


Sample Input-2:
---------------
-1 -2 -3 0 1

Sample Output-2:
----------------
2

Explanation:
------------
0 is not considered as positive number.


Sample Input-3:
---------------
1 2 3 4 -5 6  7 8

Sample Output-3:
----------------
4



'''

def Array(nums):
    ans = neg = pos = 0
    for x in nums:
        if x > 0:
            if neg > 0:
                neg += 1
            pos += 1
        elif x < 0:
            neg, pos = pos+1, (neg+1 if neg else 0)
        else:
            neg = pos = 0
        ans = max(ans, pos)
    return ans

nums=list(map(int,input().split()))
print(Array(nums))