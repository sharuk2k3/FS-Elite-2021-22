'''


A graduate at University of California (UoC) has to follow certain rules.

UoC offering K subjects, the subjects are indexed from 0 to K-1.
Some subjets have to follow the conditions, like condition[i]= [Xi, Yi], 
which specifies you must take the subject Yi before the subject Xi.

You are given total number of subjects and a list of the condition pairs.
Return the ordering of subjects that a graduate should take to finish all subjects.
	- the result set should follow the given order of conditions.
	- If it is impossible to complete all subjects, return an empty set.

Input Format:
-------------
Line-1: An integer K, number of subjects.
Line-2: An integer C, number of conditions.
Next C lines: Two space separated integers, Xi and Yi.

Output Format:
--------------
Return a list of integers, the ordering of subjects that a graduate should take 
to finish all subjects


Sample Input-1:
---------------
4
3
1 2
3 0
0 1

Sample Output-1:
----------------
[2, 1, 0, 3]

Explanation-1:
--------------
There are a total of 4 courses to take. 
Subject 1  should be taken after you finished subject 2.
Subject 3  should be taken after you finished subject 0.
Subject 0  should be taken after you finished subject 1.
So the correct subject order is [2, 1, 0, 3].

Sample Input-2:
---------------
5
5
0 1
1 2
2 3
3 4
4 0

Sample Output-2:
----------------
[]

Explanation-2:
-------------
No subject can be completed because they depend on each other.



'''

#Solution:

from collections import deque

def findOrder( numCourses, prerequisites):
    adjacentList, q, indegree, order = [[] for _ in range(numCourses)], deque(), [0] * numCourses, []
    for to, from_ in prerequisites:
        adjacentList[from_].append(to)
        indegree[to] += 1
    for course, ind in enumerate(indegree):
        if not ind: q.appendleft(course)
    while q:
        course = q.pop()
        order.append(course)
        for nextCourse in adjacentList[course]:
            indegree[nextCourse] -= 1
            if not indegree[nextCourse]: q.appendleft(nextCourse)
    return order if len(order) == numCourses else []

if __name__ == '__main__':
    numCourses=int(input())
    numC=int(input())
    prerequisites=[]
    for _ in range(numC):
        prerequisites.append(list(map(int,input().split())))
    print(findOrder(numCourses,prerequisites))
    