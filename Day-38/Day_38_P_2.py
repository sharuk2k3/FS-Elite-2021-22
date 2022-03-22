'''

For this challenge, a substring is defined as any contiuous group of one or more 
characters of a string. For example, the unique substrings of "baca" are [b, ba, 
bac, baca, a, ac, aca, c ,ca] . The list in alphabetical order is [a, ac, aca, b, 
ba, bac, baca, c, ca]. in this case, the maximum substrin, alphabetically, is 'ca'.

Given a string s, determine its maximum substring.

Your task is to design a function, that return the maximum substring of s.

NOTE:
String s contains only lowercase alphabets.

Input Format:
-------------
A string, s

Output Format:
--------------
print a string, maximum substring.


Sample Input-1:
---------------
baca

Sample Output-1:
----------------
ca


Sample Input-2:
---------------
banana

Sample Output-2:
----------------
nana



'''


#Solution:
def main(s,n):
    max_substring=''
    for i in range(n):
        for j in range(i,n):
            if s[i:j+1]>max_substring:
                max_substring=s[i:j+1]
    print(max_substring)

s=input()
n=len(s)
main(s,n)