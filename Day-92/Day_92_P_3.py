'''
Pramod is planning to design a program, which helps to create 
the IP addresses posssible from a given string S, 
where each IP address should be valid.

It is guaranteed that S contains only digits.

Can you help pramod in designing such program, which returns all possible IP addresses.
Print the answer in lexicographic order.

NOTE:
-----

- A valid IP address consists of exactly four integers, 
each integer is between 0 and 255, separated by single dots 
and cannot have leading zeros
- IP Addresses are said to be valid if it falls in the range 
from 0.0.0.0 to 255.255.255.255

- IP addresses like [123.012.234.255 , 123.234.345.34] are invalid.

Input Format:
-------------
A string S, contains only digits [0-9].

Output Format:
--------------
Print all possible IP addresses which are valid.


Sample Input-1:
---------------
23323311123

Sample Output-1:
----------------
[233.233.11.123, 233.233.111.23]


Sample Input-2:
---------------
12345678

Sample Output-2:
----------------
[1.234.56.78, 12.34.56.78, 123.4.56.78, 123.45.6.78, 123.45.67.8]


Sample Input-3:
---------------
02550255

Sample Output-3:
----------------
[0.25.50.255, 0.255.0.255]
'''

#Solution:

def restoreIpAddresses(s):
    def restore(current, start, limit):
        if limit == 0:
            if (start == len(current)-1 or current[start] != '0') and int(''.join(current[start:])) <= 255:
                result.append(''.join(current))
        else:
            for i in range(start+1, start+4):
                if i < len(current) and int(''.join(current[start:i])) <= 255:
                    current.insert(i, '.')
                    restore(current, i+1, limit-1)
                    del current[i]
                    if current[start] == '0': break
                
    result = []
    restore(list(s), 0, 3)
    return result

if __name__ == '__main__':
    s=input()
    print(restoreIpAddresses(s))