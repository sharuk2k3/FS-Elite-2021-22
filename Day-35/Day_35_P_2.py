'''

Venkat wants to create a unique name for his child, to do that he is referring 
two names, one is traditonal name(TN) and other is modern name(MN).

He is planning to create unique name(UN), using the following ways:
    - if traditional name TN is non empty, then add the first letter L of TN 
    to unique name UN and remove the letter L from traditional name TN
	e.g., if TN = "havi" and UN="anvika", then after adding L to UN and remove L 
	from TN, the names updated as UN="hanvika", TN="avi".
   
   - if modern name MN is non empty, then add the first letter L of MN 
    to unique name UN and remove the letter L from modern name MN
    e.g., if MN = "ram" and UN="ao", then after adding L to UN and remove L 
	from MN, the names updated as UN="rao", MN="am".
	
You are given two names, TN and MN, 
Your task is to help venkat to generate the unique name for his child,
and the name should be largest in the dictionary order.

For example, "kmit" is larer than "kmec", as third letter is greater in "kmit".

Input Format:
-------------
Two space separated names, TN and MN.

Output Format:
--------------
Print a string, the laregst unique name possible.


Sample Input-1:
---------------
sudha vivid

Sample Output-1:
----------------
vsuividhda


Sample Input-2:
---------------
appa banana

Sample Output-2:
----------------
bappananaa


'''

#Solution CPP
'''

#include<bits/stdc++.h>
using namespace std;
int n,m;
string a,b;


string rep(map<pair<int,int>,string>& m1,int i,int j){
    
    if(i==n && j==m){
        return "";
    }
    if(i==n){
        return m1[{i,j}] =b[j]+rep(m1,i,j+1);
    }
    if(j==m){
        return m1[{i,j}] =a[i]+rep(m1,i+1,j);
    }
    
    if(a[i]>b[j]){
        return m1[{i,j}] = a[i]+rep(m1,i+1,j);
    }
    if(b[j]>a[i]){
        return m1[{i,j}] = b[j]+rep(m1,i,j+1);
    }
    string ans1,ans2;
    ans1=a[i]+rep(m1,i+1,j);
    ans2 = b[j]+rep(m1,i,j+1);
    
    if(ans1>=ans2){
        return m1[{i,j}] = ans1;
    }
    return m1[{i,j}] =ans2;
    
    
    
}

int main(){
    
    
    cin>>a>>b;
    
    n = a.length();
    m = b.length();
    
    map<pair<int,int>,string> m1;
    
    cout<<rep(m1,0,0)<<endl;
    
    
    
}

'''