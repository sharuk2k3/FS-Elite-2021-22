'''
There are N sticks of various lengths, stklen[], where stklen[i] is the lenth of the i-th stick.
And you need to break them into pieces of any length.
And you will be given another integer P, number of pieces you need to make.
You need to break the sticks to make P pieces of equal lengths.
You can consider the unwanted piece as scrap.

You can break a stick of length 6 as follows:
	- 6 pieces of length-1.
	- 1 piece of length-1 and 1 piece of length-2 and one piece of length-3.
	- 3 pieces of length-2, etc.
	
Your task is to check, can you break the sticks into P pieces of equal length,
if possible, retrun the maximum length of the pieces possible.
otherwise return 0.

Input Format:
-------------
Line-1: Two space separated integers, N and P.
Line-2: N space separated integers, length of the sticks.

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
3 3
6 8 10

Sample Output-1:
----------------
6

Explanation:
------------
- Keep the stick-1 as it is.
- Break the stick-2 into two pieces, one of length 6 and one of length 2.
- Break the stick-3 into two pieces, one of length 6 and one of length 4.
Finally, you have 3 pieces of length 6.


Sample Input-2:
---------------
3 4
6 8 10

Sample Output-2:
----------------
5

Explanation:
------------
- Break the stick-1 into two pieces, one of length 5 and one of length 1.
- Break the stick-2 into two pieces, one of length 5 and one of length 3.
- Break the stick-3 into two pieces, one of length 5 and one of length 5.
Finally, you have 3 pieces of length 4.


Sample Input-3:
---------------
3 25
6 8 10

Sample Output-3:
----------------
0

case =1
input =25 34
4958 7120 475 2996 5282 3087 8538 1029 6477 9063 9597 6021 3560 6862 2583 8224 4784 7798 1394 5411 788 6464 3563 1952 583
output =2641

case =2
input =25 43
9086 7336 5001 8717 2040 3791 6612 4308 1161 7751 7274 6490 8687 1630 2245 7982 4761 5683 8677 58 7346 7213 6369 7042 613
output =2445

case =3
input =45 67
957 552 256 148 10 264 604 732 128 291 747 924 580 869 867 796 638 591 759 859 200 213 107 981 174 606 50 959 895 975 484 531 184 588 101 417 368 448 311 969 280 100 448 618 421
output =264

case =4
input =45 99
957 552 256 148 10 264 604 732 128 291 747 924 580 869 867 796 638 591 759 859 200 213 107 981 174 606 50 959 895 975 484 531 184 588 101 417 368 448 311 969 280 100 448 618 421
output =193

case =5
input =50 877
72125 83155 97202 86502 29039 36988 26543 7886 12209 91361 18790 98013 95556 35842 3465 19882 56887 83163 92201 42617 40865 59019 3545 43407 68639 59635 81095 75854 13955 32867 67400 14847 3359 41985 88213 10532 22342 66261 98870 46214 50934 43994 78562 38576 30346 11931 86370 8844 90720 19772
output =2760

case =6
input =50 8767
72125 83155 97202 86502 29039 36988 26543 7886 12209 91361 18790 98013 95556 35842 3465 19882 56887 83163 92201 42617 40865 59019 3545 43407 68639 59635 81095 75854 13955 32867 67400 14847 3359 41985 88213 10532 22342 66261 98870 46214 50934 43994 78562 38576 30346 11931 86370 8844 90720 19772
output =283

case =7
input =100 7643
10443 92744 84541 49276 96684 78862 34609 99341 32036 43831 48502 58883 51975 70622 26833 87776 10153 15145 24422 82662 10629 11683 40255 20943 62128 9518 72654 19059 13335 56856 41880 54876 25984 99806 22007 24274 31584 10661 16015 26012 62918 98440 65675 53451 50471 24032 80448 39908 89484 52779 9245 65911 34753 28319 73767 16086 27812 34169 27857 24982 28228 95589 40655 50682 92953 2592 94376 25946 23651 16617 19701 60246 21169 12268 60219 88171 26701 89930 54048 48902 58283 70557 50649 14074 41334 3267 14181 27620 831 29525 77369 58573 11744 52959 76376 69179 99245 23159 20170 66387
output =591

case =8
input =100 3644
10443 92744 84541 49276 96684 78862 34609 99341 32036 43831 48502 58883 51975 70622 26833 87776 10153 15145 24422 82662 10629 11683 40255 20943 62128 9518 72654 19059 13335 56856 41880 54876 25984 99806 22007 24274 31584 10661 16015 26012 62918 98440 65675 53451 50471 24032 80448 39908 89484 52779 9245 65911 34753 28319 73767 16086 27812 34169 27857 24982 28228 95589 40655 50682 92953 2592 94376 25946 23651 16617 19701 60246 21169 12268 60219 88171 26701 89930 54048 48902 58283 70557 50649 14074 41334 3267 14181 27620 831 29525 77369 58573 11744 52959 76376 69179 99245 23159 20170 66387
output =1231

'''


'''

#Solution

def Sticks(n,p,arr):
    l = 1
    arr=sorted(arr)
    h = max(arr)
    m = 0
    c = 0
    while True:
        if l>h:
            return 0
        if c==p:
            return m
        c=0
        m=(l+h)//2
        for i in arr:
            c+=i//m
        if c>p: 
            l=m+1
        if c<p:
            h=m-1
n, p = map(int, input().split())
l = list(map(int, input().split()))
print(Sticks(n,p,l))

'''


'''

#CPP 


#include<bits/stdc++.h>
using namespace std;

int check(int mid,vector<int>& temp,int n,int p){
    
    
    int count=0;
    for(int i=0;i<n;i++){
        count+=(temp[i]/mid);
    }
    
    return count>=p;
    
}

int main(){
    
    int n,p;
    cin>>n>>p;
    
    vector<int> temp(n);
    int mini = -1;
    for(int i=0;i<n;i++){
        cin>>temp[i];
        mini = max(mini,temp[i]);
    }
    
    int l=1;
    int r = mini;
    int ans=1;
    
    while(l<=r){
        
        int mid = (l+r)/2;
        
        if(check(mid,temp,n,p)){
            ans=mid;
            l=mid+1;
        }
        else{
            r=mid-1;
        }
        
    }
    cout<<ans<<endl;
    
    
}
'''