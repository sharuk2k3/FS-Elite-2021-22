'''

Given a sorted list of integers E[], and two integers  L and U
Where L <= E[i]  <= U.

Your task is to find the ranges, which are not present in the given list
and print all the ranges

For example:
Given list is [ 1, 2, 4, 51, 52, 53, 92, 93, 94, 95 ] and L=1 U=100: 
The ranges which are not present are [3, 5->50, 54->91, 96->100]

Note: List E contain no duplicates.

Input Format:
-------------
Line-1 -> Space separated integers in sorted order

Output Format:
--------------
Print the list of ranges.


Sample Input-1:
---------------
0 1 2 3 4 5 8 9 10
0 20

Sample Output-1:
----------------
[6->7, 11->20]


Sample Input-2:
---------------
1 2 4 51 52 53 92 93 94 95
1 100

Sample Output-2:
----------------
[3, 5->50, 54->91, 96->100]
 



'''

#Solution:


def MissingRanges(nums, lower, upper):
    ans,pre = [], lower-1
    for cur in nums+[upper+1]:
        if cur - pre == 2:
            ans.append(str(pre + 1))
        elif cur - pre > 2:
            ans.append(str(pre + 1) + "->" + str(cur - 1))
        pre = cur
    return(ans)
nums=list(map(int,input().split()))
lower,upper=map(int,input().split())
print(MissingRanges(nums, lower, upper))

'''
#CPP Solution:

#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s,k;
         getline(cin,s);
         
         int low,high;
        cin>>low>>high;
        
        stringstream ss(s);
        
        while(ss>>k){
            int n = stoi(k);
            if(low==n){
                low++;
                continue;
            }
            int diff = n-low;
            if(diff==1)
                cout<<low<<endl;
            else
                cout<<low<<"->"<<n-1<<endl;
            low = n+1;
        }
        int diff = high-low;
        if(diff==1){
            cout<<low<<endl;
        }
        else if(diff>1){
            cout<<low<<"->"<<high<<endl;
        }
        return 0;
    }
'''