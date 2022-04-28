'''

In summer training camp, a course is divided into N sessions.
Each session handled by N different trainers, each trainer identified by an alphabet.
At the end of the course, the students are requested to give rating for each
trainer between 1 to N, each trainer should be assigned different rating.

For example, there are 3 trainers, I, J and K, the student can vote them as IJK,
JKI, IKJ..etc. Where IJK means, trainer-I got rating-1, trainer-J got rating-2, 
trainer-K got rating-3.

You have to sort the trainers based on the rating they recieved.
The sorting of the trainers is as follows:
	- The sorting of the trainers is decided by who received the most ratings.
	- If the trainer recieved more 1-ratings, he is in first place, 
	- If two or more trainers tie in the first place, you have to consider 
	the second place to resolve the conflict, if they tie again, we continue
	this process until the ties are resolved.
	- If two or more trainers are still tied after considering all the places, 
	we sort them alphabetically based on the assigned letter.

You will be given an array of ratings by S students in the class. 
Your task is to sort the trainers according to the above rules, and return the
sorted list of N trainers as a string by the rating given to them.

Input Format:
-------------
Line: Space separated strings,ratings given by S students for N faculty, 
      where S is ratings.length and N is ratings[i].length

Output Format:
--------------
Print a String output.


Sample Input-1:
---------------
JKI KIJ KJI IJK IKJ JIK

Sample Output-1:
----------------
IJK

Explanation:
------------
Trainer-I was rated first by 2 students, second by 2 students and third by 2 students.
Trainer-J was rated first by 2 students, second by 2 students and third by 2 students.
Trainer-K was rated first by 2 students, second by 2 students and third by 2 students.
There is a tie and you sort the trainers in ascending order by their IDs.


Sample Input-2:
---------------
PQSR SQRP

Sample Output-2:
----------------
SPQR

Explanation:
------------
Trainer-P was rated first by 1 student, Trainer-S was rated first by 1 student, 
there is a tie. In second place for P and S also a tie, now in third place S 
got rated by one student, and P by none. So, S occupies first place, 
then P occupies second-place, trainer-Q was rated by 2 students next,
so Q took third place, and ramaining trainer-R in the last place.


Sample Input-3:
---------------
K K K K

Sample Output-3:
----------------
K


'''

def rankRatings(Ratings):
    len_v, n_teams = len(Ratings), len(Ratings[0])
    if len_v == 1 or n_teams == 1:
        return Ratings[0]
    d = dict()
    for i, c in enumerate(sorted(Ratings[0])):
        d[c] = i
        d[i] = c
    rank = [[i] + [0] * n_teams for i in range(n_teams)]
    for vote in Ratings:
        for i, c in enumerate(vote):
            rank[d[c]][i + 1] -= 1
    rank.sort(key=lambda row: row[1:])
    return "".join(d[r[0]] for r in rank)

Ratings=list(map(str,input().split()))
print(rankRatings(Ratings))
