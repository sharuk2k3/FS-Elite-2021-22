'''
There are B bags containing N gold boxes each. In each bag, gold boxes are 
arranged  in ascending order of their weights strictly, create a method in 
such a way that we need to return the least weight of gold box which is 
common least weight in all the given bags.

If we don’t have any common least weighted gold box, among all the bags then return -1.

Input Format:
-------------
Line-1: Two integers B and N, number of bags and number of goldboxes in each Bag.
Next B lines: N space separated integers, weights of GoldBoxes.

Output Format:
--------------
Print the least weight of gold box, if found
Print -1, if not found.


Sample Input:
---------------
5 5
1 2 3 4 5
2 3 6 7 9
1 2 3 5 8
1 3 4 6 8 
2 3 5 7 8

Sample Output:
----------------
3
'''
#SOL 1 In O(N*2) Complexity

from itertools import chain as chn
from collections import Counter as cnt
def smallestCommonElement(mat):
    return min([k for k, v in cnt(chn(*mat)).items() 
    if v == len(mat)] or [-1])
n, m = map(int, input().split())
mat = []
for i in range(n):
    l = list(map(int, input().split()))
    mat.append(l)
if __name__=="__main__":
    print(smallestCommonElement(mat))

