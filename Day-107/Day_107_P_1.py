'''

Birbal is creating a new binary code system BBC (Birbal Binary Code) as follows:

I	f(I)
-------
0	""
1	"0"
2	"1"
3	"00"
4	"01"
5	"10"
6	"11"
7	"000"

You are given an integer value I, where I is positive number.
Your task is to find BBC representation of  the given number I.

Input Format:
-------------
An integer I

Output Format:
--------------
Print the BBC representation of I.


Sample Input-1:
---------------
23

Sample Output-1:
----------------
1000


Sample Input-2:
---------------
45

Sample Output-2:
----------------
01110


'''

from collections import defaultdict


def numRep(n):
    n=list(n)
    d=defaultdict(list)
    d={
    '0':'',
    '1':'0',
    '2':'1',
    '3':'00',
    '4':'01', 
    '5':'10',
    '6':'11',
    '7':'000'
    }
    

if __name__ == '__main__':
    n=input()
    print(*numRep(n))
