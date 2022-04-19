'''


Mohith and Rohith are good friends, They are used to chatting very often.
Mohith is lazy to type the complete word, so he finds a way to shorten the words.
For example, if the original word is "banana", he types it as "ba2[na]".

Can you help Rohith, to find the original word from the shortened word 
he received from Mohith.

NOTE: 
- You may assume that the original word is always valid and does not 
  contain any digits. 
- No white spaces. The brackets are well-formed.

Input Format:
-------------
A String, a word given by Mohith, contains brackets [], and alphabets and digits

Output Format:
--------------
A string, the original word.


Sample Input-1:
---------------
ba2[na]

Sample Output-1:
----------------
banana


Sample Input-2:
---------------
3[3[sa]2[ri]]

Sample Output-2:
----------------
sasasaririsasasaririsasasariri



'''

def stackIt(s):
    stack = []
    for i in s:
        if i == '[':
            stack.append(i)
        elif i == ']':
            stack.pop()
    return stack == []
    

s=input()
stackIt(s)