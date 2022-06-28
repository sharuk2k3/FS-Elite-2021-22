'''
You are given some tokens printed with unique numbers on it and an integer T.
Your task is to find the least number of tokens that you need to make up the 
value T, by adding the numbers printed on all the tokens. 
If yyou cannot make the value T, by any combination of the tokens, return -1.

NOTE: Assume that you have unlimited set of tokens of each number type.

Input Format:
-------------
Line-1: Space separated integers tokens[], number printed on tokens.
Line-2: An integer T.

Output Format:
--------------
Print an integer, minimum number of tokens to make the value T.


Sample Input-1:
---------------
1 2 5
11

Sample Output-1:
----------------
3

Explanation:
------------
5+5+1 = 11


Sample Input-2:
---------------
2 4
15

Sample Output-2:
----------------
-1


'''

#Solution:

#Using Dynamic Programming

def coinChange(coins, amount) :
    dp = [amount+1]*(amount+1)
        
    dp[0] = 0
    for i in range(amount+1):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], dp[i-coin]+1)
        
    return -1 if dp[amount] == amount+1 else dp[amount]

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    amount = int(input())
    print(coinChange(coins, amount))