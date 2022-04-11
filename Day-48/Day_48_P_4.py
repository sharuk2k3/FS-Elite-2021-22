'''

In a game, There are N boxes in a Queue.
Each box conatins few gold coins in it.

Yash and Dutt are playing the game.

Game rules are as follows:
	- Initially, Yash picks one of the box from either end of the Queue.
	- Then, Dutt picks one of the box from either end of the Queue.
	- Repeat the first and second steps until the Queue become empty. 
The person with the maximum amount of gold coins is the winner.

You are given N boxes of gold coins, coins[].
Your task is to find the name of the winner either Yash or Dutt. 

Input Format:
-------------
Line-1: An integer N
Line-2: N space separated integers coins[].

Output Format:
--------------
Print the name of the winner, Yash / Dutt


Sample Input-1:
---------------
3
2 6 3

Sample Output-1:
----------------
Dutt

Explanation: 
------------
Initially, Yash can choose between 2 and 3.
If he chooses 3 (or 2), then Dutt can choose from 2 (or 3) and 5. If player 2 chooses 5, then
Yash will be left with 2 (or 3).
So, final score of Yash is 3 + 2 = 5, and Dutt is 6.
Hence, Dutt is the winner.

Sample Input-2:
---------------
4
2 6 50 7

Sample Output-2:
----------------
Yash


'''

def CoinsWinner(boxes):
    
    if len(boxes) % 2 ==0:
        return "Yash"
        
    dp=[[0 for j in range(len(boxes))] for i in range(len(boxes))]
    
    for i in range(len(boxes)):
        dp[i][i]=boxes[i]
        
    for j in range(1,len(boxes)):
        for i in range(len(boxes)-j):
            dp[i][i+j]=max(boxes[i]-dp[i+1][i+j],boxes[i+j]-dp[i][i+j-1])
            
    if dp[0][-1]>=0:
        return "Yash"
        
    return "Dutt"
    
n=int(input())
boxes=list(map(int,input().split()))[:n]
print(CoinsWinner(boxes))
