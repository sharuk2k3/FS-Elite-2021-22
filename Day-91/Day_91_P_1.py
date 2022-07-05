'''

Mr.Bean is given a list of N integers as List[], consists of only positive 
integers from 0 to 10^9. 

Mr.Bean has generated all the contiguous sub lists of List[]. On each sublist, 
He perforemd Bitwise OR operation on all the integers in the sublist and stored 
the final answer of that in the list answers[].

Your task is to help Mr.Bean to return the number of unique values in answers[]. 

Input Format:
-------------
Line-1: An integer N
Line-2: N space sepaarted integers, List[].

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
3
2 3 2

Sample Output-1:
----------------
2

Explanation: 
------------
Sublists are [2],[3],[2],[2,3],[3,2],[2,3,2] 
and answers[] after performing bitwise OR: [2,3,2,3,3,3]
The number of unique values in answers[] are 2.


Sample Input-2:
---------------
4
2 3 2 1

Sample Output-2:
----------------
3

Explanation: 
------------
Sublists are [2],[3],[2],[1],[2,3],[3,2],[2,1],[2,3,2],[3,2,1],[2,3,2,1] 
and answers[] after performing bitwise OR: [2,3,2,1,3,3,3,3,3,3]
The number of unique values in answers[] are 3.




'''

#Solution:

def subarrayBitwiseORs(n,arr):
    ans, vals = set(), set()
    for i in arr:
        vals = {i|j for j in vals} | {i}
        ans |= vals
    return len(ans)

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(subarrayBitwiseORs(n,arr))