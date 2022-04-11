/*
Somayajaulu working with strings.
He is given a string S, string S contains repeated characters.
Somayajulu decided to delete all the repeated characters, 
such that each character in S should appears once and only once.
He is deleting the characters from S in such a way that, 
the final string should be the smallest string among all possibilities

You are given the string S.
Your task is to help Somayajulu to find the smallest string possible 
after deleting the repeated characters from S.

Input Format:
-------------
A string S.

Output Format:
--------------
Print a string, smallest string after deleting repeated characters.


Sample Input-1:
---------------
attitude

Sample Output-1:
----------------
aitude


Sample Input-2:
---------------
cbabacbabca

Sample Output-2:
----------------
abc



*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    string s;
    cin>>s;
    
    int n = s.length();
    vector<int> freq(26,0);
    
    for(int i=0;i<n;i++){
        freq[s[i]-'a']++;
    }
    
    stack<char> st;
    map<char,int> m;
    
    for(int i=0;i<n;i++){
        freq[s[i]-'a']--;
        if(m[s[i]]){
            continue;
        }
        while(st.size() && st.top()>s[i]){
            if(freq[st.top()-'a']>=1){
                m[st.top()]=0;
                st.pop();
            }
            else{
                break;
            }
        }
        st.push(s[i]);
        m[s[i]]=1;
    }
    string ans;
    while(!st.empty()){
        ans+=st.top();
        st.pop();
    }
    reverse(ans.begin(),ans.end());
    cout<<ans<<endl;
}