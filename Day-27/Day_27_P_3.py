'''

You are given a phrase and a paper of size m*n.
So you can type exactly m * n characters on that paper.
i.e,. there are 'm' rows and in each row you can type 'n' characters
You need to type the phrase on the paper with some rules.

The rules are as follows:
    - A word in the phrase cannot be split into two lines.
    - The order of words in the phrase shuld not change.
    - Two consecutive words in a line must be separated by a single space.

Your task is to find out how many times the phrase can be typed on the paper.


Constraint:
-----------
Length of each word is <=10.

Input Format:
-------------
Line-1: Three space separated integers m, n, and s, grid size m*n, number of words.
Line-2: 's' space separated strings, set of words

Output Format:
--------------
Print an integer, no.of times set of words fit into the grid.


Sample Input-1:
---------------
2 8 2
socail distance

Sample Output-1:
----------------
1

Explanation:
------------
social__
distance


Sample Input-2:
---------------
3 6 3
a bc def

Sample Output-2:
----------------
2

Explanation:
------------
a_bc__
def_a_
bc_def


'''

#Solution

def phrasePaper(n,m,sl,s):
    
    l = [["" for i in range(m)] for j in range(n)]

    c,p,length,q,f,leng = 0,0,0,0,0,0
    
    for i in range(n):
        for j in range(m):
            f = 0
            length = len(s[p])
            if m-j >= (length-leng):
                if q == length:
                    f = 1
                    p += 1
                    q = 0
                    leng = 0
                if p == sl:
                    c += 1
                    p = 0
                if not f:
                    l[i][j] = s[p][q]
                    leng += 1
                    q += 1
          
    length = len(s[-1])
    if "".join(l[-1][m-length:]) == s[-1]:
        c += 1
    print(c)

n, m, sl = map(int, input().split())
s = input().split()
print(phrasePaper(n,m,sl,s))


'''
def phrasePaper(s,a,b):
    n=a*b
    m=len(s)+1
    value=n//m
    return value
a,b,c=map(int,input().split())
s=input()
print(phrasePaper(s,a,b))
'''
