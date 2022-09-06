'''
Program-10
========
Given two integers N and B, the task is to print the maximum index a pointer, 
starting from 0th index can reach in an array of natural numbers(i.e., 0, 1, 2, 3, 4, 5…), 
say arr[], in N steps without placing itself at index B at any point.
Jumping Index = Current Index + Step Number
Input: N = 3, B = 2
Output: 6

Step 1:
Current Index = 0
Step Number = 1
Jumping Index = 0 + 1 = 1

Step 2:
Current Index = 1
Step Number = 2
Jumping Index = 1 + 2 = 3

Step 3:
Current Index = 3
Step Number = 3
Jumping Index = 3 + 3 = 6
Therefore, the maximum index that can be reached is 6.
'''

def maximumIndex(N, B):
    max_index = 0
    for i in range(1, N + 1):
        max_index += i
    current_index = max_index
    step = N
    while (1):
        while (current_index > 0 and N > 0):
            current_index -= N
            if (current_index == B):
                current_index += N
            N -= 1
        if (current_index <= 0):
            return max_index
            #print(max_index)
            break
        else:
            N = step
            current_index = max_index - 1
            max_index -= 1
            if (current_index == B):
                current_index = max_index - 1
                max_index -= 1

N = int(input())
B = int(input())
print(maximumIndex(N, B))