/*Suppose you are given the following code:

class KmitNgit {
  public void kmit() {
    for (int i = 0; i < n; i++) {
      print("Kmit");
    }
  }

  public void ngit() {
    for (int i = 0; i < n; i++) {
      print("Ngit");
    }
  }
}

The same instance of KmitNgit will be passed to two different threads. 
Thread A will call kmit() while thread B will call ngit(). 
Modify the given program to output "KmitNgit" n times.

Input Format:
-------------
An integer N.

Output Format:
--------------
Print KmitNgit for N times using threads.


Sample Input:
-------------
1
Sample Output:
--------------
KmitNgit

Explanation:
------------
There are two threads being fired asynchronously. 
One of them calls kmit(), while the other calls ngit(). 
"KmitNgit" is being output 1 time.


Sample Input:
-------------
2

Sample Output:
--------------
KmitNgitKmitNgit

Explanation:
------------
"KmitNgit" is being output 2 times.*/

import java.util.*;


class KmitNgit {
    
    int n = 0;
    boolean isKmit = false;
    
    KmitNgit(int n){
        this.n = n;
    }
    
    public synchronized void kmit() {
        while(isKmit){
            try{
            wait();
            } catch(Exception e){
                
            }
  }
  for (int i = 0; i < n && !isKmit; i++) {
      System.out.print("Kmit");
      isKmit = true;
    }
    this.notify();
    }

  public synchronized void ngit() {
      while(!isKmit){
            try{
            wait();
            } catch(Exception e){
                
            }
  }
    for (int i = 0; i < n && isKmit; i++) {
      System.out.print("Ngit");
      isKmit = false;
    }
    n--;
      this.notify();
  }
}

class Thread1 implements Runnable {
    
    KmitNgit obj;
    
    Thread1(KmitNgit obj) {
        this.obj = obj;
    }
    
    public void run() {
        synchronized(obj){
            while(obj.n>0){
        obj.kmit();
            }
    }
    }
}

class Thread2 implements Runnable {
    
    KmitNgit obj;
    
    Thread2(KmitNgit obj) {
        this.obj = obj;
    }
    
    
    public void run() {
        synchronized(obj){
            while(obj.n>0){
        obj.ngit();
            }
    }
    }
}

public class Test {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        KmitNgit obj = new KmitNgit(n);
        Thread t1 = new Thread(new Thread1(obj));
        Thread t2 = new Thread(new Thread2(obj));
        t1.start();
        t2.start();
        sc.close();
    }
}
