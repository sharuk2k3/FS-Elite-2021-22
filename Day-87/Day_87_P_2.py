'''

Subodh is interested in playing with Strings,
For a given String 'S', Subodh applies some rules to find the value of 'S'.
The rules are as follows:
	- If it is a balanced () has value 1
	- XY has value X + Y , where X and Y are balanced () strings.
	- (Z) has score 2 * Z , where Z is a balanced parentheses string.
	
Find out the value of given String and print it.

Note: All the given strings are balanced

Input Format:
----------------
A String contains only '(', ')'


Output Format:
------------------
Print an integer as result.


Sample Input-1:
-------------------
()

Sample Output-1:
---------------------
1

Sample Input-2:
-------------------
(())

Sample Output-2:
---------------------
2

Sample Input-3:
-------------------
(()(()))

Sample Output-3:
---------------------
6



'''

#Solution:

#Using Stack

def braces(s) :
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack[-1] == "(" and i == ")":
            stack.pop()
            stack.append(1)  
        else:
            count = 0
            while stack[-1] != "(":
                count += stack.pop()
            if(stack[-1] == "("):
                stack.pop()
                stack.append(count*2)
    return sum(stack)

if __name__ == '__main__':
    s=input()
    print(braces(s))