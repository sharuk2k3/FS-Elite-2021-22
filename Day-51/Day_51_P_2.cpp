/*'''


Chitti Naidu is a school kid, writing a series of numbers in a special way.

The series is looks like following: 
	- For example, starting number is 25
	- Next number in the series is, count of digit groups like "one 2 and one 5', written as 1215.
	- Next number in the series is, count of digit groups like "one 1, one 2, one 1 and one 5', 
	written as 11121115 and so on.

You will be given a string S (A number), an integer N, where S is the starting number of series, 
You need to find the N-th term in the series. 

Note: Each term of the series of integers will be represented as a string.

Input Format:
-------------
A String S and an integer N

Output Format:
--------------
Print the N-th term in the series starts with S.


Sample Input-1:
---------------
25 3

Sample Output-1:
----------------
11121115


Sample Input-2:
---------------
21 4

Sample Output-2:
----------------
312211

Explanation:
---------------
1st term, S = 12
2nd term is "one 2 one 1" -> "1211",
3rd term is "one 1, one 2, two 1's " -> "111221"
Finally 4th term is  "three one's, two 2's, one 1" -> "312211".




'''*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    string s;
    cin>>s;
    
    int n;
    cin>>n;
    
    
    for(int i=0;i<n-1;i++){
        
        string ans;
        int j=0;
        while(j<s.length()){
            char c = s[j];
            int count=0;
            while(j<s.length() && s[j]==c){
                count++;
                j++;
            }
            
            ans+=to_string(count);
            ans+=c;
            
            
            
        }
        
        s=ans;
        
    }
    cout<<s<<endl;
    
}