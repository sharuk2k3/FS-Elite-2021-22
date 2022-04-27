/*

Indian Super League organizing a football match at Eden Gardens.
The teams are Bangalore and Chennai are playing opposite each other.

After Match starts, each team making some goals at certain time, 
for example, goal 'goal[i]' was made by a player at time 'time[i]'.
goal[i]: indicates the team number 0 (Bangalore) or 1 (Chennai).
time[i]: indicates the time of the goal made.

Now, your task is to find out the leading team at given time t[j].

Input Format:
------------------
Line-1: Two integers N and K, no of goals-> goal[i] and no of times-> t[j]
Line-2: N space seperated integers only 0's and 1', goals[i]
Line-3: N space seperated integers, time[i]
Line-4: K space seperated integers , t[i]
 
Output Format:
------------------
Print K space seperated integers as result.


Sample Input-1:
---------------
7 5
0 1 1 0 0 1 0
0 5 10 15 20 25 30
3 12 25 15 24

Sample Output-1:
----------------
0 1 1 0 0

Explanation:
------------
At time 3, the goals are [0], and 0 is leading.
At time 12, the goals are [0,1,1], and 1 is leading.
At time 25, the goals are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent goal)
At time 15, the goals are [0,1,1,0], and 0 is leading (as ties go to the most recent goal)
At time 24, the goals are [0,1,1,0,0], and 0 is leading.


*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,k;
    cin >> n >> k;
    
    vector<int> g(n);
    vector<int> t(n);
    
    for(int i=0;i<n;i++) cin >> g[i];
    for(int i=0;i<n;i++) cin >> t[i];
    
    vector<int> q(k);
    for(int i=0;i<k;i++) cin >> q[i];
    
    vector<int> pre_banglore(n,0);
    vector<int> pre_chennai(n,0);
    
    pre_banglore[0] = g[0]==0 ? 1 : 0;
    pre_chennai[0] = g[0]==1 ? 1 : 0;
    
    for(int i=1;i<n;i++)
    {
        pre_banglore[i] = pre_banglore[i-1];
        pre_chennai[i] = pre_chennai[i-1];
        
        if(g[i]==0) pre_banglore[i]++;
        else pre_chennai[i]++;
    }
    
    for(int i=0;i<k;i++)
    {
        int now = q[i];
        
        int ind = upper_bound(t.begin(),t.end(),now)-t.begin();
        ind--;
        
        if(pre_banglore[ind] > pre_chennai[ind])
        {
            cout << 0 << endl;
        }
        
        else if(pre_banglore[ind] < pre_chennai[ind]) cout << 1 << endl;
        
        else cout << g[ind] << endl;
    }
    
}