'''

There is a board with M*N size. 
The board contains M*N blocks of 1*1 size.
Each block is printed a number on it.

You will be given a number, your task is to find whether the number is printed on 
any of the blocks or not. If found print true, otherwise print false.

NOTE: 
- The numbers printed on the board in each row are in increasing order. 
- Next row starting number is greater than the last number of the previous row.

Constarint:
-----------
Can you solve it in log(M)+ log(N) time. 


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
12 15 19 23
24 28 32 36
37 41 44 47
15

Sample Output-1:
----------------
true


Sample Input-2:
---------------
4 4
1 3 6 10
12 15 19 23
24 28 32 36
37 41 44 47
26

Sample Output-2:
----------------
false


case =1
input =5 5
1 4 7 11 15
22 25 28 32 39
43 46 49 56 62
70 73 74 77 84
88 91 93 96 99
73
output =true

case =2
input =5 5
1 4 7 11 15
22 25 28 32 39
43 46 49 56 62
70 73 74 77 84
88 91 93 96 99
79
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
19 22 27 29 31 33 35 37
44 48 50 56 61 63 65 67
68 76 82 88 92 96 99 101
110 118 124 130 134 138 140 142
67
output =true

case =6
input =5 8 
1 3 5 7 9 11 13 15
19 22 27 29 31 33 35 37
44 48 50 56 61 63 65 67
68 76 82 88 92 96 99 101
110 118 124 130 134 138 140 142
135
output =false

case =7
input =8 8
1 4 7 11 15 18 19 22
23 25 27 31 34 37 40 45
46 48 50 53 56 59 63 69
70 73 76 79 82 83 87 94
104 108 109 112 113 116 118 120
122 125 127 129 135 137 138 139
142 144 146 148 151 155 159 166
173 175 177 185 188 192 195 199
142
output =true

case =8
input =8 8
1 4 7 11 15 18 19 22
23 25 27 31 34 37 40 45
46 48 50 53 56 59 63 69
70 73 76 79 82 83 87 94
104 108 109 112 113 116 118 120
122 125 127 129 135 137 138 139
142 144 146 148 151 155 159 166
173 175 177 185 188 192 195 199
66
output =false




'''

#SOLUTION

def searchMatrix( matrix, target): 
    def search_row(row, target):
        l, r = 0, len(row)-1
        while l <= r:
            mid = l + (r-l) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                r = mid-1
            else:
                l = mid+1    
        return False
    row_index = 0
    l , r = 0, len(matrix)-1
    while l <= r:
        mid = l + (r-l) // 2
        if matrix[mid][0] == target:
            return True
        if matrix[mid][0] < target:
            row_index = mid 
            l = mid+1
        else:
            r  = mid-1                            
    return search_row(matrix[row_index], target)


r,c=map(int,input().split())
matrix=[]
for i in range(r):         
    row = list(map(int, input().split()))
    matrix.append(row)
target=int(input())
if __name__=="__main__":
    ans = searchMatrix(matrix,target)
    if ans:
        print("true")
    else:
        print("false")
        


