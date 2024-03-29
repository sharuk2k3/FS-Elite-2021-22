'''

There are N pair of words, the pair of words are likely to be similiar in 
meaning, where pair[i] = [org, similar] indicates that org and similar are 
equivalent words in meaning. and you are also provided a sentence 'phrase'.

You need to transform the phrase with pairs and return all possible transformed 
phrases sorted in lexicographical order.

Input Format:
-------------
Line-1: An integer N, number of pairs.
Next N lines: two space seperated strings, the pair. 
last Line: A string S, the original phrase.

Output Format:
--------------
List of transformed phrases in lexicographcal order.


Sample Input-1:
---------------
2
happy joy
share part
i am happy to share this with you

Sample Output-1:
----------------
[i am happy to part this with you, i am happy to share this with you, 
i am joy to part this with you, i am joy to share this with you]


Sample Input-2:
---------------
3
hi hello
sweet sugary
hard tough
hi ramesh the laddu you made is so sweet and hard

Sample Output-2:
----------------
[hello ramesh the laddu you made is so sugary and hard bite, 
hello ramesh the laddu you made is so sugary and tough bite, 
hello ramesh the laddu you made is so sweet and hard bite, 
hello ramesh the laddu you made is so sweet and tough bite, 
hi ramesh the laddu you made is so sugary and hard bite, 
hi ramesh the laddu you made is so sugary and tough bite, 
hi ramesh the laddu you made is so sweet and hard bite, 
hi ramesh the laddu you made is so sweet and tough bite]



'''

