'''


Somesh is working on Number Strings.
He got an idea to find the smallest possible number by 
deleting some digits from the number without changing 
the relative order of digits in it.

You will be given a integer String 'num', and an integer n.
Find the smallest number possible after deleting n digits from 'num'.

Note: If the number string 'num' turns to empty, print 0.

Input Format:
-------------
Line-1 : A string num, consist of digits only.
Line-2 : An integer n, number of digits to delete.

Output Format:
--------------
Print the smallest possible number.


Sample Input-1:
---------------
1432219
3

Sample Output-1:
----------------
1219

Explanation: 
------------
Delete the three digits 4, 3, and 2 to form the smallest number 1219.


Sample Input-2:
---------------
10200
1

Sample Output-2:
----------------
200

Explanation:
------------
Delete the leading 1 and the smallest number is 200. 
Note that the output must not contain leading zeroes.



'''

def removedigits(num, k):
    stack = [num[0]]
    if len(num) == 1:
        return '0'
        
    for i in range(1, len(num)): 
        while stack and int(stack[-1]) > int(num[i]) and k:
            stack.pop()
            k -= 1
        stack.append(num[i])
            
    while k:
        k -= 1
        stack.pop()
            
    stack = ''.join(stack)
    return str(int(stack)) if stack else '0'

num=input()
k=int(input())
print(removedigits(num, k))