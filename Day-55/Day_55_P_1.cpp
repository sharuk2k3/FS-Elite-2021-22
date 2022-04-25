/*'''


Given a list of integers points[], the points earned or lost by N persons.

A point[a], is said to be better than a point[b],
if mod(point[a] - med) > mod(point[b] - med), where med is the median of points.
If mod(point[a] - med) == mod(point[b] - med), then point[a] is said to be 
better than point[b], if point[a] > point[b].

Median is the middle value in an ordered integer list. More formally,
if the length of the list is N, the median is the element in position 
((N - 1) / 2) in the sorted list (0-indexed).

For Example,
points[]= [7, -3, 9, 8, 1], N = 5 and the median is med = ((5 - 1) / 2) = 2. 
The element at median is points[med]= 7, as sorted list is [-3, 1, 7, 8, 9]

Your task is to return P number of better values from the points[] list.
Return the answer in sorted order.

Input Format:
-------------
Line-1: Two space seperated integers, N and P
Line-2: N space separated integers points[].

Output Format:
--------------
Print the list of integers in sorted order.


Sample Input-1:
---------------
5 2
2 3 4 5 6

Sample Output-1:
----------------
2 6

Explanation:
------------
The better 2 elements are [2, 6].
Please note that although mod(6 - 4) == mod(2 - 4) but 6 is better than 2
because 6 > 2.


Sample Input-2:
---------------
6 4
3 4 9 4 3 5

Sample Output-2:
----------------
3 3 5 9



'''*/

#include<bits/stdc++.h>
using namespace std;
int med;
bool comp(int a,int b){
    
    if(abs(a-med)>abs(b-med)){
        return 1;
    }
    if(abs(a-med)<abs(b-med)){
        return 0;
    }
    return a>=b;
    
}

int main(){
    
    int n,p;
    cin>>n>>p;
    
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
    
    sort(v.begin(),v.end());
    med=v[(n-1)/2];
    sort(v.begin(),v.end(),comp);
    vector<int> ans;
    for(int i=0;i<p;i++){
        ans.push_back(v[i]);
    }
    sort(ans.begin(),ans.end());
    for(int i=0;i<p;i++){
        cout<<ans[i]<<" ";
    }
    cout<<endl;
    
}