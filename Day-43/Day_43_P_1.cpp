/*
'''

There is a row of buildings constructed by Raj Group Ltd.

The civil engineer planned to construct the buildings in ascending order 
of their heights, but there is a group of contiguous buildings not constructed 
according to the plan, remove such group of buildings from that row of buildings 
(can be empty), so the buildings in the row are in sorted order of their heights.

Your task is to find and return the number of buildings in such group.

Input Format:
-------------
Line-1: An integer N, length of array.
Line-2: N space separated integers, heights of the buildings.

Output Format:
--------------
Print an integer, the minimum of group of buildings.


Sample Input-1:
---------------
8
2 3 5 12 2 4 5 7

Sample Output-1:
----------------
3

Explanation:
------------
The minimum group of builings in a row, you can remove is [5, 12, 2] or 
[12, 2, 4]  of length 3. 
 - the remaining buildings with the heights after removal will be [2, 3, 4, 5, 7],
 OR [2, 3, 5, 5, 7], which are in ascending order.


Sample Input-2:
---------------
6
9 7 5 4 2 1

Sample Output-2:
----------------
5

Explanation:
------------
The minimum group of builings in a row, you can remove is [7, 5, 4, 2, 1] or  
[9, 7, 5, 4, 2]  of length 5. 



'''

#Solution:

*/


#include<bits/stdc++.h>
using namespace std;

int check(int mid,int n,vector<int>& temp,vector<int>& prefix,vector<int>& suffix){
    if(mid==n){
        return 1;
    }
    for(int i=0;i+mid<=n;i++){
        int ans=1;
        if(i!=0 && i+mid<n){
            if(temp[i-1]>temp[i+mid]){
                ans=0;
            }
        }
        if(i!=0){
            ans=(ans&prefix[i-1]);
        }
        if(i+mid<n){
            ans=(ans&suffix[i+mid]);
        }
        
        
        
        if(ans){
            return 1;
        }
    }
    return 0;
    
}

int main(){
    
    int n;
    cin>>n;
    vector<int> temp(n);
    for(int i=0;i<n;i++){
        cin>>temp[i];
    }
    
    vector<int> prefix(n+2,0),suffix(n+2,0);
    prefix[0]=1;
    for(int i=1;i<n;i++){
        if(prefix[i-1] && temp[i]>=temp[i-1]){
            prefix[i]=1;
        }
    }
    suffix[n-1]=1;
    for(int i=n-2;i>=0;i--){
        if(suffix[i+1] && temp[i]<=temp[i+1]){
            suffix[i]=1;
        }
    }
    
    
    int l=0;
    int r=n;
    int ans=r;
    while(l<=r){
        
        int mid = (l+r)/2;
        if(check(mid,n,temp,prefix,suffix)){
            ans=mid;
            r=mid-1;
        }
        else{
            l=mid+1;
        }
        
        
    }
    cout<<ans<<endl;
}