'''

Murali playing a mobile game, Blast the letters.

In the game he is given a word W and value R.
Murali has to perform the blasting operation as follows:
	- He has to blast the mimeograph M of length R in W, 
	  a mimeograph is a string such that each letter in it should be same.
	- After blasting the mimeograph, the rest of the string on its
	  left side and right side, concatenated together.

Murali has to perform the blasting operation repeatedly, 
until no more blasting is possible. Your task is to return 
the final string after all the blast operations have been done.

Input Format:
-------------
Line-1: A string and an integer, W and R.

Output Format:
--------------
Print a string, the final string after all the blast operations have been done.


Sample Input-1:
--------------- 
ababbaaab 3

Sample Output-1:
----------------
aba


Sample Input-2:
--------------- 
caaabbbaacdddd 2

Sample Output-2:
----------------
cabc


'''

#SOLUTION

def BlastWords(W, R):
    stack = []
    ans = ''
        
    if len(W) <= R:
        return W
        
    for i in W:
        if stack and  stack[-1][0] == i:
            if stack[-1][1] == R-1:
                stack.pop()
            else:
                stack[-1][1] += 1
        else:
            stack.append([i, 1])
        
    for j in stack:
        ans += j[0] * j[1]
        
    return ans

W, R = input().split()
R=int(R)
print(BlastWords(W,R))