'''

Dice Game
Problem Description
Tanu and Shree are friends. They love playing dice games. They also like to experiment and invent new things. They have invented a mechanism whereby upon a click of a button the number of faces on the die and the value of every face on the die gets decided.

Their invention allows the die to have a minimum of 2 faces and a maximum of 12 faces. All faces of the die have an equal probability of being rolled over.

For example, if the button has generated the number 2, then the die will have 2 faces printed with numbers 1 and 2.

The rules of the game are as follows:

The two players of the game will play alternately
They can throw the dice any number of times in their turn to come up with the sum as exactly S
The player who comes up with the sum S in a smaller number of throws will win the game
S < m is valid; hence it is possible that the second player may not get a chance to roll the dice
Your task is to compute the number of ways in which the sum (S) can be achieved with dice throws.

Refer Examples section for better understanding.

Constraints
2 < S <= 10 ^ 5

1 < m <= 12

Input
The first line of input contains an integer T which denotes the number of test cases.

Next T lines contain two space separated integers S and m where

S denotes the sum to be achieved
m denotes the number of faces on the dice
Output
For every test case print a single integer corresponding to the number of ways in which a sum of S can be achieved. Print answer to every test case on a new line.

Time Limit (secs)
1

Examples
Example 1

Input

3

4 2

5 2

5 3

Output

5

8

13

Explanation

For Test case 1, we have S as 4 and m as 2. So, the number generated on the dice is 1 and 2. And the possible ways to get the sum as 4 from 1 and 2 are (1,1,1,1), (1,1,2), (1,2,1), (2,1,1) and (2,2). So, the output here is 5.

For Test case 2, we have S as 5 and m as 2. So, the number generated on the dice is 1 and 2. And the possible ways to get the sum as 5 from 1 and 2 are (1,1,1,1,1), (1,1,1,2), (1,1,2,1), (1,2,1,1), (2,1,1,1), (2,2,1), (2,1,2) and (1,2,2). So, the output here is 8.

For Test case 3, we have S as 5 and m as 3. So, the number generated on the dice is 1, 2 and 3. If it is expanded as shown in test cases 1 and 2 above, the total number of possible ways to get sum as 5 is 13.

Example 2

Input

1

3 2

Output

3

Explanation

For Test case 1, we have S as 3 and m as 2. So, the number generated on the dice is 1 and 2. And the possible ways to get the sum as 3 from 1 and 2 are (1,1,1), (1,2) and (2,1). So, the output here is 3.

'''