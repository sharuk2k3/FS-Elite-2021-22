'''


Naresh is working on expression of words.
If you give him an expression like, [p,q,r]s[t,u],
Naresh will form the words like as follows : [pst, psu, qst,qsu, rst, rsu]
Another example, [a,b]c[d,e] will be converted as: [acd, ace, bcd, bce].

Naresh will be given an expression as a string EXP, like the above format.
He needs to return all words that can be formed in like mentioned above, 
Can you help Naresh to convert iven expression into a list of words, in lexicographical order.

NOTE: 
Expression consist of lowercase alphabets, comma, and square brackets only.

Input Format:
-------------
A string EXP, expression.

Output Format:
--------------
Print list of words, formed from the expression.


Sample Input-1:
---------------
[b]c[e,g]k

Sample Output-1:
----------------
[bcek, bcgk]


Sample Input-2:
---------------
[a,b][c,d]

Sample Output-2:
----------------
[ac, ad, bc, bd]


Sample Input-3:
---------------
[xyz]a[b,c]

Sample Output-3:
----------------
[xyzab, xyzac]




'''

#Solution:

import itertools

def braceExpansionII(expression):
    groups = [[]]
    level = 0
    for i, c in enumerate(expression):
        if c == '[':
            if level == 0:
                start = i+1
            level += 1
        elif c == ']':
            level -= 1
            if level == 0:
                groups[-1].append(braceExpansionII(expression[start:i]))
        elif c == ',' and level == 0:
            groups.append([])
        elif level == 0:
            groups[-1].append([c])
    word_set = set()
    for group in groups:
        word_set |= set(map(''.join, itertools.product(*group)))
    return sorted(word_set)

if __name__=='__main__':
    expression=input()
    print(braceExpansionII(expression))

