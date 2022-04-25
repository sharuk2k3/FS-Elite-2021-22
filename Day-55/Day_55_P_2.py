'''



Ms.Akhila is a famous mathematician in a school, one day she decided to
send her students to Maths Olympiad competetion

To do that MS, Akhila called N number of students and ask them to stand in line.
Each student is having distinct grade according to his/her perfomences based
on the exams she conducted so far.

In order to send the students to Olympiad, Ms. Akhila has to form a team of 
3 students among N students from the line with following conditions:
	-> Pick any 3 students with index(p,q,r) with 
	grade(grade[p],grade[q],grade[r]).
	->A team is consider as valid if: 
	  - ( grade[p] < grade[q] < grade[r] ) or ( grade[p] > grade[q] > grade[r] )
 	    where (0 <= p < q < r < N).                                           
     
You are given grades[], grades of N students in the line.                                    
Your task is to return the number of teams Ms.Akhila can form with 
given conditions (students can be part of multiple teams).

Input Format:
-------------
Line-1: AN integer N, number of students.
Line-2: N space seperated integers, grades[].

Output Format:
--------------
An integer, number of teams can be formed.


Sample Input-1:
---------------
5
3 6 4 5 2

Sample Output-1:
----------------
3

Explanation:
------------
Ms Akhila can form three teams given the conditions. 
(3,4,5), (6,4,2), (6,5,2).


Sample Input-2:
---------------
5
1 2 3 4 5

Sample Output-2:
----------------
10




'''


#Naive Approach

def grade(n, grades):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (grades[i] < grades[j] < grades[k]) or (grades[i] > grades[j] > grades[k]):
                    #print(grades[i],grades[j],grades[k])
                    count += 1
    return count
n=int(input())
grades=list(map(int,input().split()))
print(grade(n,grades))