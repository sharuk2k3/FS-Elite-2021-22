'''

Bunny is playing with binary strings. He wants to break
a binary string B into 3 parts, of length atleast '1',
when we merge the 3 parts will result the string B.

Your task is to find the count the various forms to break 
the Binary String B into 3 parts, where each part should 
contain equal number of 1's.


Input Format:
-------------
A string S.

Output Format:
--------------
Print an integer, count the various forms to break.


Sample Input-1:
---------------
01010010

Sample Output-1:
----------------
6

Explanation:
------------
There are six forms to break S into 3 parts 
where each part contain the equal number of  1's.
01 | 01 | 0010
01 | 010 | 010
01 | 0100 | 10
010 | 1 | 0010
010 | 10 | 010
010 | 100 | 10


Sample Input-2:
---------------
010010

Sample Output-2:
----------------
0


'''

#Solution:

def split_string(s):
    n = len(s)
    ss = s.split("1")
    ones = len(ss)-1
    if ones % 3 != 0:
        return 0
    if ones == 0:
        return ((n-1)*(n-2)//2) % (10**9+7)
    return ((len(ss[ones//3])+1) * (len(ss[ones//3*2])+1)) % (10**9+7)
    
s=input()
print(split_string(s))