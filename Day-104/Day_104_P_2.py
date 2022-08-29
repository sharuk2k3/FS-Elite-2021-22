'''
Kiran is given a string S, and an integer N.
Kiran wants to find the longest substring which has following properties:
	- the substring of S should be maximum in length, and 
	- should contains maximum of N unique characters in it.
Your task is to help Kiran to find the longest substring 'ls' with 
above properties and return the length of the substring 'ls'.

Input Format:
-------------
Line-1: A string S
Line-2: An integer N, number of distinct characters.

Output Format:
--------------
Print an integer, length of longest substring with a max of N unique characters.


Sample Input-1:
---------------
philippines
3

Sample Output-1:
----------------
6

Sample Input-2:
---------------
abaccdbcca
2

Sample Output-2:
----------------
3

'''
from collections import Counter

def LongestSubstring(s,k):
    ans = 0
    distinct = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      if count[c] == 1:
        distinct += 1
      while distinct == k + 1:
        count[s[l]] -= 1
        if count[s[l]] == 0:
          distinct -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans

if __name__ == '__main__':
    s=input()
    k=int(input())
    print(LongestSubstring(s,k))