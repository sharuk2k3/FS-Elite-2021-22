'''

Ananth interested in creating the acronyms for any word. The definition
of acronym is another word with a concatenation of its first letter,
the number of letters between the first and last letter, and its last letter. 
 
If a word has only two characters, then it is an acronym of itself.

Examples:
    - Acronym of 'fog' is f1g'.
    - Acronym of 'another' is 'a5r'.
    - Acronym of 'ab' is 'ab'.

You are given a list of vocabulary, and another list of words.
Your task is to check,each word with the vocabulary and
return "true" if atleast one of the following rules satisfied:
1. acronym of the word should not match with any of the acronyms of vocabulary
2. if acronym of the word matches with any of the acronyms of vocabulary
'the word' and matching words in vocabulary should be same.

Otherwise, return 'false'.

Input Format:
-------------
Line-1: Space separated strings, vocabulary[] 
Line-2: Space separated strings, words[] 

Output Format:
--------------
Print N boolean values, where N = words.length 


Sample Input-1:
---------------
cool bell cool coir move more mike
cool char move 

Sample Output-1:
----------------
true false false


'''

#SOLUTION

def fun(dictionary,w):
    res_abbr = {}
    res_word = {}
    for word in dictionary:
        res_word[word] = 1 
        sub = word[0] + str(len(word) - 2) + word[-1]
        
    if sub in res_abbr:
        res_abbr[sub] += 1 
    else: 
        res_abbr[sub] = 1 
        
    if len(word) == 0:
        return True 
    if len(word) == 1 or len(word) == 2:
        return True
                
    sub = word[0] +str(len(word)-2) + word[-1]
      
     
    if word in res_word:
        if res_abbr[sub] == 1:
            return True
        return False
        
    if sub in res_abbr: 
        if res_abbr[sub] >= 1:
            return False
    return True
dictionary=list(map(str,input().split()))
w=list(map(str,input().split()))
print(fun(dictionary,w))


'''

l1 = input().split()
l2 = input().split()

L1 = ["" for i in range(len(l1))]
L2 = ["" for i in range(len(l2))]

for i in range(len(l1)):
    if len(l1[i]) > 2:
        L1[i] = l1[i][0] + str(len(l1[i])-2) + l1[i][-1]
    else:
        L1[i] = l1[i]

for i in range(len(l2)):
    if len(l2[i]) > 2:
        L2[i] = l2[i][0] + str(len(l2[i])-2) + l2[i][-1]
    else:
        L2[i] = l2[i]

f = 1
for i in range(len(L2)):
    f = 1
    for j in range(len(L1)):
        if L2[i] == L1[j]:
            if l1[j] == l2[i]:
                f = 1
            else:
                f = 0
                break

    if f:
        print('true')
    else:
        print('false')

'''