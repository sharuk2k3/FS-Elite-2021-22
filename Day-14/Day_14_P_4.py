'''

You are given a list of N integers List[], list contains both +ve and -ve integers.
Your task is to findout, the Highest Product possible,
Where the product is the product of all the elements of contiguous sublist sList[],
and sublist should conatin atleast 1 integer.

Input Format:
-------------
Line-1: An integer N.
Line-2: N space separated integers, List[].

Output Format:
--------------
Print an integer output, the highest product.

Sample Input-1:
---------------
4
2 3 -2 4

Sample Output-1:
----------------
6

Explanation:
------------
Product of contiguous sub list [2,3].


Sample Input-2:
---------------
3
-2 0 -3

Sample Output-2:
----------------
0

Explanation:
------------
Product of sub list [0], where [-2,-3] is not a contiguous sublist


'''

#SOLUTION

def Product(n,l):
    min_val, max_val, res = l[0], l[0], l[0]
    for i in range(1, len(l)):
        temp_min, temp_max = min_val, max_val
        max_val = max(l[i]*temp_max, l[i]*temp_min, l[i])
        min_val = min(l[i]*temp_max, l[i]*temp_min, l[i])
        res = max(res, max_val)
    return res
    
if __name__=="__main__":
    n=int(input())
    l=list(map(int,input().split()))[:n]
    print(Product(n,l))