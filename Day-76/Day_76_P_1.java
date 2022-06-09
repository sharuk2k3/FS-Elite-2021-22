/*

Sampoornesh Babu is working with Strings.
He is trying to form a palindrome using two strings P and Q.
The rules to form the palindrome are as follows:
	- Divide the strings P and Q into two parts, and length of P and Q are same.
	- Division of P and Q should be done at same index position.
	- After Division P -> P1 + P2 and Q -> Q1 + Q2, where + indicates concatenation.
	- Now, check whether P1 + Q2 or Q1 + P2 forms a palindrome or not.
	- if palindrome is formed print 'true', otherwise 'false'. 

For Example: 'job' can be divided in the following ways:
""+"job", "j"+"ob",  "jo"+"b", "job"+"".

Your task is to help Sampoornesh Babu to find whether palindrome can be 
formed with the strings P and Q.

Input Format:
-------------
Two space separated strings P and Q

Output Format:
--------------
Print a boolean value, whether can you form a palindrome or not.


Sample Input-1:
---------------
mortal carrom

Sample Output-1:
----------------
true

Explanation:
------------
Divide P="mortal" and Q="carrom" at index 3 as follows:
    P -> "mor" + "tal", P1 = "mor" and P2 = "tal"
    Q -> "car" + "rom", Q1 = "car" and Q2 = "rom"

P1 + Q2 = "morrom" is a palindrome,so print true.


Sample Input-2:
---------------
romans carrom

Sample Output-2:
----------------
false


*/

//Solution:

import java.util.*;

public class Day_76_P_1 {

    
    public static String word_break(String s1,String s2){
        int flag=0;
        StringBuilder sb1=new StringBuilder();
        StringBuilder sb2=new StringBuilder();
        if(s1.length()!=s2.length()){
            return "false";
        }
        for(int i=0;i<s1.length();i++){
           sb1=new StringBuilder(s1.substring(0,i)+s2.substring(i)); 
           sb2=new StringBuilder(s1.substring(i)+s2.substring(0,i));
           if(isrev(sb1)||isrev(sb2)){
               flag=1;
           }
        }
        if(flag==1){
            return "true";
        }
        return "false";
    }
    public static boolean isrev(StringBuilder s1){
        StringBuilder sbt=new StringBuilder(s1.toString());
        StringBuilder sbt2=new StringBuilder(sbt);
        if(sbt.toString().equals(sbt2.reverse().toString())){
            return true;
        }
        return false;
    }
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        String s1=sc.next();
        String s2=sc.next();
        System.out.print(word_break(s1,s2));
    }
    
    
}
