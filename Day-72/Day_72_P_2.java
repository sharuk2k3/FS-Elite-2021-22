/*

A set of computers connected with each other and formed a network with the 
following rule, one computer can directly connected with atmost two computers only.
Each computer is assigned with an ID, the computer ID's may be repeated.

You are given the entire network as a binary seach tree, (i.e., the computer ID 
is greater than its left connected computer's ID and lesser than its right 
connected computer ID )
Your task is to transform the network into a single row of computers,
The transforming process follows the below order:
    - For transformation, use the same network tree structure.
    - The row of computers have to be connected with each other, and form
        a circular doubly linked list, where left pointer points to the 
        previous computer, and right pointer points to the next one.
    - The computer ID of current computer should be greater than its left 
      computer ID and should be lesser than its right computer ID.
    
Implement the class Solution:
   1. public Node treeToCircularList(Node root) : transform the tree.


Input Format:
-------------
Single line of space separated integers, network ID's in the form the BST.

Output Format:
--------------
Print the computer IDs from left to right.


Sample Input:
-------------
4 2 3 1 5 6 7

Sample Output:
--------------
1 2 3 4 5 6 7



*/

public class Day_72_P_2 {
    
}
