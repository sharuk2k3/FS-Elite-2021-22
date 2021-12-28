/*
A Kid is arranging a structure using building blocks, 
by placing individual building-block adjacent to each other.

A building-block is a vertical alignment of blocks.
	                            _
here one block each represents  as |_|.

The following structure made up of using building blocks

                          _
                      _|_|    _
                     |_|_|w|_|_              _
                  _|_|_|_|_|_| w   w  w |_| 
              _|_|_|_|_|_|_|w|_|_w|_|____
    
               0  1   3   4   2   3    2   0   1   0   2

Once the structure is completed, kid pour water(w) on it.

You are given a list of integers, heights of each building-block in a row.
 Now your task How much amount of water can be stored by the structure.

 Input Format:
 -------------
 Space separated integers, heights of the blocks in the structure. 

Output Format:
 --------------
 Print an integer, 
  
Sample Input:
-------------
 0 1 3 4 2 3 2 0 1 0 2
    
Sample Output:
--------------
6
    
Explanation:
 -----------
In the above structure,  6 units of water (w represents the water in the structure)
can be stored.
*/


#include<bits/stdc++.h>
using namespace std;

int main(){
    
    int a;
    vector<int> nums;
    int n;
    cin>>n;
    
    while (1) {
        cin>>a;
        nums.push_back(a);
        if(cin.get() == '\n'){  
            break;
        }
    }
    
    //int n = nums.size();
    vector<int> prefix(n,0);
    prefix[0]=nums[0];
    for(int i=1;i<n;i++){
        prefix[i] = max(nums[i],prefix[i-1]);
    }
    
    vector<int> suffix(n,0);
    suffix[n-1]=nums[n-1];
    
    for(int i=n-2;i>=0;i--){
        suffix[i]=max(suffix[i+1],nums[i]);
    }
    
    /*for(int i=0;i<n;i++){
        cout<<nums[i]<<" ";
    }*/

    int count=0;
    for(int i=1;i<n-1;i++){
        if(min(prefix[i-1],suffix[i+1])>nums[i]){
            count+=min(prefix[i-1],suffix[i+1]);
            count-=nums[i];
        }
    }
    cout<<count;
    
    
    
    
}