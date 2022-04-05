/*

Shakuni playing 'Paramapadasopanam' game with Dharamaraja.
Shakuni wants to win everytime. He has a boon that whenever he used to 
roll the dice, the dice roll to show his desired number. 

Rules
--------
The game is played with a cubic dice of 6 faces numbered 1 to 6.
And Paramapadasopanam of size N*N.
- Starting from square X = 1, reach the square N*N with some rolls of the dice 
- Once Shakuni roll the dice, he will land on one of the followin squares only
  X+1, X+2, X+3, X+4, X+5, X+6.
- If current value at position X is not equal to -1, then there is a ladder 
  or snake.
- If the position of X is at the base of a ladder, the player must climb 
  the ladder. Ladders go up only.
- If the position of X is at the mouth of a snake, the player must go down 
  the snake and come out through the tail. Snakes go down only.

You have to findout, what would be the least number of rolls required 
for shakuni to win.

Note:
Shakuni can only take a snake or ladder at most once per move: 
if the tail of a snake or ladder is the start of another snake or ladder, 
you do not continue moving.


Input Format:
-------------
Line-1: An integer n , size of Paramapadasopanam.
Next N lines: N space separated integers, either -1 or 
              an integer between 1 to n*n. 

Output Format:
--------------
Print an integer, least number of rolls required for shakuni to win.


Sample Input-1:
---------------
6
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
-1 35 -1 -1 13 -1
-1 -1 -1 -1 -1 -1
-1 15 -1 -1 -1 -1

Sample Output-1:
----------------
4

Explanation: 
------------
At the beginning, you start at square 1.
Roll the dice to land at square 2, and must take the ladder to square 15.
Roll the dice to land at square 17, and must take the snake to square 13.
Roll the dice to land at square 14, and must take the ladder to square 35.
Roll the dice to land at square 36, Shakuni Won.
Total number of rolls are 4.



*/

import java.util.*;
class Box{
    int src;
    int level;
    Box(int s,int l){
        src = s;
        level = l;
    }
}
class Test{
    static int n;
    static boolean visited[];
    static ArrayList<Integer> arr;
    static int BFS(){
        Queue<Box> queue = new LinkedList<Box>();
        queue.add(new Box(1,0));
        while(!queue.isEmpty()){
            Box front = queue.remove();
            int s = front.src;
            int l = front.level;
            if(s==n*n)
                return l;
            visited[s] = true;
            for(int i=1;i<=6;i++){
                int d = s+i;
                if(d>n*n)
                    break;
                if(arr.get(d)!=-1)
                    d = arr.get(d);
                if(!visited[d]){
                    queue.add(new Box(d,l+1));
                    visited[d] = true;
                    if(d==n*n)
                        return l+1;
                }
            }
        }
        return -1;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        visited = new boolean[(n*n)+1];
        boolean reverse = true;
        if(n%2==0)
            reverse = false;
        ArrayList<Integer> board = new ArrayList<Integer>((n*n)+1);
        for(int i=0;i<n;i++){
            ArrayList<Integer> row = new ArrayList<Integer>(n);
            for(int j=0;j<n;j++){
                int x = sc.nextInt();
                row.add(x);
            }
            if(reverse){
                Collections.reverse(row);
                reverse = false;
            }
            else{
                reverse = true;
            }
            board.addAll(row);
        }
        Collections.reverse(board);
        board.add(0,0);
        arr = board;
        System.out.print(BFS());
    }
}