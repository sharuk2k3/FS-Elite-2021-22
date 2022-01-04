''''

A magic box with p rows and r columns is initially filled with silver.
If we invoke a method addMagicOperation which turns the silver at 
index(row, col) into gold. Given N set of indices to work up on, 
find the number of gold-blocks which are formed after each addMagicOperation. 

A gold-block is a block of gold cells connected horizontally and vertically 
and surrounded by silver. Consider all four edges of the magic box are 
surrounded by silver.

Input Format:
--------------
Line-1: Three space separated integers p, r , and n (number of add Magic Operations)
Next N lines: Two space separated integers, cell to perform addMagicOperation 

Output Format:
--------------
Print a list of numbers, number of gold-blocks formed after each addMagicOperation


Sample Input-1:
-----------------
3 3 5
0 0
0 1
1 2
2 1
1 1

Sample Output-1:
-----------------
[1, 1, 2, 3, 1]

Explanation:

Initially, the magic box is filled with silver. (Assume 0 represents silver and 1 represents gold).

0 0 0
0 0 0
0 0 0

Operation #1: addMagicOperation(0, 0) turns the silver at cell[0][0] into gold.

1 0 0
0 0 0   Number of Gold-blocks = 1
0 0 0

Operation #2: addMagicOperation(0, 1) turns the silver at cell[0][1] into gold.

1 1 0
0 0 0   Number of Gold-blocks = 1
0 0 0

Operation #3: addMagicOperation(1, 2) turns the silver at cell[1][2] into gold.

1 1 0
0 0 1   Number of Gold-blocks = 2
0 0 0

Operation #4: addMagicOperation(2, 1) turns the silver at cell[2][1] into gold.

1 1 0
0 0 1   Number of Gold-blocks = 3
0 1 0

Operation #5: addMagicOperation(1, 1) turns the silver at cell[1][1] into gold.

1 1 0
0 0 1   Number of Gold-blocks = 1
0 1 0


'''


#SOLUTION


#CPP

'''
#include<bits/stdc++.h>

using namespace std;

int getPar(int cur,int dsu[]){
    if(dsu[cur]==cur) return cur;
    return dsu[cur] = getPar(dsu[cur],dsu);
}

void merge(int dsu[],int c1,int c2,int &ans){
    int p1 = getPar(c1,dsu);
    int p2 = getPar(c2,dsu);
    if(p1!=p2){
        dsu[p2] = p1;
        ans--;
    }
}

int main(){
    int n,m,q;
    cin>>n>>m>>q;
    int dsu[n*m],gold[n*m],ans = 0;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<m;j++){
            int cell = i*n + j;
            dsu[cell] = cell;
            gold[cell] = 0;
        }
    }
    int dx[] = {0,0,-1,1}, dy[] = {-1,1,0,0};
    while(q--){
        int i,j;
        cin>>i>>j;
        int cur = i*n + j;
        ans++;
        gold[cur] = 1;
        for(int k = 0;k<4;k++){
            int ni = dx[k]+i, nj = dy[k] + j;
            if(ni<0 || nj<0 || ni>=n || nj>=m || gold[ni*n+nj]==0) continue;
            int cellnum = n*ni + nj;
            merge(dsu,cur,cellnum,ans);
        }
        cout<<ans<<" ";
    }
    return 0;
}

'''