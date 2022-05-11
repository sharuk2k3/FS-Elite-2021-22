/*


Mr Madan is given a line of words as a string, LoW and another set of words as
excluded[].

Your task is to help Mr Madam to return the most repeated word in LoW that is 
not an excluded word. It is guaranteed that there exists at least one word
that is not in excluded list, and the answer is unique.

Note:
The words in 'LoW' are case-insensitive but the answer should be returned in 
lowercase. Consider special characters as split symbols while processing the LoW.

Input Format:
-------------
Line-1: Single line of space separated words, line.
Line-2: Space seprated words, excluded[] the words are in lowercase.

Output Format:
--------------
Print the word, W.

Sample Input:
-------------
KMIT college is having FS classes in KMit Fs Labs
kmit

Sample Output:
--------------
fs


Sample Input-2:
---------------
hello HellO, world
world

Sample Output-2:
----------------
hello


*/

import java.util.*;
import java.util.stream.Stream;
import java.util.function.Function;
import java.util.stream.Collectors;
public class Day_61_P_5{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        List<String>exc=new ArrayList<>();
        String inp[]=sc.nextLine().split("[\\s@&.*%:'?#|$+-,]+");
        String arr[]=sc.nextLine().split(" ");
        for(int i=0;i<arr.length;i++){
            exc.add(arr[i]);
        }
        Arrays.stream(inp)
            .map(x->x.toLowerCase())
            .collect(Collectors.groupingBy(Function.identity(),Collectors.counting()))
            .entrySet()
            .stream()
            .filter(x->!exc.contains(x.getKey()))
            .sorted((x1,x2)->{
                return (int)(x2.getValue()-x1.getValue());
            })
            .limit(1)
            .map(x->{ 
                return x.getKey(); 
            })
            .forEach(System.out::print);
    }
}
