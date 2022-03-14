'''

In Dubai's Burj Khalifa, there is an elevator moves only in upwards direction, 
the elevator can carry N members.

The people are waiting for the elevator at different floors, made P requests, 
request[i] = [ num_people, enter_floor, exit_floor ], each request indicates, 
number of people to enter into elevator, entering floor number, 
exiting floor number.

Initially the elevator is empty.

Your task is to find and return true, iff it is possible to enter the people
into elevator and exit from elevator of all the requests made by the people.


Input Format:
-------------
Line-1 -> Two integers P and N, number of requests and number of members 
          can be carried by elevator.
Next N Lines -> three space separated integers, num_people, enter_floor, exit_floor.

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
2 5
2 1 5
3 3 7

Sample Output-1:
----------------
true



Sample Input-2:
---------------
2 4
2 1 5
3 3 7

Sample Output-2:
----------------
false



Sample Input-3:
---------------
3 11
3 2 7
3 7 9
8 3 9

Sample Output-3:
----------------
true


'''

#CPP SOLUTION:

'''

#include<bits/stdc++.h>
using namespace std;

bool comp(pair<int,pair<int,int>> p1,pair<int,pair<int,int>> p2){
    
    if(p1.first<p2.first){
        return 1;
    }
    if(p2.first<p1.first){
        return 0;
    }
    
    return (p1.second.first<=p2.second.first);
    
}

int main(){
    
    int p,n;
    cin>>p>>n;
    
    vector<pair<int,pair<int,int>>> temp;
    
    for(int i=0;i<p;i++){
        int c,u,v;
        cin>>c>>u>>v;
        
        temp.push_back({u,{1,c}});
        temp.push_back({v,{-1,c}});
        
        
    }
    
    sort(temp.begin(),temp.end(),comp);
    int flag=1;
    int curr=0;
    
    
    
    for(int i=0;i<2*p;i++){
        curr+=(temp[i].second.first*temp[i].second.second);
        if(curr>n){
            flag=0;
            break;
        }
    }
    if(flag){
        cout<<"true"<<endl;
    }
    else{
        cout<<"false"<<endl;
    }
}

'''