'''
In a construction site, there are M buildings planned to build.

The construction company got a unique idea, such that all the buildings will be 
constructed in a row. Each building must be one floor more than its previous.

Assume that he planned to build from i-floors building and consecutively
i, i+1, i+2, i+3,.. so on.

You will be given the number of floors of each building in the row as an array
buildings[], And an integer P, and few buildings missed according to the plan.

Your task is to find the P-th missing building with starting from first building
to the N floors building in that row, and print the number of floors of the building.


Input Format:
-------------
Line-1: Two space separated integers, M and P
Line-2: M space separated integers, buildings array.

Output Format:
--------------
Print an integer, P-th missing building in the order.


Sample Input-1:
---------------
5 3
3 5 6 8 10

Sample Output-1:
----------------
9

Explanation:
------------
The starting building has 3 floors.
Then, the order of the buildings should be 3,4,5,6,7,8,9,10.
The missed buildings are: 4,7,9,11,...
So, 3rd missing building has 9 floors.

Sample Input-2:
---------------
6 2
1 2 4 6 8 9

Sample Output-2:
----------------
5

'''

def missingNumber(arr, k):
    s = 0
    e = len(arr)-1
    ans = 0
    while(s<=e):
        mid = (s+e)//2
        if(arr[mid]-(mid+1)<k):
            ans = mid+1
            s = mid+1
        else:
            e = mid-1
    return k+ans
if __name__ == '__main__':
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(missingNumber(arr,k))