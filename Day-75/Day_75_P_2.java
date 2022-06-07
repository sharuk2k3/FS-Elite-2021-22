/* 

Indus Infra Ltd purchased a land of size L * W acres, for their upcoming venture.
The land is divided into rectangular plots, using fences. They have kept some 
H horizontal fences as hfences[] and V vertical fences as vfences[] on the land,
where hfence[i] is the distance from the top of the land to the i-th horizontal
fence and, vfence[j] is the distance from the top of the land to the j-th 
vertical fence. Each 1*1 cell is one acre plot.

Mr.RGV wants to purchase the biggest plot available to build a Guest-house.
Your task is to help Mr.RGV to find the biggest plot vailable after the fences 
are setup in the venture.
NOTE: The answer can be a large number, return the modulo of 10^9 + 7.

Input Format:
-------------
Line-1: 4 space separated integers, L,W,H and V
Line-2: H space separated integers, hfence[] in the range [0, L]
Line-3: V space sepaarted integers, vfence[] in the range [0, W]

Output Format:
--------------
Print an integer result, the area of biggest plot.


Sample Input-1:
---------------
5 6 2 2
2 3
2 5

Sample Output-1:
----------------
6


Sample Input-2:
---------------
5 6 1 1
3
4

Sample Output-2:
----------------
12
*/

//Solution
import java.util.*;
public class Day_75_P_2 {
    import java.util.*;
    class Solution{
        public static void main(String args[]){
            Scanner sc=new Scanner(System.in);
            int r=sc.nextInt();
            int c=sc.nextInt();
            int h=sc.nextInt();
            int v=sc.nextInt();
            int hor[]=new int[h];
            for(int i=0;i<h;i++){
                hor[i]=sc.nextInt();
            }
            int ver[]=new int[v];
            for(int i=0;i<v;i++){
                ver[i]=sc.nextInt();
            }
            System.out.println(func(r,c,h,v,hor,ver));
        }
        public static int func(int r,int c,int h,int v,int hor[],int ver[]){
            Arrays.sort(hor);
            Arrays.sort(ver);
            int hmax=0;int vmax=0;
            for(int i=0;i<h;i++){
                if(i==0) hmax=Math.max(hmax,hor[i]);
                else{
                    hmax=Math.max(hmax,hor[i]-hor[i-1]);
                }
            }
            hmax=Math.max(hmax,r-hor[h-1]);
            for(int i=0;i<v;i++){
                if(i==0) vmax=Math.max(vmax,ver[i]);
                else{
                    vmax=Math.max(vmax,ver[i]-ver[i-1]);
                }
            }
            vmax=Math.max(vmax,c-ver[v-1]);
            return (int) ((vmax*hmax)%1000000007);
        }
    }
    
    
}
