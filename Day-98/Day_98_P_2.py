'''

Cards Castle is a structure created by stacking cards on top of each other.

You are given a set of N cards, using them you have to build a Card Castle, by 
the following ruleset:
 - A Card Castle made up of cards arranged in rows of '/\'(triangle shape)
   and placing the cards horizontally on the triangles.
 - A '/\' shape can be achieved by leaning two cards against each other.
 - A card must be placed horizontally, between all adjacent triangles in a row.
 - Any triangle on a row higher than the first must be placed on a 
   horizontal card from the previous row.
 - Each triangle is placed in the leftmost available spot in the row.

Your taskis to find the number of unique Card Castles you can build using all N 
cards. 

NOTE: Two Card Castles are considered unique, if there exists a row 
where the two castles contain a different number of cards.


Input Format:
-------------
An integer N, number of cards

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
7

Sample Output-1:
----------------
1


Sample Input-2:
---------------
19

Sample Output-2:
----------------
3


Sample Input-3:
---------------
6

Sample Output-3:
----------------
0


Look hint for the explanation of the sample testcases.



'''

#Solution

def houseOfCards(n):
    dp = [0]*(n+1)  
    dp[0] = 1
    for t in range(1, (n+1)//3+1):
        for i in reversed(range(3*t-1, n+1)):
            dp[i] += dp[i-(3*t-1)]
    return dp[n]

if __name__ == '__main__':
    n=int(input())
    print(houseOfCards(n))