"""
Program-11:
========
Given an integer n, number of cars in a parking lot. A list of integers representing the position of the cars and an integer k, the number of cars need to be considered for a single rope. 
Find the minimum length of rope need to be used required to cover k cars.
Example:
Input:
5
2 15 6 20 7
3

Output:
6
"""

def min_rope_length(k, nums):
    if k > len(nums):
        return 0
    result= pow(2,32)
    nums.sort()
    for i in range(0,len(nums)-k+1):
        size = nums[i+k-1] - nums[i] + 1
        result = min(result, size)
    return result
    
nums=[2,15,6,20,7]
k=3
print(min_rope_length(k, nums))