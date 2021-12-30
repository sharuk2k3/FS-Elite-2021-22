'''

Mr Suresh is working with the plain text P, a list of words w[], 
He is converting P into C [the cipher text], C is valid cipher of P, 
if the following rules are followed:
	- The cipher-text C is a string ends with '$' character.
	- Every word, w[i] in w[], should be a substring of C, and 
	the substring should have $ at the end of it.

Your task is to help Mr Suresh to find the shortest Cipher C,  
and return its length.

Input Format:
-------------
Single line of space separated words, w[].

Output Format:
--------------
Print an integer result, the length of the shortest cipher.


Sample Input-1:
---------------
kmit it ngit

Sample Output-1:
----------------
10

Explanation:
------------
A valid cipher C is "kmit$ngit$".
w[0] = "kmit", the substring of C, and the '$' is the end character after "kmit"
w[1] = "it", the substring of C, and the '$' is the end character after "it"
w[2] = "ngit", the substring of C, and the '$' is the end character after "ngit"


Sample Input-2:
---------------
ace

Sample Output-2:
----------------
4

Explanation:
------------
A valid cipher C is "ace$".
w[0] = "ace", the substring of C, and the '$' is the end character after "ace"


'''


#SOLUTION

'''
import collections
def lengthOfCipher(words):
    words = list(set(words))
    Trie  = lambda: collections.defaultdict(Trie)
    trie  = Trie()
    nodes = []
    for word in words:
        current_trie = trie
        for c in reversed(word):
            current_trie = current_trie[c]                
        nodes.append(current_trie)
    return sum(len(word) + 1
               for i, word in enumerate(words)
               if not nodes[i])
words=list(map(str,input().split()))
if __name__=="__main__":
    print(lengthOfCipher(words))

'''


import collections
def lengthOfCipher(words):
    trie_root = dict()
    isLeafNode = lambda node: len(node) == 0
    tail_nodes = []
    unique_words = set(words)
    for word in unique_words:
        cur = trie_root
        for char in reversed(word):
            cur[char] = cur.get(char, dict() )
            cur = cur[char]
        tail_nodes.append( (cur, len(word)+1) )
    return sum( suffix_length for node, suffix_length in tail_nodes if isLeafNode(node) )
if __name__=="__main__":
    words=list(map(str,input().split()))
    print(lengthOfCipher(words))