'''

You are given a set of N integers, and a value to find F. Initially a variable, 
'total' is set to 0. You can perform either addition(+) or subtraction(-)
of every integer from the set to the 'total'. The resultant total should be
equal to the value F.

Your task is to find out the number of ways, you can make the 'total' equal to
the value F.

Input Format:
-------------
Line-1: Two integers N and F.
Line-2: N space separated integers 

Output Format:
--------------
Print an integer, number of ways.


Sample Input:
---------------
5 3
1 1 1 1 1

Sample Output:
----------------
5

Explanation:
------------
total = -1+1+1+1+1 = 3 -> total=value-F
total = +1-1+1+1+1 = 3 -> total=value-F
total = +1+1-1+1+1 = 3 -> total=value-F
total = +1+1+1-1+1 = 3 -> total=value-F
total = +1+1+1+1-1 = 3 -> total=value-F

NOTE: + means addition, - means subtraction


'''

def SumWays(nums,s):
    Sum=sum(nums)
    if len(nums)==1 and abs(nums[0]==abs(s)):
        return 1
    if len(nums)==1 and abs(nums[0]!=abs(s)):
        return 0
    if (s>Sum or -s<-Sum or (s+Sum)%2==1): return 0
    dp=[0]*((s+Sum)//2+1)
    dp[0]=1
    for num in nums:
        for i in range(len(dp)-1,num-1,-1):
            dp[i]+=dp[i-num]
    return dp[len(dp)-1]
n,s=map(int,input().split())
nums=list(map(int,input().split()))[:n]
print(SumWays(nums,s))
