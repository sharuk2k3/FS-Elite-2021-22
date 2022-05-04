'''


A triplet is a subsequence of list of elements.
and length of the subsequence should be 3.
 i.e., List is [1,2,3,4,5,6], triplets possible are
[1,2,3], [1,2,4], [1,2,5], [1,2,6] and so on.
 
Ganesh is given a list of integers, nums[], and three integers x,y,z.
He need to findout the triplets(nums[i],nums[j],nums[k]),
which are following the conditions given below:
	* 0 <= i < j < k < nums.length
	* abs(nums[i] - nums[j]) <= x
	* abs(nums[j] - nums[k]) <= y
	* abs(nums[i] - nums[k]) <= z

Your task is to help Ganesh to find the number of such triplets possible.

Input Format:
-------------
Line-1: Four space separated integers, N, x, y, z.
Line-2: N space separated integers, nums[].

Output Format:
--------------
Print an integer, number of triplets.


Sample Input-1:
---------------
6 7 2 3
3 0 1 1 9 7

Sample Output-1:
----------------
4

Explanation:
------------
There are 4 triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Satisfying given conditions

Sample Input-2:
---------------
5 0 0 1
1 1 2 2 3

Sample Output-2:
----------------
0

Explanation:
------------
There is no triplet, which satisfy the given conditions.



'''