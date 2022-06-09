/*

Mr Robert is working with strings.

He selected two strings S1 and S2, may differ in length,

consists of lowercase alphabets only.



Mr Robert has to update the strings S1, S2 to meet any one of the criteria:

	- All the alphabets in S1 should be less than all the alphabets in S2.

	- All the alphabets in S2 should be less than all the alphabets in S1.

	- Both S1 and S2 should have only one distinct alphabet in it.

To Achieve, one of the criteria, you are allowed to replace any one letter in 

the string with any other lowercase alphabet.



Your task is to help Mr Robert, to find the minimum replacements to be done to 

update the strings S1 and S2 to meet one of the criteria mentioned above.





Input Format:

-------------

Two space separated strings S1 and S2.



Output Format:

--------------

Print an integer, minimum number of replacements.





Sample Input-1:

---------------

apple ball



Sample Output-1:

----------------

3



Explanation:

------------

Consider the best way to make the criteria true:

- Update S2 to "baaa" in 2 replacements, and Update S1 to "cpple" in 1 replacement

then every alphabet in S2 is less than every alphabet in S1.

        (OR)

- Update S1 to "ppppp" in 3 replacements, then every alphabet in S2 is less 

than every alphabet in S1.





Sample Input-2:

---------------

kmit kmec



Sample Output-2:

----------------

2


*/

//Solution

import java.util.*;
class Day_76_P_3{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s1=sc.next();
        String s2=sc.next();
        int[] s1Count = new int[26];
        int[] s2Count = new int[26];
        int s1_Max = 0;
        for (int i = 0; i < s1.length(); i++)
            s1_Max = Math.max(s1_Max,++s1Count[s1.charAt(i) - 'a']);
        
        int s2_Max = 0;
        for (int i = 0; i < s2.length(); i++) 
            s2_Max = Math.max(s2_Max, ++s2Count[s2.charAt(i) - 'a']);
        
        int result = s1.length() - s1_Max + s2.length() - s2_Max,s1Till = 0,s2Till = 0;
        for (int i = 0; i < 25; i++) {
            s1Till +=s1Count[i];
            s2Till += s2Count[i];
            result = Math.min(result, s2Till + s1.length() - s1Till);
            result = Math.min(result, s1Till + s2.length() - s2Till);
        }
         System.out.println(result);
    }
}