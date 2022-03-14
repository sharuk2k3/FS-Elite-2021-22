'''

Kiran is playing with strings and its subsequences.
A subsequence can be formed from a string by deleting some characters
(may be string itself)

Kiran has given two strings S and T, your task to form T by concatenating 
the subsequences of S  

Return the minimum number of subsequences required to form T.
If the task is impossible, return -1 .


Input Format:
-------------
Line-1 -> Two strings S and T

Output Format:
--------------
Print an integer as result.


Sample Input-1:
---------------
abc abcbc

Sample Output-1:
----------------
2

Explanation:
------------
T = "abcbc" can be formed by "abc" and "bc",
which are subsequences of S = "abc".


Sample Input-2:
---------------
abc acdbc

Sample Output-2:
----------------
-1

Explanation: 
------------
string T cannot be constructed from the
subsequences of string S due to the character "d" in string T.


'''

def subsequence_string(s,t):
    res,j,k = 0,0,-1
    while True:
        if j >= len(t):
            return res
        if k == j:
            return -1
        k = j
        for i in s:
            if t[j] == i:
                j += 1
            if j >= len(t):
                return res+1
        res += 1

s,t=map(str,input().split())
print(subsequence_string(s,t))
