'''

Mario
Problem Description
Imagine you are a video games developer. You are developing a game which requires the player to collect coins and cross hurdles. Let the character in your video game be called Mario. As Mario moves to collect coins and cross hurdles, the game keeps a count of relevant metrics. Write code to implement this flow.

Mario will run from left to right and jump from the ground in the air to collect coins or cross hurdles. The Game Screen will be provided as input in form of a matrix comprising of three characters viz {0, C and H}, where

0 - denotes empty space

C - denotes coins to be collected

H - denotes hurdles to be crossed

All coins are of the same type, whereas there are two types of hurdles - simple hurdle and ring hurdle. Simple hurdle is referred to as Hurdle hereafter.

A Hurdle always begins from the ground and a series of the letter H stacked vertically make up the height of the hurdle.

A Ring Hurdle on the other hand, has a hole in it i.e., between H characters there will be exactly one hole denoted by 0 character. This hole is big enough for Mario to jump through it to cross that hurdle.

Now, let us understand how this information is provided in the input

The screen will be depicted in the input as a M * N matrix. The index of row and columns of this matrix begin from zero.
The left bottom cell of this matrix is (0, 0). As we move right and up, the row and column indices increase
Row zero is considered as Ground and anything above row zero is considered as Air
Coins will always be in air, whereas hurdles will always manifest from the ground
Hurdle will never be so tall that Mario cannot cross it
Once Mario crosses all the columns, the game is over
To collect coins Mario will jump vertically in the column where the coin is. Mario always jumps to the highest point where a coin is, on the screen. On his way down from that point, he grabs all coins lower in height in that column. Thus, one jump in one column is enough to fetch all coins in that column
Jumping consumes energy. Jumping one row consumes 2 calories. Similarly, if Mario jumps R rows in a column, his calorific expenditure is 2 * R
Mario never jumps unless he must collect coins or cross a hurdle
When crossing a ring hurdle, the calories consumed in clearing it is 2 * height of the hole in the ring hurdle. Refer Examples section for better clarity
Walking i.e., moving from one column to another consumes no energy
Your task is to keep a track of how many coins Mario collects and how many calories are expended in collecting them.

Consider a screen (grid) of size 5 * 10:

0000000000

0CCC00000H

0CCC0H0000

00000H0H0H

00000H0H0H

We can see that we have coins on the screens in columns 1, 2 and 3.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@2e8ab815:image1.pngcom.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@2e8ab815:image2.png

The above two images describe collection of coins and energy spent in collecting them.

Column 1 has two coins at a height of 2 and 3 respectively. So, Mario will jump 3 units high and collect the highest coin. On his way down he will collect the coin at height 2. Total calories expended in collecting both coins in Column 1 is 3 * 2 = 6 calories.

Columns 2 and 3 are identical to Column 1. Hence Mario will have collected 6 coins and spent 18 calories in traversing the grid up to column 3.

Column 4 is empty. So, no energy is expended traversing it. Next, there are hurdles at Column 5 and 7.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@2e8ab815:image3.pngcom.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@2e8ab815:image4.png

For clearing these hurdles, he must jump over two hurdles, and by doing this he will consume 3 * 2 + 2 * 2 calories.

Total calories burned till now: 18 + 10 = 28

There is also a ring hurdle at column 9.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@2e8ab815:image5.png

For clearing these hurdles, he must jump over two hurdles, and by doing this he will consume 2 * 2 calories.

Total calories burned till now: 28 + 4 = 32

Total Coins grabbed: 6

Total Calories burned: 32

Note: Assume Mario can jump any hurdle of any height and collect coins at any height.

Constraints
0 < M <= 10

10 <= N < 100

Input
First line contains two space separated integers M and N which denote the size of grid (screen).

Next M lines will each contain a string of size N characters. The strings will comprise of {0, C and H} characters.

Output
Print two space delimited integers. First integer denotes the number of coins grabbed and second integer denotes the calories expended in crossing the screen.

Time Limit (secs)
1

Examples
Example 1

Input

5 10

0000000000

0CCC00000H

0CCC0H0000

00000H0H0H

00000H0H0H

Output

6 32

Explanation:

Explained in problem description section.

Example 2

Input

5 10

0000000000

000000000H

00H00H0000

00H00H0H0H

00H00H0H0H

Output

0 20

Explanation:

As we can see there are two hurdles of height 3 at column 2 and column 5 (3 * 2 * 2), one hurdle of height of 2 at column 7(2 * 2) and a ring hurdle of height 2(2 * 2) at column 9.

Thus, total coins grabbed is 0 and total calories expended is 20.

'''