'''

A string is called well-weighted string,if and only if
the string has equal number of 'A's and 'B's in it.

You are given a string S, divide S in to the maximum number of well-weighted 
strings. You should not leave any letter/part of the string.
Return the maximum number of well-weighted strings.

Input Format:
-------------
A string contains only A's and B's

Output Format:
--------------
Print an integer, maximum number of well-weighted strings


Sample Input-1:
---------------
ABBBBAAABA

Sample Output-1:
----------------
3

Explanation:
--------------
Well weighted strings, AB, BBBAAA, BA.


Sample Input-2:
---------------
ABAABBABAB

Sample Output-2:
----------------
4

Explanation:
--------------
Well weighted strings, AB, AABB, AB, AB.


Sample Input-3:
---------------
ABAAABBABB

Sample Output-3:
----------------
2


'''

#Solution
'''
def wellWeighted(s):
    a,b=0,0
    for i in s:
        if i=='A':
            b=b+1
        elif i=='B':
            b=b-1
        if b==0:
            a=a+1
    return a
s=input()
print(wellWeighted(s))
'''
#Using Stack

lst=list(input())
count=-1
stack=[]
for i in range(len(lst)):
    if(len(stack)==0):
        count=count+1
        stack.append(lst[i])
    elif(stack[-1]==lst[i]):
        stack.append(lst[i])
    else:
        stack.pop(-1)
if(len(stack)==0):
    count=count+1
print(count)