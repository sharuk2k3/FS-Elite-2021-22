'''
Program-8:

Given two lists of equal size. Where each element is a string. 
We have to find where the same index elements in both array's are anagram or not. 
If not, what is the minimum number of characters replaced to make both the word anagram. 
If the word's sizes are different then taking it -1.

lnput : 
list1-["ate","bat","girl"]
list2-["eat","tar","gir"]
Output: [0,1,-1]
Explanation: 
The first pair of elements "ate" and "eat" are anagrams so no replacing.
The second pair of elements "bat" and  "tar" differ from once character so we need to replace once character in either of the string
The third pair of elements "girl" and "gir" have different lengths and we are not allowed to append the character so the answer is -1.
Input:
list1-["battle","table","fat"]
list2-["tleabc","ttabc","fat"]
Output:
[1,2,0]
'''
from collections import Counter 
def minSteps():
    ans=[]
    for i in range(len(l1)):
        s=l1[i]
        t=l2[i]
        if len(s)!=len(t):
            ans.append(-1)
            continue
        counters, countert=Counter(s),Counter(t)
        counter_diff = dict(counters - countert)
        ans.append(sum(counter_diff.values()))
    return ans
l1=list(map(str,input().split()))
l2=list(map(str,input().split()))
print(minSteps())
