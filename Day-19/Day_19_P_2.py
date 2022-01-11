'''

"Emphatic Pronunciation" of a given word is where we take the word and
replicate some of the letter to emphasize their impact.

Instead of saying 'oh my god', someone may say "ohhh myyy goddd", 
We define emphatic pronunciation of a word, which is derived by replicating 
a group (or single) of letters in the original word. 

So that the replicated group is atleast 3 characters or more and 
greater than or equal to size of original group. 
For example Good -> Goood is an emphatic pronunciation,
but Goodd is not because in Goodd the 'd' are only occuring twice consecutively.
 
In the question you are given the "Emphatic pronunciation" word, 
you have to findout how many words can legal result in the 
"emphatic pronunciation" word.

Input Format:
-------------
Line-1 -> A String contains a single word, Emphatic Pronunciation word
Line-2 -> Space seperated word/s

Output Format:
--------------
Print an integer as your result


Sample Input-1:
---------------
Goood
Good

Sample Output-1:
----------------
1


Sample Input-2:
---------------
heeelllooo
hello hi helo

Sample Output-2:
----------------
2


'''


#SOLUTION

def find(S, words):
        def find2(st):
            if not st:
                return [], []
            chars, counts = [st[0]], [1]
            
            for i in range(1, len(st)):
                if st[i] == chars[-1]:
                    counts[-1] += 1
                else:
                    chars.append(st[i])
                    counts.append(1)
            return chars, counts

        ans = 0
        s_chars, s_counts = find2(S)
        for word in words:
            w_chars, w_counts = find2(word)
            
            if s_chars == w_chars:
                c = 0
                for k in range(len(w_chars)):
                    if w_counts[k]==s_counts[k] or (w_counts[k]<s_counts[k] and s_counts[k]>=3):
                        c += 1
                
                if c ==len(w_chars):
                    ans += 1

        return ans
if __name__=="__main__":
    S=input() 
    words=list(map(str,input().split()))
    print(find(S,words))


#CPP SOLUTION
'''
#include<bits/stdc++.h>
using namespace std;

int check(string comp,string s){
    
    int n = comp.length();
    int m = s.length();
    
    int i=0;
    int j=0;
    
    while(i<n && j<m){
        
        int c1=0,c2=0;
        char f,p;
        f=comp[i];
        p=s[j];
        if(f!=p){
            return 0;
        }
        while(i<n && comp[i]==f){
            i++;
            c1++;
        }
        
        while(j<m && s[j]==p){
            j++;
            c2++;
        }
        
        if(c1>c2 || (c2<=2 && c1!=c2)){
            return 0;
        }
        
        
    }
    
    return (i==n && j==m);
    
}


int main(){
    string s;
    cin>>s;
    
    vector<string> temp2;
    string x;
    while(cin>>x){
        temp2.push_back(x);
        if(cin.get()=='\n'){
            break;
        }
        
    }
    
    
    int count=0;
    for(int i=0;i<temp2.size();i++){
        count+=check(temp2[i],s);
        
    }
    cout<<count<<endl;
    
    
    
}
'''