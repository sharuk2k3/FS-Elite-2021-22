'''
Program-3:

Sam and Alex are playing a made-up game with numbers. The goal of the game is to make the array contain as 
many distinct elements as possible after performing some number of operations. In a single operation, Sam can choose 
any 3 elements from the array and remove the maximum and minimum among the three from the array. 
Determine the maximum number of elements remaining in the array when all of the elements are distinct.

Example:

n = 7
number = [1, 2, 4, 3, 2, 4, 3]

Output = 3
Constraints:
*  3 <= n <= 100000, and n is odd
*  1 <= number[i] <= 100000
The goal is to maximize the number of distinct elements in the final array, so ignore the 1 which is already distinct. 
Choose the triplet (2, 2, 3), 
remove the minimum and maximum elements, 2 and 3, then return the remaining 2 to the array. Now number' = [1, 4, 3, 2, 4]. 
Choose another triplet, (3, 4, 4), and 
remove the minimum and maximum values, then return the 4 to the array. Now number'' = [1, 2, 4], and all 3 elements are distinct. 
The maximum number of distinct elements possible is 3.
'''
from collections import defaultdict
n=int(input())
l = list(map(int, input().split()))
d = defaultdict(int)
for i in l:
    d[i] += 1
for i,j in d.items():
    if j >= 3:
        if j%2 == 0:
            d[i] = 2
        else:
            d[i] = 1
c = 0
t = 0
for i,j in d.items():
    if j == 2:
        c += 2
    t += j
    
if c%4 == 0:
    print(t-c//2)
else:
    print(t-c//2-1)