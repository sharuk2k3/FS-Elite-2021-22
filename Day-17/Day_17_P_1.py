'''

Mallika taught a new fun time program practice for Engineering Students.
As a part of this she has given set of numbers, and asked the students 
to find the sum of numbers between indices S1 and S2 (S1<=S2),
both S1 and S2 inclusive.

There are P Students in the class, numbered from 1 to P. Each student is
given set of indices and that student has to find the sum of the numbers 
between the indices and print the result.

And return the answer in the same order of

Input Format:
-------------
Line-1: Two integers N and P, N is length of set of numbers.
		where 1<= N <= 1000
Line-2: N space separated integers, array set[]
Next P lines: Two integers S1 and S2, index positions 
		where 0 <= S1 <= S2 < N
		and 1<= set[i] <= 100000

Output Format:
--------------
Print the sum of numbers between indices(s1, s2) given to each student.


Sample Input-1:
---------------
8 2
115053 59099 681359 526248 123844 612168 920784 591204
2 6
1 5

Sample Output-1:
----------------
2864403
2002718


'''

#TOPIC Segment Tree
#SOLUTION

#CPP
'''

#include <iostream>
#include<bits/stdc++.h>
using namespace std;


void build(int x,int l,int r,vector<int>& temp,vector<int>& tree){
    if(l>r){
        return;
    }
    if(l==r){
        tree[x] = temp[l];
        return;
    }
    int mid = (l+r)/2;
    
    build(2*x+1,l,mid,temp,tree);
    build(2*x+2,mid+1,r,temp,tree);
    tree[x]=tree[2*x+1]+tree[2*x+2];
    
}

int get(int x,int l,int r,int i,int j,vector<int>& tree){
    
    if(l>j || r<i){
        return 0;
    }
    if(l>=i && r<=j){
        return tree[x];
    }
    int mid = (l+r)/2;
    
    return (get(2*x+1,l,mid,i,min(mid,j),tree) + get(2*x+2,mid+1,r,max(mid+1,i),j,tree));
    
}



int main()
{
    int n,p;
    cin>>n>>p;
    
    vector<int> temp(n);
    for(int i=0;i<n;i++){
        cin>>temp[i];
    }
    vector<int> tree(4*n,0);
    
    build(0,0,n-1,temp,tree);
    
    for(int i=0;i<p;i++){
        
        int l,r;
        cin>>l>>r;
        
        cout<<get(0,0,n-1,l,r,tree)<<endl;
        
    }
    
    
    

    return 0;
}

'''