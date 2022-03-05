"""

Train Track
Problem Description
Station master of Codington railway station is working on automation of trains to platform allocation. This allocation will not only prevent manual errors but also bring about a consistency in train to platform allocation. This will improve the passenger experience. Your job is to help the station master achieve the objectives.

The data and the rules that need to be considered for this automation are as follows-

Codington is a large railway junction. Hence assume that there is always a platform at which the incoming train can be accommodated (infinitely many platforms). However, operating using a less number of platforms is economical and hence preferred.
Safety is of paramount importance. Hence, safety cannot be traded off for cost. For example, if Train A's departure time is x and Train B's arrival time is x, then we can't accommodate Train B on the same platform as Train A.
The trains to platforms allocation rules are as follows-
The platform which is being freed earlier has to be considered earlier for allocation to the next train. For example, if platform #2 is freed at t=5 and platform #1 is freed at t=6, in that case the next train arriving at t=7 will arrive at platform #2.
If two or more platforms are freed at the same time, then the train arrives on the platform with the lowest number. For example, if platform #1 and #2 are freed at t=5 and the train is arriving at time t=6, then the train needs to arrive at platform #1.
If two or more trains are arriving at the same time then above two rules should be applied first for a train with smaller train number. This train's allocation will be decided first and the next qualified platform will be allocated to the other train. For example, consider the table below
Case No.	Platform #1 free since	Platform #2 free since	Train number 1 arriving at	Train number 2 arriving at	Resulting allocation
Case 1	t=5	t=6	t=7	t=7	Train 1 is allocated platform #1 and Train 2 is allocated platform #2
Case 2	t=5	t=5	t=7	t=7	Train 1 is allocated platform #1 and Train 2 is allocated platform #2
Case 3	t=6	t=5	t=7	t=7	Train 1 is allocated platform #2 and Train 2 is allocated platform #1
Constraints
1 <= N <= 5.10^4

0 <= A <= 86400

0 < I <= 86400

1000 < T < 10^8

Number of platforms > 0

Input
First line contains an integer N denoting number of trains.

Next N lines contain three integers T, A and I denoting the train number(T), the arrival time(A) and stoppage interval(I) of train respectively.

Next line contains an integer F denoting the train number for whom the allocated platform is to be reported in the output.

Output
First line contains an integer denoting the platform number on which the train F arrived.

Second line contains an integer denoting the busiest platform number on which the maximum trains arrived.

OR

If there are more than one platform having same traffic, sort all such platforms and print them in ascending order with each platform number on a new line. For example, if platform #2 and #3 are the busiest platforms then print as given below -

2

3

Time Limit
2

Examples
Example 1

Input

3

12121 15 5

12311 5 10

17215 2 3

12311

Output

2

1

Explanation

The earliest arriving train (17215) is at time t = 2 will arrive at platform# 1. Since it will stay there till t = 5, train (12311) arriving at time t = 5 will arrive at platform# 2 as the previous train (17215) will leave at t=5. Since current train (12311) will depart at time t = 15, next train (12121) arriving at time t = 15 will arrive at platform# 1 as the previous train (17215) left at t=5.

Here, maximum traffic came on platform #1. And train 12311 arrived at platform #2.

Example 2

Input

4

12106 2 4

12144 7 2

02812 3 2

13411 5 5

13411

Output

3

2

Explanation

The earliest arriving train (12106) at time t = 2 will arrive at platform# 1. Since it will stay there till t = 6, train (02812) arriving at time t = 3 will arrive at platform# 2. Since it will stay there till t = 5, train (13411) arriving at time t = 5 will arrive at platform# 3 Since it will stay there till t = 10, train (12144) arriving at time t = 7 will arrive at platform #2 as the previous train (02812) left at t=5.

Here, maximum traffic came on platform #2. And train 13411 arrived at platform #3.

"""

#SOLUTIONS
