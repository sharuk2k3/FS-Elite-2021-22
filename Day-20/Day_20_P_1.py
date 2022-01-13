#CONCEPT DAY 20 - FENWICK TREE/Binary Indexed Tree (FT>>Segment Tree)
'''

Mallika taught a new fun time program practice for Engineering Students.
As a part of this she has given set of numbers, and asked the students 
to find the sum of numbers between indices S1 and S2 (S1<=S2),
both S1 and S2 inclusive.

There are P Students in the class, numbered from 1 to P. Each student is
given set of indices and that student has to find the sum of the numbers 
between the indices and print the result.

And return the answer in the same order of

Input Format:
-------------
Line-1: Two integers N and P, N is length of set of numbers.
		where 1<= N <= 1000
Line-2: N space separated integers, array set[]
Next P lines: Two integers S1 and S2, index positions 
		where 0 <= S1 <= S2 < N
		and 1<= set[i] <= 100000

Output Format:
--------------
Print the sum of numbers between indices(s1, s2) given to each student.


Sample Input-1:
---------------
8 2
115053 59099 681359 526248 123844 612168 920784 591204
2 6
1 5

Sample Output-1:
----------------
2864403
2002718



''' 
#CPP SOLUTION


'''
#include<bits/stdc++.h>
using namespace std;

#define FOR(n) for(int i=0; i<n; i++)
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef vector<int> vi;
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

int sum(vi &fenvickTree, int i, int j) {
	
	int ind, s1 = 0, s2 = 0;
	ind = i;
	
	while(ind > 0) {
		
		s1 += fenvickTree[ind];
		ind -= ind&(-ind);
		
	}
	
	ind = j+1;
	
	while(ind > 0) {
		
		s2 += fenvickTree[ind];
		ind -= ind&(-ind);
		
	}
	
	return s2-s1;
	
}

void createTree(vi &fenvickTree, vi &v, int n) {
	
	int i, j, val;
	for(i=0; i<n; i++) {
		
		val = v[i];
		j = i+1;
		while(j<n+1) {
			fenvickTree[j] += val;
			j += j&(-j);
		}
		
	}
	
}

int main()
{
    ios::sync_with_stdio(0);
	cin.tie(0);

	int n, p; cin >> n >> p;
	vi v(n), fenvickTree(n+1, 0);
	
	FOR(n) {
		cin >> v[i];
	}

	createTree(fenvickTree, v, n);
	
	int i, j;
	while(p--) {
		cin >> i >> j;
		cout << sum(fenvickTree, i, j) << endl;
	}

//	print(fenvickTree);
	
    return 0;
}
'''