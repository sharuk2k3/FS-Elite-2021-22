"""

Marripalem Obul (Mario) is playing with a numeric string.
The string S consists only two digits in it 1 and 2.
The string has following properties:
	- The first few digits in the string as follows: 
	    "1221121221221121122......"
	- The string is originally formed as follows:
		1 22 11 2 1 22 1 22 11 2 11 22 ......
	and the count of '1's or '2's in each consecutive groups are:
		1 2 2 1 1 2 1 2 2 1 2 2 ......
	the count sequence above is in the string S itself.

You are given an integer L, Your task is to help Mario to find and print
the number of '1's in the substring of S of length L from index-0.

Note: L will not exceed 100,000.

Input Format:
-------------
An integer L

Output Format:
--------------
Print an Integer.


Sample Input-1:
---------------
7

Sample Output-1:
----------------
4

Explanation:
------------
The sustring of length 7 is "1221121".The count of 1's is 4.


Sample Input-2:
---------------
12

Sample Output-2:
----------------
5

Explanation:
------------
The sustring of length 12 is "122112122122".The count of 1's is 5.



"""

#Solution:



def NamunaString(n):
    s = ['1', '2', '2']
    for i in range(2, n):
        add_two = s[-1] == '1'
        s.extend(list(int(s[i]) * ('2' if add_two else '1')))
        if len(s) >= n: break 
    return s[:n].count('1')

if __name__=="__main__":
    n=int(input())
    print(NamunaString(n))

