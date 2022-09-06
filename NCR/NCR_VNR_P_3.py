'''
Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing. 
Input: arr[] = {1, 4, 3}
Output: 1
There is only one subarray {1, 4}

Input: arr[] = {1, 2, 3, 4}
Output: 6
There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
                      {2, 3}, {2, 3, 4} and {3, 4}

Input: arr[] = {1, 2, 2, 4}
Output: 2
There are 2 subarrays {1, 2} and {2, 4}
'''
def countIncreasing(arr, n):
    cnt = 0 
    length = 1
    for i in range(0, n - 1):
        if arr[i + 1] > arr[i]:
            length += 1
        else:
            cnt += (((length - 1) * length) // 2)
            length = 1
    if length > 1:
        cnt += (((length - 1) * length) // 2)
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
print(countIncreasing(arr, n))
'''
//CPP SOL
#include<bits/stdc++.h>
using namespace std;
int countIncreasing(int arr[], int n)
{
    int cnt = 0;
    int len = 1;
    for (int i=0; i < n-1; ++i)
    {
        if (arr[i + 1] > arr[i])
            len++;   
        else
        {
            cnt += (((len - 1) * len) / 2);
            len = 1;
        }
    }
    if (len > 1)
        cnt += (((len - 1) * len) / 2);
    return cnt;
}
int main()
{
  int arr[] = {1, 2, 2, 4};
  int n = sizeof(arr)/sizeof(arr[0]);
  cout<< countIncreasing(arr, n);
  return 0;
}
'''