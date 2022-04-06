/*'''

Charlie Brown is working with strings,
He is a given a string S. He wants to find out the maximum substring 'MaxSub'.

MaxSub is a substring which appears atleast twice in S with Maximum length. 

Your task is to help Charlie Brown to find the Maximum Substring MaxSub,
and print the length of MaxSub. If there is MaxSub, return 0.

Input Format:
-------------
A string S.

Output Format:
--------------
Print an integer, length of MaxSub


Sample Input-1:
---------------
babababba

Sample Output-1:
----------------
5

Explanation: 
------------
The Maximum substring is 'babab' , which occurs 2 times.


Sample Input-2:
---------------
abbbbba

Sample Output-2:
----------------
4

Explanation: 
------------
The Maximum substring is 'bbbb' , which occurs 2 times.


Sample Input-3:
---------------
vignesh

Sample Output-3:
----------------
0



'''
*/
#include<bits/stdc++.h>
using namespace std;

#define FOR(n) for(int i=0; i<n; i++)
#define MP make_pair
#define PB push_back
typedef long long int ll;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef map<int, int> mi;
typedef pair<int, int> pi;

template<typename T>
void print(T v) {
	for(int i=0; i<v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

template<typename T1, typename T2>
void print2(T1 v, T2 n, T2 m) {
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cout << v[i][j] << " ";
		}
		cout << endl;
	}
}

int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0);
	
	string s; cin >> s;
	int n = s.size();
	unordered_map<string, int> m;
	
	FOR(n) {
		string temp;
		for(int j=i; j<n; j++) {
			temp += s[j];
			m[temp]++;
		}
	}
	
	int ans = 0;
	for(auto it: m) {
	    int sz = it.first.length();
		if(it.second >= 2) {
			ans = max(ans, sz);
		}
	}
	
	cout << ans;
	
	return 0;
}