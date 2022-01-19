'''

Now a days, everyone is used to type the words in short-forms,
A short-form can be created by replacing non-intersected substrings 
and non-adjacent substrings with their respective lengths.

e.g., elite can be written as follows:
    - e3e (by replacing lit with 3), 
    - el2e (by replacing it with 2), 
	- 1l1t1 (by replacing e,i,e, with 1,1,1)
    - 3t1 (by replacing eli and e with 3 and 1), etc.
	and can't be written as follows:
	- 22e (by replacing el and it with 2 and 2)
	- 32 (by replacing eli and te with  3 and 2)

You will be given a word.
Your task is to find all possible short-forms of the given word, 
and print them as a list of lexicographic order.



Input Format:
-------------
A string W, the word.

Output Format:
--------------
Print the list of possible short-forms of W in lexographic order. 


Sample Input-1:
---------------
kmit

Sample Output-1:
----------------
[1m1t, 1m2, 1mi1, 1mit, 2i1, 2it, 3t, 4, k1i1, k1it, k2t, k3, km1t, km2, kmi1, kmit]


Sample Input-2:
---------------
cse

Sample Output-2:
----------------
[1s1, 1se, 2e, 3, c1e, c2, cs1, cse]


'''

#SOLUTION

def shortforms(word):
    if len(word) == 0:
        return [""]

    dp = [[]] * (len(word) - 1)
    dp.append(["1", word[-1]])

    for idx in range(len(word) - 2, -1, -1):
        suffixes = set()
        for l in range(1, len(word) - idx):
            for suffix in dp[idx + l]:
                suffixes.add(word[idx:idx+l] + suffix)
                if suffix[0].isalpha():
                    suffixes.add(str(l) + suffix)

        suffixes.add(str(len(word) - idx))
        dp[idx] = list(suffixes)

    return sorted(dp[0])
word=input()
print(shortforms(word))


'''

#NAVIE

def shortforms(word):
    ret = [ ("",0) ]
    for c in word:
        newRet = []
        for (s,k) in ret:
            newRet.append( (s,k+1) )
            newRet.append( (s + (str(k) if k else "") + c, 0) )

        ret = newRet

    return sorted([ (s + (str(k) if k else "")) for (s,k) in ret ])
word=input()
print(shortforms(word))
'''