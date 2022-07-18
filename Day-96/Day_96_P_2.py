'''


Mr Gnanesh is working with words. He has given a list of words. 
Each word in the list contains only two lowercase letters [a-z].

He wants to create biggest word BW, by concatenating words from the list, which 
is a palindrome too. He is allowed to use each word from the list atmost once.

Return the length of the biggest word can be formed using the list.
If it is impossible to create such word, return 0.

Input Format:
-------------
Space separated strings, words[], two letter words.

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
ab ba dd

Sample Output-1:
----------------
6

Explanation: 
------------
The biggest word is, ab,dd,ba => abddba, which is a palindrome.


Sample Input-2:
---------------
pq rs sr mk km pq

Sample Output-2:
----------------
8

Explanation: 
------------
The biggest word is, rs,sr,mk,km => rsmkkmsr or mkrssrkm..etc, 
which is a palindrome.


Sample Input-3:
---------------
aa bb cc

Sample Output-3:
----------------
2




'''
from collections import Counter

def longestPalindrome( words) :
    counts = Counter(words)
    ans, flag = 0, False
        
    for word in words:
        if not counts[word]:
            continue
        counts[word] -= 1
        if counts[word[::-1]]:
            ans += 4
            counts[word[::-1]] -= 1
        elif word == word[::-1]:
            flag = True
        
    return ans + (2 if flag else 0)

if __name__ == '__main__':
    words = list(map(str,input().split()))
    print(longestPalindrome(words))