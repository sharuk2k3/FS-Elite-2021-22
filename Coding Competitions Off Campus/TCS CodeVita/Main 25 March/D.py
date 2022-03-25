'''

Coin Collection
Problem Description
CoinCollection is a game played only by two players. It has an N x N grid, where each cell of grid may have a coin. A coin in a cell is represented by 'C' and an empty cell is represented with 'N'.

Here the players are denoted by Player1 and Player2 and they play turn by turn. A Player collects a group of coins which are contiguous either vertically or horizontally. When s/he cannot collect a coin anymore, the turn passes to the other player. The other player will do the same thing i.e., collect as many coins as possible from a group where coins are contiguous and when s/he cannot collect any more coins, the turn passes back to the first player.

Rules of the game are as follows:

Player1 always starts the game and then the turn goes to Player2 and this continues alternately.
A cell containing coin will have only one coin.
A group of coins indicate that coins are adjacent to each other horizontally or vertically. Suppose if there are no coins adjacent to a coin, then the number of coins in the group is 1.
For e.g.

1)

NCNN

NCCN

NNNC

In the above example, there are two groups viz. 3 coins group and 1 coin group.

2)

NCCN

NNNC

In the above example, there are two groups viz. 2 coins group and 1 coin group.

Players can collect the coins from any cells in the grid, it is not mandatory to start game from the 0th cell.
Each player must play optimally i.e., on their turns players must collect maximum coins that can be collected in that situation.
A player should collect only one group in his/her turn.
The game finishes after no coins are left in the grid.
Finally, compute the total number of coins collected by Player1 and Player2 and display them as output. Refer to Examples section for output format.

Constraints
1< = N <= 100

Input
First line contains an integer denoting the size of grid (N x N).

Next N lines contain values providing the grid state for each row.

Output
Print the value of coins collected by Player1 and Player2 separated by space.

Time Limit (secs)
1

Examples
Example 1

Input

4
CNNC
NCCN
NCCN
CNNC

Output

6 2

Explanation-

Given N=4 denotes the size of grid is 4X4.

Since the game always starts with Player1, Player1 will collect the group of coins present in the center. Player1 Turn:

CNNC
NCCN
NCCN
CNNC

After Player1 collects the group of coins from the center, Player2 gets a chance to play.

Now, Player2 collects coins present in any of the corners. But player2 can collect only from 1 group of his choice.

CNNC
NNNN
NNNN
CNNC

Let's assume Player2 collects group of coins from the top right corner.

After Player2 collects the group, Player1 gets a chance again and collects the coins from the other three corners i.e., top left, bottom left, bottom right. In this way the game goes on and finally the total number of coins collected by Player1 and Player2 are 6 and 2 respectively.

Example 2

Input

5

NNNNN

NNNNN

NNNNN

NCCCN

NNNNN

Output

3 0

Explanation-

Given N=5 denotes the size of grid is 5X5.

Since the game always starts with Player1, Player1 will collect the group of coins present in the fourth row.

Player1 Turn:

NNNNN

NNNNN

NNNNN

NCCCN

NNNNN

After player1 collects the group of coins from the grid, Player2 gets a chance to play.

Since there are no coins available in the grid, the game ends and Player2 has 0 coins.

Thus, total number of coins collected by Player1 is 3 and Player2 is 0.

'''