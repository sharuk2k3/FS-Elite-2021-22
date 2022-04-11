'''

AlphaCipher is a string formed from another string by rearranging its letters

You are given a string S.
Your task is to check, can any one of the AlphaCipher is a palindrome or not.

Input Format:
-------------
A string S

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
carrace

Sample Output-1:
----------------
true


Sample Input-2:
---------------
code

Sample Output-2:
----------------
false



'''

#Solution
def AlphaCipher(s):
    l = []
    for i in range(len(s)):
        if (s[i] in l):
            l.remove(s[i])
        else:
            l.append(s[i])
    if (len(s) % 2 == 0 and len(l) == 0 or (len(s) % 2 == 1 and len(l) == 1)):
        return True
    else:
        return False
s=input()
print(AlphaCipher(s))
