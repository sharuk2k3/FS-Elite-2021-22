'''

Pramod is working on words. He used to remove all the duplicate letters 
from a word. Pramod is given a word W. His task to remove all the duplicate 
letters from W, in such a way that the resulatant word R, contains 
no duplicate letters and all distinct letters from W should be there in R. 
And R should appear first in the dictionary order. 

Input Format:
-------------
A String, the word W.

Output Format:
--------------
Print a String, resulatant word R.


Sample Input-1:
---------------
cbadccb

Sample Output-1:
----------------
adcb


Sample Input-2:
---------------
silicosis

Sample Output-2:
----------------
ilcos


'''

#SOLUTION

import collections
def removeDup(s):
    myC=collections.Counter(s)
    res=[]
    seen=set()
    
    for c in s:
        while res and c<res[-1] and myC[res[-1]]>0 and c not in seen:
            
            x=res.pop()
            seen.discard(x)        
        if c not in seen:    
            res.append(c)
            seen.add(c)
        myC[c]-=1
        
    return ''.join(res)
    
s=input()
print(removeDup(s))