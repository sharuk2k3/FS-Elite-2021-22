/*

You are given an alphanumeric word W.
You need find the number of words that can be formed from W.

The words have the following properties:
    - It should be a substring of W of any length, minimum 1.
    - All the letters in the word should be same.


Input Format:
-------------
Single String W.

Output Format:
--------------
Print an integer, the number of words can be formed


Sample Input-1:
---------------
daddy
 
Sample Output-1:
----------------
6

Explanation:
------------
The words are : d, a, d, d, dd, y


Sample Input-2:
---------------
binary11100

Sample Output-2:
----------------
15

Explanation:
------------
The words are : b, i, n, a, r, y, 1, 1, 1, 11, 11, 111, 0, 0, 00 

*/

import java.util.*;
public class Day_8_P_1 {
    
    static String str;
    static int count = 0;
    static void calc(int i){
        if(i==str.length() || str.charAt(i-1)!=str.charAt(i) ){}
        else{
            calc(i+1);
        }
        count++;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        str = sc.next();
        for(int i=0;i<str.length();i++)
            calc(i+1);
        System.out.print(count);
    }
}


/*
//CPP SOLUTION J



#include<iostream>
#include<map>
using namespace std;
int main(){
    string str;
    cin>>str;
    map<char,int> count;
    int sum=1;
    char prev=str[0];
    count[str[0]]=1;
    for(int i=1;i<str.length();i++){
        int x=0;
        if(str[i]==prev){
            count[str[i]]++;
            sum=sum+count[str[i]];
        }
        else{
            count[prev]=0;
            count[str[i]]=1;
            sum=sum+count[str[i]];
            prev=str[i];
        }
    }
    cout<<sum;
}
*/
