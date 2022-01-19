'''

Ramesh and Suresh are best friends. 
They decided to play a word game.

The game rules are as follows:
	- The game board shows a word W consist of two characters only A and B.
	- You are allowed to replace a pair of neighbour letters AA with BB in W.
	- Finally, The one who failed to replace the letters will lose the game.

You can assume that Ramesh will start playing the game always.

Your task is to determine if Ramesh can guarantee a win.
Print 'true', if Ramesh guarantee a win, otherwise, print 'false'.

Input Format:
-------------
A string W, word.

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
AAABAAAA

Sample Output-1:
----------------
true

Explanation:
------------
Given word is AAABAAAA 
Ramesh -> AAABBBAA 
Now whatever the pair Suresh replaced with BB, 
one more replace is possible for Ramesh
So, there is a guarantee for Ramesh to win.

Sample Input-2:
---------------
AAAAAA

Sample Output-2:
----------------
true


Sample Input-3:
---------------
AAABAAA

Sample Output-3:
----------------
false



'''

#SOLUTION

#BACK TRACKING 6/8 passed
def rep(i, n, c, s):
    
    if i >= n:
        if c%2 != 0:
            if "AA" in s:
                return False
            return True
        return

    if i+1 < n:
        if s[i] == s[i+1] == 'A':
            s = s[:i] + "BB" + s[i+2:]
            if rep(i+2, n, c+1, s):
                return True
            s = s = s[:i] + "AA" + s[i+2:]
        if rep(i+1, n, c, s):
            return True
        
    else:
        if rep(i+1, n, c, s):
            return True

s = input()
if rep(0, len(s), 0, s):
    print("true")
else:
    print("false")

'''
NAVIE
7/8 cases passed
s = input()
c = 0
for i in range(len(s)-1):
    if s[i] == s[i+1] == 'A':
        c += 1
        i += 2
    else:
        i += 1
if c%2 != 0:
    print('true')
else:
    print('false')


'''