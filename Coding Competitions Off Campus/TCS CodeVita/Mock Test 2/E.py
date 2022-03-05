"""

Minimum Penalty
Problem Description
You are playing a game in which you have to beat n players. You are invincible; hence you are always able to beat your opponent. After beating a player, you will get some points. Your task is to get maximum score by beating them all. You can pick anyone randomly for maximizing your score. Rules of the game are as follows:

It is guaranteed that you will be able to beat your opponent, hence your real task is to choose the best order to achieve maximum final score.
When you beat a player, you get some points and a score will be generated.
Here are some rules related to the game and maximizing your score:
All your opponent players are standing in one line next to each other i.e. the order of opponent is fixed
Your task is to choose a suitable opponent from this line
When you choose one opponent from that line, he steps out of the line and competes with you
After you beat him, you get to decide how your score for winning against him will be calculated
Essentially, if the opponent you have beaten has two neighbours, then you have the option to multiply the opponent number with any one of the two neighbours and subtract the other opponent number. That value becomes your winning score for that match
If your opponent has only one neighbor then your winning score for that match is product of current opponent number with neighbours opponent number
When dealing with last opponent in the game, your winning score is equal to the value of the last opponent number
As the game proceeds, the opponent that you have beaten has to leave the game
Example: 2 5 6 7

This depicts that you have four opponents with numbers 2 5 6 and 7 respectively

Suppose you choose to play with opponent number 5, then after winning, the max score for this match = 5*6 - 2 = 28
Now opponent number 5 is out of the game. So opponent numbers 2 6 7 remain

Suppose you now choose to play with opponent number 2, then after winning, the max score for this match = 2*6 = 12. Your overall score is now 28 + 12 = 40
Now opponent number 2 is out of the game. So opponent number 6 7 remain

Suppose you now choose to fight opponent number 6, then after winning, the max score for this match = 6*7 = 42. Your overall score is now 40 + 42 = 82
Now opponent number 6 is out of the game. So opponent number 7 remains

After beating opponent number 7, the max score for this match is 7
So overall score in this case is 89. Hence when the order is 5->2->6->7 the overall score is 89.

Some other orders of choosing opponents will yield the following overall score

Order 7->2->6->5 will yield overall score as 87
Order 2->5->6->7 will yield overall score as 89
Order 5->6->2->7 will yield overall score as 89
Order 6->7->2->5 will yield overall score as 87
But by following the order 6->5->2->7 will yield overall score as 91, which is maximum.
Hence, the correct answer yielded by order 6->5->2->7 is 91.

Your task is to maximize your score by taking the right decisions

Constraints
1 <= N <= 500

0 <= individual points of opponents < 100

Input
First line contains an integer N which denotes the number of opponents in the game

Second line contains N space separated integers, which are the opponent numbers of other opponents

Output
Print the maximum obtainable score by making all the right decisions

Time Limit
1

Examples
Example 1

Input

4

2 5 6 7

Output

91

Explanation:

Refer the explanation in problem description.

Example 2

Input

3

7 8 9

Output

137

Explanation:

You choose to play with opponent number 8, then after winning, the max score for this match is = 8*9-7 = 65
Now opponent number 8 is out of the game. So opponent numbers 7 9 remain

Suppose you now choose to play with opponent number 7, then after winning, the max score for this match is = 7*9 = 63. Your overall score is now 65 + 63 = 128
Now opponent number 7 is out of the game. So opponent number 9 remains

After beating opponent number 9, the max score for this match is = 9
So overall score in this case is 128 + 9 = 137.

There is no other optimal order in which final score can be better than 137.

"""

#SOLUTIONS
