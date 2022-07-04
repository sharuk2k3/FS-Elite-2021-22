'''

Vihaan is given a list of words[]. 
He is asked to create a method which returns the numbers of characters in a word 
formed from long lasting frequent posteriority.

Posteriority is the word formed from the original word with few characters removed
without modifying the corresponding order of the left over characters.

An uncommon posteriority between the list of words is a word that is a posteriority
of one word but not the others.

Your task is to find the longest uncommon posteriority of the list of words.
Return 0 if no uncommon posteriority.


Input Format:
-------------
Space separated strings words[]

Output Format:
--------------
Print an integer, the length of longest uncommon prosperity.


Sample Input-1:
---------------
mom rar ama

Sample Output-1:
----------------
3


Sample Input-2:
---------------
ppp ppp pp

Sample Output-2:
----------------
-1



'''

#Solution


import collections

def longestUncommonSublength(S):
    C = collections.Counter(S)
    S = sorted(C.keys(), key = len, reverse = True)
    for i,s in enumerate(S):
    	if C[s] != 1: 
            continue
    	b = True
    	for j in range(i):
    		I, c = -1, True
    		for i in s:
    			I = S[j].find(i,I+1)
    			if I == -1:
    				c = False
    				break
    		if c:
    			b = False
    			break
    	if b: return len(s)
    return -1

if __name__ == '__main__':
    S=list(map(str,input().split()))
    print(longestUncommonSublength(S))
    