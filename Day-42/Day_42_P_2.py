'''

You are given a square box with square cubes in it.
Each cube of size 1*1*1, and colored with either yellow or blue.
yellow cube represented by 1 and blue cube represented by 0.

In one operation, You can choose any two adjacent horizontal lines of cubes in 
the box and swap them. The box is said to be diagonal box, if all the square 
cubes above the main diagonal are blue colored.

Your task is to find the the minimum number of operations needed to arrange 
the box as diagonal box , if it is not possible to arrange return  -1.

The main diagonal of a box is the diagonal that starts at cube (0, 0) and
ends at cube (n-1, n-1) .

Input Format:
-------------
Line-1: An integer, N size of the box.
Next N lines: N space separated integers, colors of the cubes in the box.

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
3
0 1 0
1 0 1
1 0 0

Sample Output-1:
----------------
2

Explanation:
------------
Please do look at the Hint.


Sample Input-2:
---------------
4
1 1 0 0
1 0 1 0
0 1 0 0
1 0 1 0

Sample Output-2:
----------------
-1


'''
def diagonal_box(box):
    
    n = len(box)
    for i in range(1, n):
        if box[i][i] != 0:
            return False
    return True



if __name__ == '__main__':
    n = int(input())
    b = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print