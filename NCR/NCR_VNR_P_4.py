'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1

Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

def numberOfSubstrings(s):
    s,e,c = 0,0,0
    d = {'a' : 0, 'b' : 0, 'c' : 0}
    for e in range(len(s)):
        d[s[e]] += 1
        while d['a'] > 0 and d['b'] > 0 and d['c'] > 0:
            c += (len(s) - e)
            d[s[s]] -= 1
            s += 1  
    return c
s=input()
print(numberOfSubstrings(s))

'''
//CPP Sol
class Solution {
public:
	int numberOfSubstrings(string s) {
		int n = s.size(), ans = 0;
        unordered_map<int, int> m;
		int j = 0;
		for (int i = 0; i < n; ++i) {
            m[s[i] - 'a']++;
			while(m[0] && m[1] && m[2]) {
			    m[s[j++] - 'a']--;
			}
			ans += j;
		}
		return ans;
	}
};
'''