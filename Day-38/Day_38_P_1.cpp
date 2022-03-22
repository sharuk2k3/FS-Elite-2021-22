/*
'''

Given a set of weights of n items weights[], and another item wieght w.
Your task is to check if the sum of weights of continuous subset is equal to 
one of the multiple of w, where subset size should be minimum 2.

For example: Mulitple of w means, w=3 then multiple of w are
3, 6, 9, 12, .... so on.

Print true, if such subset sum is possible.
Otherwise, print false.

Input Format:
-------------
Line-1 : Two integers n and w, number of weights and weight to match.
Line-2 : n space separated integers, weights of n items.

Output Format:
--------------
Print a boolean value.


Sample Input-1:
---------------
5 4
1 2 3 5 6

Sample Output-1:
----------------
true


Sample Input-2:
---------------
5 4
1 2 3 6 5

Sample Output-2:
----------------
true

Explanation: 
------------
sum of  continuous subset of weights [1,2,3,6]  equals to 12, multiple of 4.

'''
*/

//Solution:

#include<bits/stdc++.h>
using namespace std;

#define FOR(n) for(int i=0; i<n; i++)
#define MP make_pair
#define PB push_back
typedef long long ll;
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
	
	int n, w, s=0, f=0; cin >> n >> w;
	vi v(n), mod(w, -1);
	FOR(n) {
		cin >> v[i];
	}
	
	s += v[0];
	for(int i=1; i<n; i++) {
		s+=v[i];
		if(mod[s%w] == 1 || s%w == 0) {
			f = 1;
			break;
		} else {
			mod[s%w] = 1;
		}
	}
	if(f) {
		cout << "true";
	} else {
		cout << "false";
	}
	
	return 0;
}