'''

In a shopping mall, there is a Lift with a capacity of 500kgs only.
There are N persons waiting for the lift, and their weights (weights[]) are given.
If The Lift is overloaded, it will not move.
 
Your task is to find out the maximum number of persons can use the Lift,
without any overloading issue.

Input Format:
-------------
Line-1: An integer N, number of persons
Line-2: N space separated integers, weights of the persons.

Output Format:
--------------
Print an integer, max num of persons can use the lift.


Sample Input-1:
---------------
6
98 121 76 135 142 65

Sample Output-1:
----------------
5


Sample Input-2:
---------------
7
85 67 69 83 54 61 50

Sample Output-2:
----------------
7



'''


#SOLUTION

def MaxLiftLoad(n,weights):
    sum, c = 0, 0
    weights.sort()
    for i in weights:
        sum = sum + i
        if sum <= 500:
            c = c + 1
    return c
if __name__=="__main__":
    n=int(input())
    weights=list(map(int,input().split()))[:n]
    print(MaxLiftLoad(n,weights))