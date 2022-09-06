'''
Program-9:
=======
Given a integer n, number of elements and n integer elements, 
Find the index where the sum of elements left to that index is equal to sum of elements right to that index.
Example:
5
1 2 3 4 6
Output:
3
Explanation:
At index 3, left sum=1+2+3=6 and right sum=6.
'''

def equilibrium(arr):
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        if leftsum == total_sum:
            return i
        leftsum += num
    return -1
size=int(input())
arr=list(map(int,input().split()))
print(equilibrium(arr))