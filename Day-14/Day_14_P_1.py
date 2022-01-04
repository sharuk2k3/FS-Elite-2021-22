'''

PROGRAM TO DO IN 7 mins 



Alice wants send a mail to his clients,
He has saved the clients Mail IDs in a list.
There exists an email parser, which perform the following checks 
and send the mail to the distinct clients, the checks are as follows:
- Each mail id has two parts, one is username one is domain name.
- The part before the @ symbol is username, and other is domain name.
- In username, if there exists a '.' symbol, remove it.
- In username, if there exists a '+' symbol, ignore the 
  suffix of the username from that symbol (including '+') 
- In domain name, the '.' symbol will be stays as it is.
- There will be no '+' symbol in domain name.

After performing above checks, your task is to find the count
of distinct client mail ids, who recieves the mail sent by Alice.

Input Format:
-------------
Space separated strings, emails list[].

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
a.v.nagireddy@kmit.in av.nagireddy@gmail.com avnagireddy@kmit.in a.v.nagireddy+org@kmit.in

Sample Output-1:
----------------
2

Explanation:
------------
These 3 mail id's: a.v.nagireddy@kmit.in, avnagireddy@kmit.in, a.v.nagireddy+org@kmit.in
are belons to same client with mail ID: avnagireddy@kmit.in
and another client with mail ID-av.nagireddy@gmail.com
So, there are 2 distinct clients.


Sample Input-2:
---------------
avnreddy@gmail.com avnreddy@yahoo.co.in nsudha@outlook.com

Sample Output-2:
----------------
3

Explanation:
------------
All 3 mail IDs belons to different clients.


'''

#SOLUTION 80/100

def func(lst,ans):
    for i in lst:
        at=i.index("@")
        if("+" in i):
            plus=i.index("+")
            i=i.replace(i[plus:at],"")
        if("." in i[:at]):
            temp=i[:at]
            temp=temp.replace(".","")
            i=i.replace(i[:at],temp)
        ans.append(i)
    return ans
lst=list(input().split())
ans=[]
ans=func(lst,ans)
print(len(set(ans)))


#JAVA SOLUTION 100/100
'''
import java.util.*;
class Test
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        newMail(s);
    }
    public static void newMail(String s)
    {
        String s_arr[] = s.split(" ");
        Set<String> set = new HashSet<>();
        for(int i=0;i<s_arr.length;i++)
        {
            set.add(update(s_arr[i]));
        }
        System.out.println(set.size());
    }
    public static String update(String s)
    {
        String str[] = s.split("@");
        str[0]=str[0].replace(".","");
        for(int i=0;i<str[0].length();i++)
        {
            if(str[0].charAt(i)=='+')
            {
                str[0]=str[0].replace(str[0].substring(i,str[0].length()),"");
                break;
            }
            
        }
        return str[0].toString()+str[1].toString();
    }
}'''