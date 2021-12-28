'''

Mr Shravan Kumar is given a word W and a list of words[]. He wants to check 
whether is it possible to create the word W from the given list of words 
by appending them or not. It is not necessary to use all the words from the list.
It is allowed to use the words in the list repeatedly if required to form the 
original W. 
Your task if to help Mr Nagireddy to find it is possibe to create the oridinal
word W or not. If possible print true. Otherwise flase.


Input Format:
-------------
Line-1: A single line word W, Original word.
Line-2: A single line space space-separated words, list[].

Output Format:
--------------
Print a boolean value.

Sample Input-1:
---------------
capable
cap cable ap able 

Sample Output-1:
----------------
true


Sample Input-2:
---------------
capable
cable ap able

Sample Output-2:
----------------
false


'''

#SOLUTION


def word(s, words):
    dp = [False for _ in range(len(s)+1)]
    for i in range(1,len(s)+1):
        if s[0:i] in words:
            dp[i] = True
        else:
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
    return dp[len(s)]

if __name__ == "__main__":
    s=input()
    words=list(map(str,input().split()))    
    print(word(s, words))