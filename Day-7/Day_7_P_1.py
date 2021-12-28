'''

There is a board with M*N size. 
The board contains M*N blocks of 1*1 size.
Each block is printed a number on it.

You will be given a number, your task is to find whether the number is printed on 
any of the blocks or not. If found print true, otherwise print false.

NOTE: 
- The numbers printed on the board in each row and each column are
  in increasing order. And all the numbers are unique.

Input Format:
-------------
Line-1 -> Two integers M and N, board size.
Next M lines -> N space separated integers.
Last Line -> An integer T, number to search.

Output Format:
--------------
Print a boolean value, 'true' if number found.
otherwise, 'false'.


Sample Input-1:
---------------
4 4
1 3 6 10
2 5 9 13
4 8 12 16
7 11 14 17
5

Sample Output-1:
----------------
true


Sample Input-2:
---------------
4 4
1 3 6 10
2 5 9 13
4 8 12 16
7 11 14 17
15

Sample Output-2:
----------------
false


case =1
input =5 5
1 4 7 11 15
2 5 8 12 19
3 6 9 16 22
10 13 14 17 24
18 21 23 26 30
5
output =true

case =2
input =5 5
1 4 7 11 15
2 5 8 12 19
3 6 9 16 22
10 13 14 17 24
18 21 23 26 30
20
output =false

case =3
input =6 7
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28 
29 30 31 32 33 34 35
36 37 38 39 40 41 42
25
output =true

case =4
input =6 7
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28 
29 30 31 32 33 34 35
36 37 38 39 40 41 42
48
output =false

case =5
input =5 8 
1 3 5 7 9 11 13 15
2 12 17 19 21 23 25 27
4 14 20 26 31 33 35 37
8 16 22 28 32 36 39 41
10 18 24 30 34 38 40 42
36
output =true

case =6
input =5 8 
1 3 5 7 9 11 13 15
2 12 17 19 21 23 25 27
4 14 20 26 31 33 35 37
8 16 22 28 32 36 39 41
10 18 24 30 34 38 40 42
6
output =false

case =7
input =8 8
11 14 17 21 25 28 29 32
13 25 27 31 34 37 40 45
15 26 30 35 38 41 46 51
20 33 36 39 42 43 47 54
44 48 49 52 53 56 58 60
50 55 57 59 65 72 78 83
62 64 66 68 71 75 79 86
53 73 74 85 88 92 95 99
71
output =true

case =8
input =8 8
11 14 17 21 25 28 29 32
13 25 27 31 34 37 40 45
15 26 30 35 38 41 46 51
20 33 36 39 42 43 47 54
44 48 49 52 53 56 58 60
50 55 57 59 65 72 78 83
62 64 66 68 71 75 79 86
53 73 74 85 88 92 95 99
76
output =false



'''

#SOLUTION
def CheckElement(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    for x in range(m):
        if matrix[x][0] <= target:        
            left = 0
            right = n-1
            while left<=right:
                mid = (left + right)//2
                if matrix[x][mid] == target:
                    return True
                if matrix[x][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            break
    return False
        
r,c=map(int,input().split())
matrix=[]
for i in range(r):         
    row = list(map(int, input().split()))
    matrix.append(row)
target=int(input())
if __name__=="__main__":
    ans = CheckElement(matrix,target)
    if ans:
        print("true")
    else:
        print("false")

