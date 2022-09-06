'''
Program-6:
========
Given an array of integers, the task is to print the array in the order – smallest number, the Largest number, 
2nd smallest number, 2nd largest number, 3rd smallest number, 
3rd largest number and so on….. 
Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
Output :arr[] = {1, 9, 2, 8, 3, 7, 4, 6, 5}

Input : arr[] = [1, 2, 3, 4]
Output :arr[] = {1, 4, 2, 3}
ments are distinct. The maximum number of distinct elements possible is 3.
'''
def rearrangeArray(arr, n):
    a = []
    arr.sort()
    i = 0
    j = n-1
    while (i<j):
        a.append(arr[i])
        i += 1
        a.append(arr[j])
        j -= 1
    if n%2!=0:
        a.append(arr[i])
    arr[:] = a

arr = [ 1,2,3]
n = len(arr)
rearrangeArray(arr, n)

for i in range(0, n) :
	print( arr[i], end = " ")
 

