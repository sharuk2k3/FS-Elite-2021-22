'''

Crazy Mohan is interested to disturb the order of the items.
There is a number N, each digit of the number is printed on a cube
and arranged accordingly in a row. Now, Crazy Mohan is allowed to swap 
the positions of the cubes, It is not allowed to add or remove the cubes.

You have to stop Crazy Mohan, when you find the new sequence of the cubes 
forms a new number W, such that W>N and W should be minimum.

If it is possible to form W from N, print the value of W, otherwise print '-1'

Input Format:
-------------
An integer N, given number.

Output Format:
--------------
Print an integer, the next nearest higher number.


Sample Input-1:
---------------
121

Sample Output-1:
----------------
211


Sample Input-2:
---------------
321

Sample Output-2:
----------------
-1



'''


def maximumSwap(num):
    nums = list(str(num))
    i = 0
    while i < len(nums)-1 and nums[i] >= nums[i+1]:
        i += 1
    if i == len(nums) - 1:
        return -1
    k = i
    for j in range(len(nums)-1, i, -1):
        if nums[j] > nums[k]:
            k = j
    for j in range(i+1):
        if nums[j] < nums[k]:
            break
    nums[j], nums[k] = nums[k], nums[j]
    return int(''.join(nums))
num=int(input())
print(maximumSwap(num))