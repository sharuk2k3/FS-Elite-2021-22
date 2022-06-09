/*

Jason Statham is a well known transporter.
He transports goods from one place to other place using his container.
The container is divided into M*N slots, you can place M*N items in it.
In the container few slots are closed, you can't use them.
No other item can move from it.

When the items are loaded the container looks like an M*N grid, 
but to unload the items from the container it is turned 90-derees clockwise.
So, the Items in the container moves through the empty slots and set one on one.
If there is an closed slot, the items will be fall on the closed slot.

You will be given a matrix of size M*N, consists of 3 letters [I,O,S]
Where I indicates item, O indicates closed slot, S indicates empty slot.

Your task is to help Jason Stathamto know the positions of items, empty slots and 
closed slots after turning the container 90-degree clockwise.

Input Format:
-------------
Line-1: Two space separated integers M and N, size of the container
Next M lines: A string of length N, consists only 3 characters [I, O, S]

Output Format:
--------------
Print a charcter matrix of size N*M as described in sample.


Sample Input-1:
---------------
2 3
ISI
ISO

Sample Output-1:
----------------
SS
II
OI

Explanation:
------------
Look at hint for explanation.


Sample Input-2:
---------------
3 6
IIOSOS
IIIOSS
IIISIS

Sample Output-2:
----------------
SII
SII
IIO
IOS
ISO
ISS

Explanation:
------------
Look at hint for explanation.



*/

//Solution



class Day_76_P_2{

        public static void main(String args[]){
            Scanner sc=new Scanner(System.in);
            String p=sc.next();
            String q=sc.next();
            System.out.print(find(0,p,q) || find(0,q,p));
        }
        public static boolean isPalindrome(String s){
            int l=0,r=s.length()-1;
            while(l<=r){
                if(s.charAt(l)!=s.charAt(r))
                    return false;
                l+=1;
                r-=1;
            }
            return true;
        }
        public static boolean find(int loc,String p,String q){
            if(loc>=p.length())
                return false;
            if(isPalindrome(p.substring(0,loc+1)+q.substring(loc+1))||isPalindrome(q.substring(0,loc+1)+p.substring(loc+1)))
                return true;
            return find(loc+1,p,q);
        }
}


