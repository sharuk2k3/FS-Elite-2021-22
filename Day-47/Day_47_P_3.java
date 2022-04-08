/*
Write a Java Program which read atmost 5 files and a dictionary of pair of words,
A pair of word looks like, pair[]=["first","second"], in one operation 
replace all occurences of first word with second word.
for example, pair[]={"hello", "hi"}, you need to replace all the occurneces 
of "hello" with "hi" in every file.

You need to create callables for each file, and you need to perform the 
above operation for every pair of words in the dictionary.

Return the result as single string, 
String s=data from (paragraph1.txt+pragraph2.txt+..+pragraph5.txt)

Hint:
Available file names:
paragraph1.txt
paragraph2.txt
paragraph3.txt
paragraph4.txt
paragraph5.txt

Input Format:
-------------
Line-1: Space separated pair of words, dictionary.
        each pair is '-' separated.
Line-2: space separated strings, filenames.


Output Format:
--------------
Print a string result.

Sample Input-1:
---------------
india-bharath from-to bitter-sweeter
paragraph1.txt paragraph2.txt paragraph3.txt

Sample Output-1:
----------------
Large output:

*/

import java.util.*;
import java.io.*;
import java.util.concurrent.*;

class Day_47_P_3 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String[] pair = sc.nextLine().split("-");
        String[] files = sc.nextLine().split(" ");
        ExecutorService executor = Executors.newFixedThreadPool(files.length);
        for (String file : files) {
            executor.submit(new replace(file, pair));
        }
        executor.shutdown();
        while (!executor.isTerminated()) {
        }
        System.out.println(replace.result);
    }
}

