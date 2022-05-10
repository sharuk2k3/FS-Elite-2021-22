/*'''


Akhila is given a string S, Where S conatins only [aeiou] letters.
A special subsequence defined as a sequence of letters derived from S
that contains all five vowels in order. It means a specail subsequence 
will have one or more a's followed by the one or more e's followed by 
one or more i's followed by one or more o's followed by one or more u's.

Your task is to help Akhila to return the length of the longest special 
subsequence in S.

Input Format:
-------------
Your code should be read input from the given attached file as a string (no line breaks)

Output Format:
--------------
An integer, the length of longest subsequence.

Sample input-1:
---------------
aeeiooua

Sample Output-1:
----------------
7

Explanation:
------------
Given S = "aeeiooua", then "aeiou" and "aeeioou" are special subsequences
but "aeio" and "aeeioua" are not


Sample input-2:
---------------
aeiaaioooaauuuaeiou

Sample Output-2:
----------------
10




'''*/

#include<bits/stdc++.h>
using namespace std;


int rep(int i,int j,int n,string& s,vector<vector<int>>& dp,vector<char>& letters){
    
    if(j==5){
        return 0;
    }
    if(i==n){
        if(j<4){
            return INT_MIN;
        }
        return 0;
    }
    if(dp[i][j]!=-1){
        return dp[i][j];
    }
    int count=0;
    if(s[i]==letters[j]){
        count++;
    }
    
    if(count){
        return dp[i][j]= 1+max(rep(i+1,j+1,n,s,dp,letters),rep(i+1,j,n,s,dp,letters));
    }
    else{
        return dp[i][j] = rep(i+1,j,n,s,dp,letters);
    }
    
}

int main(){
    
    
    string s;
    cin>>s;
    
    vector<char> letters;
    letters.push_back('a');
    letters.push_back('e');
    letters.push_back('i');
    letters.push_back('o');
    letters.push_back('u');
    
    int n = s.length();
    vector<vector<int>> dp(n+2,vector<int>(5,-1));
    cout<<rep(0,0,n,s,dp,letters)<<endl;
    
    
    
    
    
}