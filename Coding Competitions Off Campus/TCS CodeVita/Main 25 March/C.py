'''

Point Force
Problem Description
We can imagine the points on a line attracting each other with a force akin to gravity. Consider points with natural number coordinates on a line that starts at the origin and extends up to 10^8. Assume that there is an attractive "force" between any chosen pair of points that is given by the following:

Force between the two points on the above line having coordinates x1 and x2 with x2 > x1 (both non-primes) is given by the following equation [(x1 * x2) / ((x2 - x1) ^ 2)] which is equivalent to the product of the coordinates of the points divided by the square of the distance between the points.

Note that the force between the origin and any other point is zero since the coordinate of the origin is zero. Further assume that prime numbers are like the origin - hence the force between a prime number and any other point is zero.

Consider the following points: 1 and 2. The force between these is 0 since 2 is prime.

Points 1,2 => Force 0

Taking a few more pairs, we have the following forces:

1,3 => 0 (since 3 is prime)

1,4 => 4/9 = 0.44

1,5 => 0 (since 5 is prime)

1,6 => 6/25 = 0.24

..

2,3 => 0 (since 2, 3 are prime)

2,4 => 0 (since 2 is prime)

..

3,4 => 0 (since 3 is prime)

3,5 => 0 (since 3,5 are prime)

..

4,5 => 0 (since 5 is prime)

4,6 => 24/4 => 6 (henceforth, all intermediate computations are not depicted where the force is an integer value)

4,7 => 0 (since 7 is prime)

4,8 => 2

4,9 => 36/25 = 1.44

..

100, 101 => 0 (since 101 is prime)

100, 102 => 2550

..

1729, 1730 => 1729*1730/1^2 = 2991170

Now, find two points with the smallest coordinates between 2 given coordinates p1 and p2 with a force greater than or equal to a given value F, a natural number.

Print "None" if there are no such points.

Refer Examples section for better understanding.

Constraints
p1 < p2 <= 10 ^ 8

p2-p1 <= 10 ^ 3

F <= 10 ^ 10

Input
Input consists of 3 natural numbers representing F, p1, p2 separated by spaces where F denotes the force and p1 and p2 are points on the number line.

Output
Two numbers (point coordinates) separated by a space - these should be the smallest coordinates between which the force is at least F.

Time Limit (secs)
1

Examples
Example 1

Input

31 10 15

Output

12 14

Explanation

We need to solve for least x1, x2 such that 10 <= x1 < x2 <= 15 and [(x1 * x2) / ((x2 - x1) ^ 2)] >= 31

Force between 10, 11 => 0 (since 11 is prime).

Force between 10, 12 => 30

Force between 10, 13 => 0 (since 13 is prime).

Force between 10, 14 => 140/16 = 2.5

Force between 10, 15 => 6

Force between 11, (any other number <=15) => 0 (since 11 is prime).

Force between 12, 13 => 0 (since 13 is prime).

Force between 12, 14 => 42, which is greater than 31.

Hence the desired points are 12 and 14. Hence, output is 12 14.

Example 2

Input

1729 1000 2000

Output

1000 1001

Explanation

Here F=1729. The force between 1000 and 1001 (both non-prime) is [(1000 * 1001) / (1 ^ 2)] = 1001000 which is greater than 1729. These are the least coordinates between 1000 and 2000 for which the force exceeds 1729. Hence output is 1000 1001.

Example 3

Input

123456 100 200

Output

None

Explanation

There is no pair of points between 100 and 200 for which the mutual force exceeds 123456. Hence, output is None.

'''

