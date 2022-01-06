'''

In Hyderabad after a long pandemic gap, the Telangana Youth festival Is 
Organized at HITEX. In HITEX, there are a lot of programs planned. During 
the festival in order to maintain the rules of Pandemic, they put a 
constraint that one person can only attend any one of the programs in 
one day according to planned days.

Now it’s your aim to implement the "Solution" class in such a way that 
you need to return the maximum number of programs you can attend according 
to given constraints.

Explanation:
You have a list of programs ‘p’ and days ’d’, where you can attend only 
one program on one day. Programs [p] = [first day, last day], 
p is the program's first day and the last day.


Input Format:
-------------
Line-1: An integer N, number of programs.
Line-2: N comma separated pairs, each pair(f_day, l_day) is separated by space.

Output Format:
--------------
An integer, the maximum number of programs you can attend.


Sample Input-1:
---------------
4
1 2,2 4,2 3,2 2

Sample Output-1:
----------------
4

Sample Input-2:
---------------
6
1 5,2 3,2 4,2 2,3 4,3 5

Sample Output-2:
----------------
5


'''
#TOPIC Segment Tree
#SOLUTION
#CPP

'''

#include<bits/stdc++.h>

using namespace std;


bool comp(pair<int,int> p1,pair<int,int> p2){
    if(p1.second<p2.second){
        return 1;
    }
    if(p2.second<p1.second){
        return 0;
    }
    
    return p1.first<=p2.first;
    
}

void update(int x,int l,int r,vector<int>& tree,int index,int val){
    
    if(l==r){
        tree[x] = val;
        return;
    }
    int mid = (l+r)/2;
    
    if(index<=mid){
        update(2*x+1,l,mid,tree,index,val);
    }
    else{
        update(2*x+2,mid+1,r,tree,index,val);
    }
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


int main(){
    
    int n;
    cin>>n;
    
    vector<pair<int,int>> temp;
    
    for(int i=0;i<n;i++){
        int u,v;
        cin>>u>>v;
        
        temp.push_back({u,v});
    }
    
    sort(temp.begin(),temp.end(),comp);
    
    vector<int> tree(4*n,0);
    int count=0;
    
    
    for(int i=0;i<n;i++){
        
        int l=temp[i].first-1;
        int r = temp[i].second-1;
        
        int ans=-1;
        
        while(l<=r){
            int mid = (l+r)/2;
            
            if(get(0,0,n-1,l,mid,tree)<mid-l+1){
                ans=mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
            
            
        }
        
        if(ans!=-1){
            update(0,0,n-1,tree,ans,1);
            count++;
            
            
        }
        
        
        
    }
    
    cout<<count<<endl;
    
    
    
}

'''