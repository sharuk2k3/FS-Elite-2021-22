/*


There are P people in a Village, some of the people are relatives, 
others are not. Their relationship is transitive. 

For example, 
if A is a direct relative of B, and B is a direct relative of C, 
then A is an indirect relative of C. And we define a Relation Chain as 
a group of people who are direct or indirect relatives.

Given a P*P matrix R represents the relationship between people 
in the village. If R[i][j] = 1, then the i and j persons are direct 
relatives with each other, otherwise not. 

Your task is to find out the total number of Relation Chains 
among all the people.

Input Format:
-------------
Line-1 : An integer P, number of people
Next P lines : P space separated integers.

Output Format:
--------------
Print an integer, the total number of Relation Chains


Sample Input-1:
---------------
3
1 1 0
1 1 0
0 0 1

Sample Output-1:
----------------
2

Explanation:
------------
The 0-th and 1-st people are direct relatives, so they are in a relation chain.
The 2-nd person himself is in a relation chain. So return 2.


Sample Input-2:
---------------
3
1 1 0
1 1 1
0 1 1

Sample Output-2:
----------------
1

Explanation:
------------
The 0-th and 1-st people are direct relatives, 1-st and 2-nd people 
are direct relatives. So, the 0-th and 2-nd people are indirect relatives.
All of them in the same relative chain. So return 1.




*/

#include<bits/stdc++.h>
using namespace std;

int find(int a,vector<int>& par){
    
    if(par[a]==-1){
        return a;
    }
    return par[a]=find(par[a],par);
    
}

void uni(int a,int b,vector<int>& par){
    
    a=find(a,par);
    b=find(b,par);
    if(a!=b){
        par[b]=a;
    }
    
}


int main(){
    
    int n;
    cin>>n;
    
    vector<vector<int>> temp(n+2,vector<int>(n+2));
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>temp[i][j];
        }
    }
    
    vector<int> par(n+2,-1);
    int count=0;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(temp[i][j] && i!=j){
                uni(i,j,par);
            }
        }
    }
    for(int i=1;i<=n;i++){
        if(par[i]==-1){
            count++;
        }
    }
    cout<<count<<endl;
}