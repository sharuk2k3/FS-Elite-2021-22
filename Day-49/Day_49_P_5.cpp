/*
'''

Given N satellite stations, numbered 1 to N.
These satellites are connected to send signals from one to other.
To send a signal from satellite 's' to satellite 'd', it takes 
an amount of time 't'.

You are given a list of travel times as directed edges times[i] = (s, d, t).

Your task to find the time taken to recieve signal from a satellite station K, 
to all N-1 satellite stations. If it is impossible, return -1 .

Input Format:
-------------
Line-1 ->   Three integers, N number of satellite stations, 
            K is the satellite to send signal and T is the number of edges.
Next T lines -> Three space separated integers, 's' is the source, 
            'd' is the destination, 
			't' is the time taken recieve signal from 's' to 'd'.

Output Format:
--------------
Print an integer as your result.


Sample Input-1:
---------------
4 2 3
2 1 1
2 3 1
3 4 1

Sample Output-1:
----------------
2


Sample Input-2:
---------------
5 2 4
2 1 1
2 3 2
3 4 3
5 1 4

Sample Output-2:
----------------
-1


Sample Input-3:
---------------
5 2 4
2 1 1
2 3 2
3 4 3
1 5 6

Sample Output-3:
----------------
7


'''*/

#include<bits/stdc++.h>
using namespace std;

vector<pair<int,int>> ar[10005];


int main()
{
    int n,k,e;
    cin >> n >> k >> e;
    
    
    for(int i=0;i<e;i++)
    {
        int s,d,t;
        cin >> s >> d >> t;
        
        ar[s].push_back({d,t});
    }
    
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
    pq.push({0,k});
    int cnt=0;
    int ans=0;
    
    vector<int> vis(n+1,0);
    
    while(pq.size())
    {
        auto temp = pq.top();
        pq.pop();
        
        int node=temp.second;
        int dist=temp.first;
        
        if(vis[temp.second]) continue;
        
        vis[node]=1;
        ans = dist;
        cnt++;
        
        for(auto child : ar[node])
        {
            if(!vis[child.first])
            {
                pq.push({ans+child.second,child.first});
            }
        }
    }
    
    
    if(cnt<n) cout << -1 << endl;
    else cout << ans << endl;
}