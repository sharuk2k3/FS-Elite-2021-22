'''

Radiation
Problem Description
Staying in towns that have nuclear energy sources nearby is not without its risk. One has to run for life if there is even a slight possibility of radiation leaks. Given your own location within the town and location of sources of radiation and a few other factors, predict if it is possible to survive radiation leaks.

These other factors are:

Time that it takes for the radiation to spread
Speed at which an individual can move towards a safe zone
Location at which an individual is deemed "safe" from radiation
Initial location of the source(s) of radiation and the individual
You are performing a simulation to analyze survivability. You use the following rules in your experiment:

Radiation can move only in Left, Right, Up and Down directions if the town is viewed logically in the form of a matrix
The left top element of the matrix is considered (0, 0) and indices increase as one moves right and down
Radiation will spread exponentially i.e., it will infect the adjacent cells after say T time units. These newly infected cells will also infect their neighbours after another T time units have elapsed
An individual can also move in all 4 directions viz. Left, Right, Up and Down. Also, the speed of the movement of the human is 1 cell (of the matrix) / time unit
An individual has to constantly be on the move if radiation breaks out and one cannot go back to the already visited cell in the matrix during the dash towards the safe zone
An individual has to reach a non-infected cell of column zero to be deemed to have escaped from radiation
Let's see examples of how the radiation spreads.

If the town is depicted as a 3 * 3 matrix and the source of radiation is at (1, 1) and the radiation growing rate is of 5 time units, then the following will happen, over time.

In the beginning, state of the town will look like this:

0 0 0

0 X 0

0 0 0

After 5 time units:

0 X 0

X X X

0 X 0

Similarly, consider another example - If the town is denoted as a 7 * 13 matrix and cells marked as X are the initial sources of radiation, and if the radiation infects its adjacent cells in 5 time units, then the same is depicted below

T0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 X 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 X 0 0 0 0

0 0 X 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

T5

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 X 0 0 0 0 0 0 0 0 0

0 0 X X X 0 0 0 0 0 0 0 0

0 0 0 X 0 0 0 0 X 0 0 0 0

0 0 X 0 0 0 0 X X X 0 0 0

0 X X X 0 0 0 0 X 0 0 0 0

0 0 X 0 0 0 0 0 0 0 0 0 0

T10

0 0 0 X 0 0 0 0 0 0 0 0 0

0 0 X X X 0 0 0 0 0 0 0 0

0 X X X X X 0 0 X 0 0 0 0

0 0 X X X 0 0 X X X 0 0 0

0 X X X 0 0 X X X X X 0 0

X X X X X 0 0 X X X 0 0 0

0 X X X 0 0 0 0 X 0 0 0 0

Now, let us understand how an individual moves during leaks

Example:

Input:

Grid size: 7 * 13

Radiation source at T = 0: [6, 12] and [6, 2]

Spreading time: 5 time units

Entry point: [2, 12]

T0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 * <--Initial location of the individual---

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 X 0 0 0 0 0 0 0 0 0 X

T5

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 * 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 X 0 0 0 0 0 0 0 0 0 X

0 X X X 0 0 0 0 0 0 0 X X

T10

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 * 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 X 0 0 0 0 0 0 0 0 0 X

0 X X X 0 0 0 0 0 0 0 X X

X X X X X 0 0 0 0 0 X X X

T12

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

* 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 X 0 0 0 0 0 0 0 0 0 X

0 X X X 0 0 0 0 0 0 0 X X

X X X X X 0 0 0 0 0 X X X

Please note that although the last row of zeroth column is infected, the cell that the individual has reached is not infected. Hence this individual has escaped the radiation leaks.

Constraints
1 <= N, M <= 50

0 < R <= 10

0 < T < 10

Input
First line contains two space separated integers M and N, which denote the size of matrix.

Second line contains an integer R which is the number of radiation sources.

Next R lines consist of two space separated integers denoting the coordinates of the source of radiation leaks.

Next line consists of an integer T which depicts the time interval required for the radiation to infect its adjacent cells.

Next line consists of two space separated integers which denote the initial location of the individual in the grid.

Output
Print "Escape possible" If the individual is able to escape the grid without being affected by the radiation, otherwise print "Escape not possible".

For more clarity refer the Examples section.

Time Limit (secs)
1

Examples
Example 1

Input

5 5

2

0 0

4 4

3

3 4

Output

Escape possible

Explanation:

Given M = 5, N = 5,

There are 2 radiation sources: {0, 0} and {4, 4}

T0

X 0 0 0 0

0 0 0 0 0

0 0 0 0 0

0 0 0 0 * <-----Initial location of the individual

0 0 0 0 X

T1

X 0 0 0 0

0 0 0 0 0

0 0 0 0 0

0 0 0 * 0

0 0 0 0 X

T2

X 0 0 0 0

0 0 0 0 0

0 0 0 0 0

0 0 * 0 0

0 0 0 0 X

T3

X X 0 0 0

X 0 0 0 0

0 0 0 0 0

0 * 0 0 X

0 0 0 X X

T4

X X 0 0 0

X 0 0 0 0

0 0 0 0 0

* 0 0 0 X

0 0 0 X X

We can see that the person has reached the non-infected cell of the 0th column of the matrix. Hence the output will be "Escape possible".

Example 2

Input

4 8

3

0 0

3 3

3 7

3

2 7

Output

Escape not possible

Explanation:

Given M = 4, N = 8

There are 3 radiation sources: {0, 0}, {3, 3} and {3, 7}

T0

X 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 *

0 0 0 X 0 0 0 X

T1

X 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

0 0 0 0 0 0 * 0

0 0 0 X 0 0 0 X

T2

X 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0

0 0 0 0 0 * 0 0

0 0 0 X 0 0 0 X

T3

X X 0 0 0 0 0 0

X 0 0 0 0 0 0 0

0 0 0 X * 0 0 X

0 0 X X X 0 X X

T4

X X 0 0 0 0 0 0

X 0 0 0 * 0 0 0

0 0 0 X 0 0 0 X

0 0 X X X 0 X X

T5

X X 0 0 0 0 0 0

X 0 0 * 0 0 0 0

0 0 0 X 0 0 0 X

0 0 X X X 0 X X

T6

X X X 0 0 0 0 0

X X * X 0 0 0 X

X 0 X X X 0 X X

0 X X X X X X X

So, the individual will get stuck at position (1, 2), and whatever path one takes at T6, one will get infected. Even if one takes an altogether different path, right from T0, one will still get infected. So, the output in this case will be "Escape not possible".

'''

def main():
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for source in sources:
        grid[source[0]][source[1]] = 1
    if grid[start[0]][start[1]] == 1:
        print("Escape not possible")
    else:
        for i in range(t):
            for j in range(n):
                for k in range(m):
                    if grid[j][k] == 1:
                        if j-1 >= 0:
                            grid[j-1][k] = 1
                        if j+1 < n:
                            grid[j+1][k] = 1
                        if k-1 >= 0:
                            grid[j][k-1] = 1
                        if k+1 < m:
                            grid[j][k+1] = 1
            print("Escape possible")
            break

n, m = map(int, input().split())
r = int(input())
sources = []
for _ in range(r):
    sources.append(list(map(int, input().split())))
t = int(input())
start = list(map(int, input().split()))
main()