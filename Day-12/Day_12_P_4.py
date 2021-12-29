'''
Clavius, the person who suggested grouping of data using brackets.
He has suggested that the grouping should be well formed.
Well formed groupings are as follows, (), [], {}, {()}, {[]()}, {[]}(), etc.

You will be given a string S, return true if the string S is a well formed 
grouping, otherwise false.

Note: S contains only characters ( ) [ ] { }

Input Format:
-------------
A string S, contains only characters (){}[]

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
{[([])[]]}

Sample Output-1:
----------------
true

Sample Input-2:
---------------
{[([])[]}]

Sample Output-2:
----------------
false
'''

#SOLUTION

def Valid(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []
if __name__=="__main__":
    s=input()
    print(Valid(s))
    


