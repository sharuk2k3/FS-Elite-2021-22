"""

Max Funds
Problem Description
An NGO wants to arrange funds for flood relief. It has divided volunteers into groups. A volunteer can only be a part of single group. Your task is to find the maximum funds collected by a group.

You will be given the funds collected by each volunteer and grouping pairs of the volunteers. You need to group the volunteers through these pairs.

Constraints
0 < N, P <= 10000

0 < A, B <= N

Input
First line contains one integer N, denoting number of volunteers.

Second line contains N space separated integers, representing the amount collected by each volunteer. The index of integer is the volunteer number starting from 1.

Third line contains the number of pairs, P.

Next P lines contain two space separated integers, A and B where A represents the first person and B represents the second person in the pair.

Output
One line containing an integer, representing the maximum funds collected by the group.

Time Limit
2

Examples
Example 1

Input

5

23 43 123 54 2

3

1 3

2 3

1 2

Output

189

Explanation

In the above example, we have five volunteer [1, 2, 3, 4, 5] who have collected [23, 43, 123, 54, 2] respectively.

We have three groups that consists of [1, 2, 3], [4], [5]. First group collects 189 units of money, second group collects 54 units of money and third group collects 2 units of money. The maximum funds collected by any group is 189. Hence, the output is 189

Example 2

Input

9

34 54 65 76 88 23 56 76 43

7

1 3

2 3

1 2

6 8

5 4

5 7

8 9

Output

220

Explanation

In the above example, we have three groups that consists of [1, 2, 3], [4, 5, 7], [6, 8, 9]. Each group collects 153, 220, 142 units of money respectively. The maximum funds collected by a group is 220. Hence the output is 220.

"""

#SOLUTIONS

def main(n,a,p):
    return(max(max(a[pairs[i][0]-1] + a[pairs[i][1]-1] for i in range(p)) for _ in range(n)))

n = int(input())
a = list(map(int, input().split()))
p = int(input())
pairs = []
for _ in range(p):
        pairs.append(list(map(int, input().split())))
print(main(n,a,p))
