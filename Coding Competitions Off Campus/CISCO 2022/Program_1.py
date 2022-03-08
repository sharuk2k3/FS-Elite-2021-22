'''

#CISCO EXAM OFF CAMPUS

1. Largest square possible
Given an array of N integers where each number a[x] indicates a stack of cubical bricks of height a[x]. Essentially the array represents N stacks of bricks. The goal is to determine the largest n x n matrix (square matrix) embedded in this array of stacks.

 

Input format:

First line indicates the size of the integer array say N

Each of the next N lines represent the height of the stack at index x where 1 <= x <= N

 

Constraints:

1 <= N < 10ˆ4

0 <= x < 10ˆ4

 

Output:

Value of n where n x n matrix is the largest one embedded in the stacks.


Example:
Input 1 :

3

5

4

3

 

Output 1 :

3

 

Explanation 1 :

The array can be viewed as follows.



The largest n x n matrix possible is a 3 x 3 matrix as highlighted in yellow. Hence the answer is 3.

Input 2  :

5

3

2

4

2

3

 

Output 2 :

2


Explanation 2 :
The array can be viewed as follows.


The largest n x n matrix possible is a 2 x 2 matrix. One of such matrix is color coded in yellow. Hence the answer is 2.

 

'''

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
a=max(arr)
res=min(arr,n)