'''

Given a sorted list of integers, 

Your task is to find the continuous range of numbers, make them as groups
and print all the groups as show in the sample testcases.

For example:
Given list is [ 1, 2, 3 ]: 1, 2, 3 is continuous range, grouped as 1->3
Given list is [ 1, 2, 4, 5, 7 ]: 1, 2 is continuous range, grouped as 1->2, 
4,5 grouped as 4->5, 7 is left alone.

Note: List contain no duplicates.

Input Format:
-------------
Line-1 -> Space separated integers in sorted order

Output Format:
--------------
Print the list of continuous range groups.


Sample Input-1:
---------------
1 2 4 5 7

Sample Output-1:
----------------
[1->2, 4->5, 7]

Explanation: 
------------
1,2 form a continuous range; 4,5 form a continuous range.


Sample Input-2:
---------------
1 2 3 5 6 7 9 10 12

Sample Output-2:
----------------
[1->3, 5->7, 9->10, 12]

Explanation: 
------------
1,2,3 form a continuous range 
5,6,7 form a continuous range
9,10 form a continuous range


'''

#Solution:

def Ranges(nums):
    list = []
    start = None
    for i in range(0, len(nums)):
        if start is None:
            start = nums[i]
        if i == len(nums)-1 or not nums[i+1] - nums[i] == 1 :
            list.append(str(start) + "->" + str(nums[i]) if start != nums[i] else str(nums[i]))
            start = None
    return list
nums=list(map(int,input().split()))
print(Ranges(nums))


'''

#include<bits/stdc++.h>
    using namespace std;
    
    int main()
    {
        string s,k;
        getline(cin,s);
        stringstream ss(s);
        vector<int> v;
        while(ss>>k)
            v.push_back(stoi(k));
        int n = v.size();    
        
        for(int i=0;i<n-1;i++){
            int temp = i;
            while(i<n-1 and v[i]-v[i+1]==-1)
                i++;
            if(temp==i)
                cout<<v[i]<<endl;
            else
                cout<<v[temp]<<"->"<<v[i]<<endl;
        }
        if(v[n-1]-v[n-2]!=1)
           cout<<v[n-1]<<endl;
            
        return 0;
    }

'''