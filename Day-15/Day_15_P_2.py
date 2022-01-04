'''

Given a classic mobile phone, and the key pad of the phone looks like below.
	1		2		3
		   abc	   def
		 
	4		5		6
   ghi     jkl     mno
  
	7		8		9
  pqrs     tuv    wxyz
	
	*		0		#


You are given a string S contains digits between [2-9] only, 
For example: S = "2", then the possible words are "a", "b", "c".

Now your task is to find all possible words that the string S could represent.
and print them in a lexicographical order. 

Input Format:
-------------
A string S, consist of digits [2-9]

Output Format:
--------------
Print the list of words in lexicographical order.


Sample Input-1:
---------------
2

Sample Output-1:
----------------
[a, b, c]


Sample Input-2:
---------------
24

Sample Output-2:
----------------
[ag, ah, ai, bg, bh, bi, cg, ch, ci]


'''

#SOLUTION

def fun(digits):
    res = []
    digitarray = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }



    
    def backtrack(i,currentstring):
        if len(currentstring) == len(digits):
            res.append(currentstring)
            return
        for c in digitarray[digits[i]]:
            backtrack(i+1,currentstring + c)
    if digits:
        backtrack(0,"")
    return res
digits=input()
if __name__=="__main__":
    print(fun(digits))
    
    
    
