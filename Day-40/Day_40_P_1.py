'''

Babylonians invented multiplication of numbers.

You will be given two strings consist of digits only.
You have to perform the multiplication of these two strings using 
Babylonians approach, and return the result of multiplication of two strings.


Input Format:
-------------
Two space separated strings, num1 and num2.

Output Format:
--------------
Print the product of two strings num1 and num2.


Sample Input-1:
---------------
5 4 

Sample Output-1:
----------------
20


Sample Input-2:
---------------
121 432 

Sample Output-2:
----------------
52272

Note:
-----
	- Input should contain digits only, and should not contain leading 0's 
	  except number 0.
	- Output will be in the range of integer only.
	- There will be no leading minus '-' symbol also.
	- Should not use built-in BigInteger library.
	- Should not convert the given strings into integers.


'''
#LOL SOLUTION

def main():
    num1, num2 = input().split()
    ans1=0 ; ans2=0 
    for d in num1: ans1=ans1*10+(ord(d)-ord('0'))
    for d in num2: ans2=ans2*10+(ord(d)-ord('0'))
    print(str(ans1*ans2))
    
main()