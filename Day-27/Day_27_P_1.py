'''

KMIT hosting a Keshav Memorial Badminton League. They planned to conduct
N number of games. Each game begin and ends in perticular time slot.

You are given an array of time slots of the N games, consisting of
begin and end times (b1,e1),(b2,e2),... (b < e ).
Your task is to determine minimum number of badminton courts required 
to conduct all the games smoothly.

NOTE: If a game begins at time 'a' ends at time 'b', 
another game can start at 'b'.

Input Format:
-------------
Line-1: An integer N, number of games.
Next N lines: Two space separated integers, begin and end time of each game.

Output Format:
--------------
Print an integer, minimum number of badminton courts required.


Sample Input-1:
---------------
3
0 30
5 10
15 20

Sample Output-1:
----------------
2

Sample Input-2:
---------------
3
0 10
15 25
25 35

Sample Output-2:
----------------
1



'''

#Solution

def BadmintonCourts(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    
    s = 0
    e = 0
    count = 0
    res = 0

    while s < len(start):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)
    return res
n=int(input())
intervals=[]
for i in range(n):
    row=list(map(int,input().split()))
    intervals.append(row)
print(BadmintonCourts(intervals))