/*

Ms Tejaswi is given a Triply Linked list (TLL), The Triply linked list contains
three pointers left, right and down.

The TLL is created in multi level format as follows:
    - In each level only one Node will be connected to another Node 
      through down pointer.
    - For the remaining Nodes in that level, the down pointer ponits to null. 

Your task is to convert the given TLL to DLL (Doubly Linked List) as follows:
    - The priority for processing the TLL pointers are
      1. down, 2.right, 3.left
    - You need to follow Depth First approach, and convert the TLL to DLL

You need to implement the Solution Class:
    - public Node convertToDLL(Node head) : return the head node.

NOTE: All the levels should be processed first, before you process the right node.

NOTE: 
- The numbers printed on the board in each row and each column are
  in increasing order. And all the numbers are unique.

Input Format:
-------------
Single line comma',' separated data of the list, integer

Output Format:
--------------
Print the modified doubly linked list as given sample.


Sample Input-1:
---------------
1,2,3,null,null,4,5,6,null,null,7,8,9,null,null,10,11,12

Sample Output-1:
----------------
1->2->4->5->7->8->10->11->12->9->6->3

Explanation:
------------
Please look the hint


Sample Input-2:
---------------
1,2,3,4,5,null,null,null,6,7,8,9,null,null,10,11

Sample Output-2:
----------------
1->2->3->6->7->10->11->8->9->4->5


case =1
input =1,2,3,null,null,4,5,6,null,null,7,8,9,null,null,10,11,12
output =1->2->4->5->7->8->10->11->12->9->6->3

case =2
input =1,2,3,4,5,null,null,null,6,7,8,9,null,null,10,11
output =1->2->3->6->7->10->11->8->9->4->5

case =3
input =1,2,null,3
output =1->3->2

case =4
input =1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12
output =1->2->3->7->8->11->12->9->10->4->5->6

case =5
input =1,2,3,4,5,6,7,8,null,null,null,10,11,12,13,14,15,null,null,null,null,null,16,17,18,19,20
output =1->2->3->10->11->12->13->14->16->17->18->19->20->15->4->5->6->7->8

case =6
input =1,2,3,null,4,5,6,null,11,13,14,null,null,null,15,16,17,null,7,8,9,null,null,10,23,24
output =1->4->11->13->14->15->7->8->10->23->24->9->16->17->5->6->2->3

case =7
input =1,2,22,23,24,null,null,3,4,20,21,null,null,5,6,7,18,19,null,null,null,8,9,16,17,null,null,10,11,15,null,null,12,13,14
output =1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->16->17->18->19->20->21->22->23->24

case =8
input =4,3,2,1,null,8,7,6,5,null,null,12,11,10,null,null,13,12
output =4->8->7->12->11->13->12->10->6->5->3->2->1




*/


//SOLUTION


/*
//Structure of the node in Triply Linked List(TLL)

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node down;
}

*/


import java.util.*;
class Day_9_P_4{
    public Node convertToDLL(Node head) {
        //implement this method
        if(head == null){
            return head;
        }
        if(head.down!=null){
            Node next = head.right;
            Node temp = convertToDLL(head.down);
            head.down = null;
            head.right  = temp;
            temp.left = head;
            while(temp.right!=null){
                temp = temp.right;
            }
            temp.right = next;
            if(next!=null) next.left = temp;   
        }else{
            head.right= convertToDLL(head.right);
        }
        return head;
    }
}
