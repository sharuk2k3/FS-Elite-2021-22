'''

Sri Vihaan Travels announced a family trip to Sri Nagar, for which they began 
taking reservations. They are only offering 2 and 3 seater tickets for this trip.

Each member of certain groups is identifiable by the group ID to which he or 
she belongs. Each group is uniquely identified by its group ID.

The ticket will only be issued to members of the same group, the travel 
administration decided. It is decided that No wasted tickets will be issued 
(i.e., If a person is alone, then he is not allowed to get a ticket).

You are given a list of integers person_id[], where person_id[i] is the group ID 
of ith person in the list. Your objective is to determine fewernumber of tickets 
should be issued to cover everyone in each group. Print -1, if it is not possible.


Input Format:
-------------
Line-1: Comma separated integers, Person's group-ID

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
1,1,3,2,2,2,1,2,2,3

Sample Output-1:
----------------
4

Explanation: 
------------
Tohey can book the tickets for all the people, as follows:
- Issue the 3-seater ticket, to group with ID-1 of size 3.
- Issue the 2-seater ticket, to group with ID-3 of size 2.
- Issue the 3-seater ticket, to group with ID-2 of size 5.
- Issue the 2-seater ticket, to group with ID-2 of size 5.
So, you have issued 4 tickets in total.


Sample Input-2:
---------------
1,1,1,2,2,3

Sample Output-2:
----------------
-1

Explanation: 
------------
There is a group with ID-3 of size 1. 
The administration's ruling states that a single person cannot receive a ticket.
So, print -1.


'''

#Java Solution


'''
import java.util.*;

class main{
    static int tickets(String[] in){
        Map<String,Integer> map = new HashMap<>();
        for(String s : in) map.put(s,map.getOrDefault(s,0)+1);
        
        int ans = 0;
        for(String key : map.keySet()){
            int n_persons = map.get(key);
            if(n_persons>1){
                int rem = n_persons%3;
                if(rem == 0) ans += n_persons/3;
                else if(rem==1){
                    int k = n_persons/3;
                    ans += (k-1);
                    ans += 2;
                    
                }
                else{
                    ans += (n_persons/3);
                    ans+= 1;
                    
                }
                
            }
            else return -1;
            
        }
        
        return ans;
        
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        String[] in = sc.nextLine().split(",");
        System.out.println(tickets(in));
        
    }
    
}
'''