'''

There are N players, played a game.
You are given the scores of the N players as scores[] array,
where i-th player score is score[i].
You are given P chances to modify the score of the players.

In each chance you can modify the score of i-th player as follows:
	- You are allowed increment the score of i-th player by 1.
You have to perform these increments, in order to maximize the occurences of any score.

Your task is to maximize occurences of a score, after utlizing atmost P chances.

Input Format:
-------------
Line-1: Two space separated integers N and P, Players count, and number of chances.
Line-2: N space separated integers, scores of N players scores[].

Output Format:
--------------
Print an integer, maximum occurences of a score!


Sample Input-1:
---------------
5 3
2 3 5 6 9

Sample Output-1:
----------------
2


Sample Input-2
---------------
6 5
2 3 4 6 8 9


/*
Explination

1                                   
3 3 4 6 8 9
2
4 3 4 6 8 9
3
4 4 4 6 8 9
4 
4 4 4 7 8 9
5
4 4 4 8 8 9
*/
Sample Output-2:
----------------
3



'''



#SOLUTION

#CPP


'''
#include<bits/stdc++.h>
using namespace std;

int n,p;

int check(int mid,int i,vector<int>& temp,vector<int>& prefix){
    
    if(mid==0){
        if((temp[i]*(i-mid))-prefix[i-1]<=p){
            return 1;
        }
        return 0;
    }
    
    if((temp[i]*(i-mid))-(prefix[i-1]-prefix[mid-1])<=p){
        return 1;
    }
    return 0;
    
}

int main(){
    
    
    cin>>n>>p;
    
    vector<int> temp(n);
    for(int i=0;i<n;i++){
        cin>>temp[i];
    }
    
    sort(temp.begin(),temp.end());
    
    vector<int> prefix(n,0);
    prefix[0]=temp[0];
    for(int i=1;i<n;i++){
        prefix[i]=prefix[i-1]+temp[i];
    }
    
    int fans=1;
    for(int i=1;i<n;i++){
        
        int l=0;
        int r=i-1;
        int ans=-1;
        
        while(l<=r){
            int mid = (l+r)/2;
            
            if(check(mid,i,temp,prefix)){
                ans=mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
            
        }
        if(ans!=-1){
            fans=max(fans,i-ans+1);
        }
        
        
    }
    cout<<fans<<endl;
    
    
}
'''


n,k=map(int,input().split())
nums=list(map(int,input().split()))[:k]
len_nums = len(nums)
nums.sort()
max_freq = 1
freq = 1
left = 0
ops = k
for right in range(1, len_nums):
    ops -= (nums[right] - nums[right - 1]) * freq
    freq += 1
    if ops >= 0:
        max_freq = max(max_freq, freq)
    else:
        while ops < 0:
            ops += nums[right] - nums[left]
            left += 1
            freq -= 1
print(max_freq)
