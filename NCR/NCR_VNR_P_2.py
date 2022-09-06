'''
Effective Teams
'''

def getEfficiency(skill):
    skill.sort(reverse=False)
    n=len(skill)
    s=skill[0]+skill[n-1]
    ans=0
    for i in range(n//2):
        if skill[i]+skill[n-i-1]!=s:
            ans=-1
            break
        else:
            ans+=skill[i]*skill[n-i-1]
    return ans
skill=[1,5,6,2]
print(getEfficiency(skill))
'''
#CPP
long getEfficiency(vector<int> skill){
    sort(skill.begin(),skill.end());
        int n=skill.size(),sum=skill[0]+skill[n-1];
        long ans=0;
        for(int i=0;i<n/2;i++){
            if((skill[i]+skill[n-i-1])!=sum){
                ans=-1;
                break;
            }
            else 
            ans+=skill[i]*skill[n-i-1];
        }
        return ans;
}
//With Driver Code Sol
#include <bits/stdc++.h>
using namespace std;
long getEfficiency(vector<int> skill){
    sort(skill.begin(),skill.end());
        int n=skill.size(),sum=skill[0]+skill[n-1];
        long ans=0;
        for(int i=0;i<n/2;i++){
            if((skill[i]+skill[n-i-1])!=sum){
                ans=-1;
                break;
            }
            else 
            ans+=skill[i]*skill[n-i-1];
        }
        return ans;
}
int main()
{	int n;
 	cin>>n;
	vector<int> skill(n);
  	for(int i=0;i<n;i++)
    {
            cin>>skill[i];
    }
	cout <<getEfficiency(skill) ;
	return 0;
}

'''
