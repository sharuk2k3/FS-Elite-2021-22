'''
Program-2: 
BadElement

consider variables i and j and some no.of jumps allowed, i=0 and j=1 initially.
in every jump out of the total no.of jumps allowed, there are two ways possible.
i=i+j and j=j+1
or i doesnt change but j=j+1
We should see that i is never equal to the given Bad element, following that condition, 
find out the maximum position that i can reach in the give no.of jumps.

Ex: Consider
Input=no.of jumps=4 and Bad Element=6
Scenario 1:
Jump1: i=0+1=1   j=j+1=2
Jump2: i=1+2=3   j=j+1=3
Jump3: i=3+3=6-> WRONG!      (i is equal to the bad element. So,jump through the second condition where only j increments and i remains the same.)
CORRECT: i=3 j=j+1=4
Jump4: i=3+4=7   j=j+1=5

Hence in 4 jumps, i=7 was achieved.

Scenario 2:
Jump1: Let us consider that i doesnt change in the initial jump itself, only j is incremented by 1
i=0   j=j+1=2
Jump2: i=0+2=2   j=j+1=3
Jump3: i=2+3=5   j=j+1=4
Jump4: i=5+4=9   j=j+1=5

Hence in 4 jumps, i=9 was achieved.

Hence the maximum position reachable without reaching bad element in any jump is 9.
Hence return 9
'''
def rep(be, jp, i, j):
    if i == be:
        return 0
    if jp == 0:
        return i
    return max(rep(be, jp-1, i+j, j+1), rep(be, jp-1, i, j+1))

jump = int(input())
badEle = int(input())
print(rep(badEle, jump, 0, 1))