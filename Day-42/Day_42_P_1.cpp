/*'''

Manoj is working on sets and relations.
He is given a set S consist of N integers from 1 to N, without dupliactes.
The set S may contain any shuffled order of 1 to N numbers.
And also P number of subsets also given where each subset of size Q.
Each subset is a subsequence of shuffled set S.

Manoj has to check, using the given subsets can he form the set S uniquely 
or not. i.e., the order of numbers in the subsets remains unchanged and 
can form only one unique super set using the subsets, and 
the unique super set should be S.

Your task is to help Manoj to check whether it is possible to form 
the shuffled set S uniquely from the given subsets.

For example: 
-----------
If given shuffled set is [2,4,6] and subsets are [2,4] [2,6].
You can form the following sets, [2,4,6] or [2,6,4].

So, you should return false, as the given subsets form more than 1 set.

Simply, there should be always only one unique super set can be formed.
and that set should be equal to S.


Input Format:
-------------
Line-1: An integer N, size of the shuffled array.
Line-2: N space separated integers, shuffled set S.
Line-3: Two space separated integers P and Q, number of subsets, size of subsets
Next P lines: Q space separated integers, non repeated integers from [1-N]

Output Format:
--------------
Print a boolean value, can you form the shuffled set S uniquely or not.


Sample Input-1:
---------------
4
1 3 2 4
3 2
1 2
3 2
3 4

Sample Output-1:
----------------
false

Explanation: 
------------
The subsets are [1,2], [3,2] and [3,4] cannot
form the given shuffled set [1,3,2,4].
It can form another set as [1,3,4,2] also.


Sample Input-2:
---------------
4
1 3 2 4
4 2
1 2
3 2
1 3
2 4

Sample Output-2:
----------------
true

Explanation: 
------------
The subsets are [1,2], [3,2], [1,3] and [2,4] can uniquely 
form the given shuffled set [1,3,2,4].


Sample Input-3:
---------------
5
1 3 5 4 2
3 3
3 4 2
5 4 2
1 3 5

Sample Output-3:
----------------
true

Explanation: 
------------
The subsets are [3,4,2], [5,4,2], and [1,3,5] can uniquely 
form the given shuffled set [1,3,5,4,2].




'''

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    p, q = map(int, input().split())
    subsets = []
    for _ in range(p):
        subsets.append(list(map(int, input().split())))
    if check_unique(arr, subsets):
        print(True)
    else:
        print(False)
def check_unique(arr, subsets):
    for subset in subsets:
        if not check_subset(arr, subset):
            return False
    return True
def check_subset(arr, subset):
    for i in range(len(subset)):
        if subset[i] not in arr:
            return False
        arr.remove(subset[i])
    return True

main()

*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int n;
    cin>>n;
    
    vector<int> temp(n);
    
    for(int i=0;i<n;i++){
        cin>>temp[i];
    }
    
    int p,q;
    cin>>p>>q;
    
    vector<vector<int>> adj(n+2);
    vector<int> indegree(n+2,0);
    
    for(int i=0;i<p;i++){
        int root;
        cin>>root;
        for(int j=1;j<q;j++){
            int x;
            cin>>x;
            adj[root].push_back(x);
            indegree[x]++;
            root=x;
        }
    }
    
    int flag=1;
    queue<int> qq;
    for(int i=1;i<=n;i++){
        if(indegree[i]==0){
            qq.push(i);
        }
    }
    
    vector<int> tt;
    while(!qq.empty()){
        
        int size = qq.size();
        if(size>=2){
            flag=0;
            break;
        }
        
        for(int i=0;i<size;i++){
            int val = qq.front();
            qq.pop();
            tt.push_back(val);
            for(auto xx: adj[val]){
                indegree[xx]--;
                if(indegree[xx]==0){
                    qq.push(xx);
                }
            }
            
        
        }
        
        
    }
    if(flag){
        int f2=1;
        for(int i=0;i<tt.size();i++){
            if(tt[i]!=temp[i]){
                f2=0;
                break;
            }
        }
        if(f2){
            cout<<"true"<<endl;
        }
        else{
            cout<<"false"<<endl;
        }
    }
    else{
        cout<<"false"<<endl;
    }
    
    
    
}