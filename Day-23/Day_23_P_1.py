'''

Sreedhar is a farmer, and he started harvesting the watermelon crop, 
the crop grown very well. There are several watermelons in the crop. 
Sreedhar started picking up the watermelons one by one.
After each pick, he keeps the watermelon in a truck placed inside the crop.

The crop is in the from of 2D grid of size m*n.
You will be given the positions of the truck, Sreedhar's, and the watermelons.  
Positions are represented by the cells in the 2D grid. 

Your task is to find the minimum distance for Sreedhar to collect 
all the watermelons and put them inside the truck one by one. 

Sreedhar can only take at most one watermelon at one time 
and can move in four directions - up, down, left and right, to the adjacent cell. 
The distance is represented by the number of moves.

Input Format:
-------------
Line-1: Two space separated integers m and n, size of crop. 
Line-2: Two space separated integers, position of the truck. 
Line-3: Two space separated integers, position of Sreedhar.
Line-4: An integer W, number of watermelons in the crop.
Next W lines: Two space separated integers, positions of watermelon. 

Output Format:
--------------
An integer, minimum distance covered by Sreedhar to pickup all the watermelons


Sample Input-1:
---------------
5 7		//size of the crop as 2D grid.
2 2		//Truck Position
4 4		//Sreedhar Position
2		//Number of watermelons
3 0		//Watermelon positions
2 5

Sample Output-1:
----------------
12


'''

#SOLUTION


'''
#include<bits/stdc++.h>

using namespace std;

int main(){
    
    
    int n,m;
    cin>>n>>m;
    
    int x,y;
    cin>>x>>y;
    
    
    
    int w,z;
    cin>>w>>z;
    
    int t;
    cin>>t;
    
    vector<pair<int,int>> temp;
    int ans=abs(x-w)+abs(y-z);
    for(int i=0;i<t;i++){
        int u,v;
        cin>>u>>v;
        
        temp.push_back({u,v});
        ans+=(2*abs(x-u));
        ans+=(2*abs(y-v));
        
    }
    int fans=ans;
    for(int i=0;i<t;i++){
        
        int tt = ans;
        tt-=(abs(x-w)+abs(y-z));
        tt-=(abs(temp[i].first-x)+abs(temp[i].second-y));
        
        tt+=(abs(temp[i].first-w)+abs(temp[i].second-z));
        fans=min(fans,tt);
        
        
    }
    cout<<fans<<endl;
    
    
    
}

'''