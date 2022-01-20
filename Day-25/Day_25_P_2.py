'''
#BACKTRACKING PROBLEM


Pramod is working on Strings consist of digits only. He wants to findout, 
whether the given string can form Fibonacci sequence or not.

A String can form a Fibonacci Sequence, if it contains at least 
three numbers, and numbers are in the following order:
first, second, third  = first + second, fourth = third + second, .. so on.

Return true, if the given string can form fibonacci sequence,
otherwise, return false.

Note: Numbers in the fibonacci sequence contains no leading 0's.
for example, 2, 03,5 or 2,3,05 or 02,3,5 are not valid.

Input Format:
-------------
A String consist of digits only

Output Format:
--------------
Print a boolean value as result.


Sample Input-1:
---------------
23581321

Sample Output-1:
----------------
true

Explanation: 
------------
Fibonacci Sequence is : 2, 3, 5, 8, 13, 21
2, 3, 2+3=5, 3+5=8, 5+8=13, 8+13=21.

Sample Input-2:
---------------
199100199

Sample Output-2:
----------------
true

Explanation: 
------------
Fibonacci Sequence is : 1 99 100 199
1, 99, 1+99=100, 99+100=199.




'''

#SOLUTION BACKTRACK(Not Excatly)

def BackTrack(s,i,x,y,cnt=0):
    if i==len(s):
        return cnt>+3
    if s[i]=='0':
        return False
    current=""
    res=False
    for j in range(i,len(s)):
        current+=s[j]
        z=int(current)
        if x==-1 or y==-1 or x+y==z:
            res=res or BackTrack(s,j+1,y,z,cnt+1)
    return res
s=input()
if BackTrack(s,0,-1,-1):
    print("true")
else:
    print("False")
    

'''

#NAVIE SOLUTION

def Fibonacci(S):
    L, T, t = len(S), "", []
    for i in range(1,L-2):
        for j in range(1,L-i-1):
            if (i > 1 and S[0] == '0') or (j > 1 and S[i] == '0'): continue
            a, b = int(S[:i]), int(S[i:i+j])
            T, t = S[:i+j], [a,b]
            while len(T) < L:
                c = a + b
                T += str(c)
                t += [c]
                a, b = b, c
            if (len(T) == L and T == S and len(t) > 2 and t[-1] < 2**31 - 1): 
                return True
    return False
if __name__=="__main__":
    S=input()
    print(Fibonacci(S))
'''


