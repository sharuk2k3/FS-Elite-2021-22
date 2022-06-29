'''

Gunith is interested in series and sequence problems in Maths.
Gunith is given an array A of integers, he wants to find out 
a Sequence, which is long and subsequence of given array.

Subsequence AS is the list AS[i], AS[i1], AS[i2], .... AS[ik], from the array, 
where 0 <= i< i1 < i2 < ..<ik < A.length

The sequence S has to follow this rule, S[i+1] - S[i] are all the same value 
(for 0 <= i < S.length - 1 ), and Sequence S can be formed from A

Find out the Max possible length of the Longest Sequence.

Input Format:
-------------
Line-1 -> An integer N, number of array elements
Line-2 -> N space separated integers, elements of the array.

Output Format:
--------------
Print an integer as your result.


Sample Input-1:
---------------
4
2 6 10 14

Sample Output-1:
----------------
4


Sample Input-2:
---------------
7
2 5 6 8 10 11 14

Sample Output-2:
----------------
5

Explanation:
------------
The longest possible arithmetic series is 2 5 8 11 14.



'''

#Solution:
#Using Dynamic Programming

def max_sequence(n,arr):
    if n <= 1:
        return n 
        
    ap = [None] * n
    for i in range(n):
        ap[i] = dict()

    for j in range(1, n):
        for i in range(0, j):
            diff = arr[j] - arr[i]
            ap[j][diff] = ap[i].get(diff, 1) + 1

    ans = 0

    for item in ap[1:]:
        vals = max(item.values())
        ans = max(ans, vals)

    return ans 
    

if __name__ == '__main__':
    n=int(input())
    arr= list(map(int, input().split()))
    print(max_sequence(n,arr))