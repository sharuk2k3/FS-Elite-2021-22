'''

In an english training institute, the trainer Reeta given a task to the trainees.
We know that, in english we have prefixes and suffixes for the words.
You can divide a word as concatenation of prefix and suffix.
i.e., word = prefix + suffix, another = an + other

You will be given a list of prefixes and a statement consisting of words.
Now, the task given to the trainees is as follows:
	- Replace all the words in the statement with the prefix, 
	  if you found prefix of that word in the list.
	- If you found more than one prefix in the list for a word in the statement,
	  replace the word with the prefix that has the shortest length.

Your task is to help the trainees to prepare and print the final statement
after all the replacements done.

Input Format:
-------------
Line-1: Space separated strings, prefixes.
Line-2: A single line of words, statement.

Output Format:
--------------
Print the String, the final statement.


Sample Input-1:
---------------
am add mean ref 
amigos used to address or refer to a friend

Sample Output-1:
----------------
am used to add or ref to a friend


Sample Input-2:
---------------
th the pa tho
thomas the trainer teaches theroy part of thermodynamics

Sample Output-2:
----------------
th th trainer teaches th pa of th


'''

#SOLUTION


p = input().split()
w = input().split()
ans = []

class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
        
class Trie:
    
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        return TrieNode()

    def _charToIndex(self,ch):
        
        return ord(ch)-ord('a')


    def insert(self,key):
        
        r = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])

            if not r.children[index]:
                r.children[index] = self.getNode()
            r = r.children[index]

        r.isEndOfWord = True

    def search(self, key):
        
        r = self.root
        length = len(key)
        for i in range(length):
            index = self._charToIndex(key[i])
            if not r.children[index]:
                return False
            r = r.children[index]

        return r.isEndOfWord
    
t = Trie()

for i in p:
    t.insert(i)
    
for i in w:
    s = ""
    f = 0
    for j in i:
        s += j
        if t.search(s):
            ans.append(s)
            f = 1
            break
    if not f:
        ans.append(s)
print(*ans)


'''
def tries(words, statement):
    trie = {}    
    for w in words:
        temp = trie
        for c in w:
            if c not in temp:
                temp[c] = {}
            temp = temp[c]
        temp['\n'] = w 
        
        
    def replace(word): 
        temp = trie
        for c in word:
            if '\n' in temp:
                return temp['\n']
            if c not in temp:
                return word
            temp = temp[c]
        return word
        
    words = statement.split(' ')
    ans = []    
    for word in words:
        ans.append(replace(word))    
    return " ".join(ans)

words=input()
statement=input()

if __name__=="__main__":
    print(tries(words, statement))
'''