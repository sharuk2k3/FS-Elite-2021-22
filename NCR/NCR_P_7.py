'''
Program-5:
=======
A person is attempting to break out of prison. The gate has N horizontal and M vertical bars. 
The area of each square box made when the bars intersect is 1*1=1
In order for the person to break out, few rods have to be removed. 
You are given the row and column numbers of the missing bars in the form of an array. 
Return the area of the biggest hole made when the bars are removed.

Input Format
N- Horizontal bars
M- Vertical bars
X- No. of horizontal bars removed
H [ ] - Array 
Y- No. of vertical bars removed
V [ ] - Array  

Sample Test Case 1
Input
3
3
1
2
1
2

Output
4
'''
'''
    Time Complexity: O(max( N, M))
    Space Complexity: O(max( N, M))

    Where N and M are the numbers of horizontal and vertical bars respectively.
'''
def breakThePrison(H , V, n, m, x, y):
    boolH = [True for i in range(n + 1)]
    boolV = [True for i in range(m + 1)]
    for i in range(x):
        boolH[H[i]] = False
    for i in range(y):
        boolV[V[i]] = False
    lh = 0
    gh = -1
    lv = 0
    gv = -1
    for i in range(1, n + 1):
        if(boolH[i]):
            lh = 0
        else:
            lh += 1
            gh = max(lh, gh)
    for i in range(1, m + 1):
        if(boolV[i]):
            lv = 0
        else:
            lv += 1
            gv = max(lv, gv)
    return (gh + 1) * (gv + 1)

n=int(input())
m=int(input())
x=int(input())
H=list(map(int,input().split()))
y=int(input())
V=list(map(int,input().split()))
print(breakThePrison(H , V, n, m, x, y))