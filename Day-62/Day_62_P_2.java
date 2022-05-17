/*


You are given two words W1 and W2.
You need find all the mapping of W2 in W1, and 
return all the statrting indices of the mappings.

The mapping of the words w2 and w1 is as follows:
	- A shuffled word contains all the characters as original word.
	The length of the words and occurrence count of each character are same.
	- find shuffled word of W2 as a substring in W1, and 
	return the starting index of substring.


Input Format:
-------------
Single line space separated strings, two words.

Output Format:
--------------
Print the list of integers, indices.


Sample Input-1:
---------------
abcabcabc abc
 
Sample Output-1:
----------------
[0, 1, 2, 3, 4, 5, 6]



Sample Input-2:
---------------
bacacbacdcab cab

Sample Output-2:
----------------
[0, 3, 4, 5, 9]




*/

import java.util.*;

class Day_62_P_2{

    public static boolean isSub(String s,String b){
        int j=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)==b.charAt(j)) j++;
             if(j==b.length()){
                return true;
            } 
        }
        return false;
    }
    
    public static void main(String args[]){
        
        Scanner sc=new Scanner(System.in);
        
        String s=sc.nextLine();
        String words=sc.nextLine();
        
        String arr[]=words.split(" ");
        
        Arrays.sort(arr,(a,b)->{if(a.length()!=b.length())
                                    return b.length()-a.length();
                                else
                                return a.compareTo(b);});
        
        
    for(int i=0;i<arr.length;i++){
        if(isSub(s,arr[i]))
        {
            System.out.print(arr[i]);
            System.exit(0);
        }
    }
    System.out.print("No Word");
    }
}
