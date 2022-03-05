"""

Jogging Ground
Problem Description
There are 4 circular grounds of equal sizes. Their circumferences do not intersect. The radius and the distance of the center of each circle from the leftmost circle's center are given.

There are 4 joggers who can start at the same time from any of the points designated as { a, b, c, d } on the circumference of all the four circles as shown in the diagram below. All 4 joggers jog in different grounds along the circumference of that ground. They could jog in either clockwise (left to right) or anticlockwise (right to left) direction. Finally they may also jog at different speeds.

Given starting position, direction of jogging and speed of jogging of all the 4 joggers, find the summation of length of 3 segments between the four joggers at a given point in time since the start of the jog.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@369beeb9:image1.png

Note: All the computation has to be accurate up to 6 digits after the decimal point.

Constraints
1 <= N < 10^9

Input
First line contains 4 integers each denoting the following

R denotes the radius of all four circles
D1 denotes the distance centre of the second circle from left to the centre of the leftmost circle
D2 denotes the distance centre of the third circle from left to the centre of the leftmost circle
D3 denotes the distance centre of the last circle from left to the centre of the leftmost circle
Second line contains 4 space separated integers denoting the angle with point a of each of the 4 circles where 0 degree indicates point a itself, 90 degree indicates point b, 180 degree indicates point c and 270 degree indicates point d.

Third line contains 4 space separated integers denoting the velocity in degrees per second.

Fourth line contains 4 space separated integers denoting the direction of running for joggers (0=clockwise and 1=anticlockwise).

Fifth Line contains integer N denoting the time in seconds since the start of the jog.

Output
Print the summation of length of 3 segments between the four joggers after N seconds, rounded to the nearest integer.

Time Limit
1

Examples
Example 1

Input

10 25 50 75

0 0 0 0

1 1 1 1

1 1 1 1

90

Output

75

Explanation

Here every jogger is starting from point a and all have speed of 1 degree per second. So they will be at 90 degree after 90 seconds. After connecting these points we get segment lengths as (25 +25 +25) = 75

Example 2

Input

10 25 50 75

0 0 0 0

1 2 3 4

0 0 0 0

90

Output

91

Explanation

Here every jogger is starting from point a. They are jogging at the speed of 1, 2, 3 and 4 degrees per second respectively in clockwise direction. Hence after 90 seconds they will reach points where the segment length between them is (18.027800+36.400500+36.400500) = 90.8288. Hence, output is 91

"""

#SOLUTIONS
