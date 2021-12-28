/*
Indian Army setup some military-camps, sitauted at random places at LAC in Galwan.
There exist a main base camp connected with other base camps as follows:
Each military-camp is connected with atmost two other military-camps.
Each military-camp will be identified with an unique ID,(an integer).

To safeguard all the military-camps, Govt of India planned to setup protective 
S.H.I.E.L.D. Govt of India ask your help to build the S.H.I.E.L.D that should 
enclose all the militar-camps.

You are given the IDs of the military-camps as binary tree. 
Your task is to find and return the military camp IDs, those are on the edge of 
the S.H.I.E.L.D in anti-clockwise order.

Implement the class Solution:
   1. public List<Integer> compoundWall(BinaryTreeNode root): returns a boolean value.
  

NOTE:
'-1' in the IDs indicates no military-camp (NULL).


Input Format:
-------------
space separated integers, military-camp IDs.

Output Format:
--------------
Print all the military-camp IDs, which are at the edge of S.H.I.E.L.D.


Sample Input-1:
---------------
5 2 4 7 9 8 1

Sample Output-1:
----------------
[5, 2, 7, 9, 8, 1, 4]


Sample Input-2:
---------------
11 2 13 4 25 6 -1 -1 -1 7 18 9 10

Sample Output-2:
----------------
[11, 2, 4, 7, 18, 9, 10, 6, 13]

case =1
input =2 1 3 6 4 -1 9
output =[2, 1, 6, 4, 9, 3]

case =2
input =5 2 4 7 9 8 1
output =[5, 2, 7, 9, 8, 1, 4]

case =3
input =1
output =[1]

case =4
input =11 2 13 4 25 6 -1 -1 -1 7 18 9 10
output =[11, 2, 4, 7, 18, 9, 10, 6, 13]

case =5
input =1 2 4 3 5 6 9 12 8 14 11 6 2 9 13
output =[1, 2, 3, 12, 8, 14, 11, 6, 2, 9, 13, 9, 4]

case =6
input =5 -1 1 -1 -1 3 6
output =[5, 3, 6, 1]

case =7
input =11 8 6 1 7 5 16 3 20 18 14 22 10 4 2 17 15 19 12
output =[11, 8, 1, 3, 17, 15, 19, 12, 18, 14, 22, 10, 4, 2, 16, 6]

case =8
input =1 3 5 7 -1 -1 9 8 -1 -1 -1 -1 -1 -1 6 10 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 13
output =[1, 3, 7, 8, 10, 13, 6, 9, 5]



*/


//https://www.lintcode.com/problem/878/description
//SOLUTION


/*
//TreeNode Structure for Your Reference..

class BinaryTreeNode{
	public int data; 
	public BinaryTreeNode left, right; 
	public BinaryTreeNode(int data){
		this.data = data; 
		left = null; 
		right = null; 
	}
}

*/

import java.util.*;
class Day_9_P_3{
    public List<Integer> compoundWall(BinaryTreeNode root) {
        // Implement Your Code here..
        List<Integer> nodes = new ArrayList<>();
        if (root == null || root.data == -1) {
            return nodes;
        }
        nodes.add(root.data);
        leftBoundary(root.left, nodes);
        addLeaves(root.left, nodes);
        addLeaves(root.right, nodes);
        rightBoundary(root.right, nodes);
        return nodes;
    }
    public void leftBoundary(BinaryTreeNode root, List<Integer> nodes) {
        if ((root == null || root.data == -1) || ((root.left == null || root.left.data == -1) && (root.right == null || root.right.data == -1))) {
            return;
        }
        nodes.add(root.data);
        if ((root.left == null) || (root.left.data == -1)) {
            leftBoundary(root.right, nodes);
        } else {
            leftBoundary(root.left, nodes);
        }
        
    }

    public void rightBoundary(BinaryTreeNode root, List<Integer> nodes) {
        if ((root == null || root.data == -1) || ((root.left == null || root.left.data == -1) && (root.right == null || root.right.data == -1))) {
            return;
        }
        if ((root.right == null) || (root.right.data == -1)) {
            rightBoundary(root.left, nodes);
        } 
        else {
            rightBoundary(root.right, nodes);
        }
        nodes.add(root.data);
    }

    public void addLeaves(BinaryTreeNode root, List<Integer> nodes) {
        if ((root == null || root.data == -1)) {
            return;
        }
        if ((root.left == null || root.left.data == -1) && (root.right == null || root.right.data == -1)) {
            nodes.add(root.data);
            return;
        }
        addLeaves(root.left, nodes);
        addLeaves(root.right, nodes);
    }
}