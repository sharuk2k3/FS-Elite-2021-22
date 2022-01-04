'''

Alice has sent an encra cipher text to his friend Bob, and ask his help 
to crack it. The cipher text conatins digits only. 

Bob has cracked the pattern of decryption as follows:
1 maps to 'A',  2 maps to 'B',  3 maps to 'C', ... , 26 maps to 'Z'.

Now its Alice task is to find out the number of ways to decrypt 
the cipher text to plain text.

Example-1: 121 can be converted as ABA, or AU, or LA
Example-2: 1201 can be converted as ATA only. Alice is not allowed to 
convert as LA, 12 maps to L, 01 should not map to 'A'.


Input Format:
-------------
A string, the secret.

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
123

Sample Output-1:
----------------
3

Explanation:
------------
123 can be converted as: ABC, LC, AW


Sample Input-2:
---------------
326

Sample Output-2:
----------------
2

Explanation:
------------
326 can be converted as: CBF, CZ


'''


#SOLUTION



def Decode(s):
    if s=="":
        return 0
    if s=='0':
        return 0
    n=len(s)
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        if 0<int(s[i-1])<10:
            dp[i]+=dp[i-1]
        if 10<=int(s[i-2:i])<=26:
            dp[i]+=dp[i-2]
    return dp[n]
s=input()
print(Decode(s))

