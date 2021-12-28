/*Mr Rakesh is interested to work on Data Structures.
He has constructed a BinaryTree-BT.

He asked his friend Anil to check whether BT is self mirror tree or not.
Can you help Anil to find and return "true" if the given BT is a self mirror tree,
otherwise return "false".

Implement the class Solution:
   1. public boolean isSelfMirrorTree(BinaryTreeNode root): returns a boolean value.
  
NOTE:
	- In the tree '-1', indicates empty(null).
   
Input Format:
-------------
A single line of space separated integers, values at the treenode

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
2 1 1 2 3 3 2

Sample Output-1:
----------------
true


Sample Input-2:
---------------
2 1 1 -1 3 -1 3

Sample Output-2:
----------------
false
*/


//SOLUTION HERE


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

class Solution {
    public boolean isSelfMirrorTree(BinaryTreeNode root) {
        // Implement Your Code here..
        return isSelfMirrorTree(root.left,root.right);
    }


public boolean isSelfMirrorTree(BinaryTreeNode t1, BinaryTreeNode t2) {
        if (t1 == null && t2 == null) {
            return true;
        }
        if (t1 == null || t2 == null) {
            return false;
        }
        if (t1.data != t2.data) {
            return false;
        }
        return isSelfMirrorTree(t1.left, t2.right) && isSelfMirrorTree(t1.right, t2.left); 
    }
}
