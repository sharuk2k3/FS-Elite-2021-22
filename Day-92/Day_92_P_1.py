'''
You are given a set of releases of a software and you are asked to find the most
recent release. There may be multiple checkins of the software in a given branch. 
Each branch may also have sub branches. For example release 3-5-4 refers to the 
fourth checkin in the fifth sub branch of the third main branch. 
This hierarchy can go upto any number of levels. 

If a level is missing it is considered as level 0 in that hierarchy. 
For example 3-5-7 is  same as 3-5-7-0 or even same as 3-5-7-0-0. 
The higher numbers denote more recent releases. 

For example 3-5-7-1 is more recent than 3-5-7 but less recent than 3-6.

Input Format:
-------------
A single line space separated strings, list of releases 

Output Format:
--------------
Print the latest release of the software.


Sample Input-1:
---------------
1-2 1-2-3-0-0 1-2-3

Sample Output-1:
----------------
1-2-3

Sample Input-2:
---------------
3-5-4 3-5-7 3-5-7-1 3-5-7-0-0 3-6

Sample Output-2:
----------------
3-6
'''

#Solution:

def compareVersion(version1, version2) :
        
    str1 = version1.split("-")
    str2 = version2.split("-")
       
    len1 = len(str1)
    len2 = len(str2)
        
    for i in range(max(len1,len2)):
            
        i1 = int(str1[i]) if i < len1 else 0
        i2 = int(str2[i]) if i < len2 else 0
            
        if i1 != i2:
            return 1 if i1 >i2 else -1
            
    return 0

l = input().split()
ans = l[0]
for i in range(1, len(l)):
    res = compareVersion(ans, l[i])
    if res == -1:
        ans = l[i]
    elif res == 0:
        ans = ans if len(ans) < len(l[i]) else l[i]
print(ans)