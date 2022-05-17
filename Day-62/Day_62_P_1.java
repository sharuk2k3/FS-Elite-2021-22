/*


Mr Shravan is working with Strings.
He is given a string S, and a list of words.
He wants to find a word which is maximum in length and 
appears first in lexicographical order, And the word is a subsequence of S.

Your task is to help Mr Shravan to find such a word from the given list of words.
If there is no such word, print "No Word".

Input Format:
-------------
Line-1: A string S.
Line-2: Space separated strings, words[].

Output Format:
--------------
Print a string result.



Sample Input-1:
---------------
rascapepurple
ape cape racer app apple

Sample Output-1:
----------------
apple


Sample Input-2:
---------------
abcdefhijk
bca abd abc dfe def ghi

Sample Output-2:
----------------
abc

Sample Input-3:
---------------
vivid
viva diva diya

Sample Output-3:
----------------
No Word



*/

import java.util.*;

class Day_62_P_1 {
    
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