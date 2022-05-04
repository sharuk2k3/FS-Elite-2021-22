'''


Bubloo is working with Binary Trees.
The elements of the tree is given in the level order format.
Bubloo has to find the number of edges between two nodes with data E1 & E2
in the tree.

You will be given the root of the binary tree. Your task is to help Mr Bubloo 
to find the number of edegs between two nodes E1 and E2.

Your task is to implement the class Solution:
	- public boolean findDistance(BinaryTreeNode root, int e1, int e2):
	  return an integer value, the number of edegs between e1 and e2.
	
NOTE: 
All the nodes have distinct data value.
Please do ignore the node with data=-1, and treat that node as null node.

Input Format:
-------------
Space separated integers, elements of the tree.

Output Format:
--------------
Print an integer value.


Sample Input-1:
---------------
1 2 4 3 5 6 7 8 9 10 11 12
4 8

Sample Output-1:
----------------
4

Explanation:
------------
The edegs between 4 and 8 are: [4,1], [1,2], [2,3], [3,8]


Sample Input-2:
---------------
1 2 4 3 5 6 7 8 9 10 11 12
6 6

Sample Output-2:
----------------
0

Explanation:
------------
No edegs between 6 and 6.



'''