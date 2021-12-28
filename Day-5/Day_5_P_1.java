/*
There are a group of kids playing a game in a circle.This game is to check their
Arithmetic division skills.We will start the game by selecting a kid and he has 
to say 1 to start the game and the next kid turn arrives he has to say next 
number but with the following rules.
   - if number is divisible by 3 then the answer is "Hi".
   - if number is divisible by 5 then the answer is "Hello".
   - if number is divisible by both 3 and 5 then the answer is "HiHello".
   - else the answer is the number itself.

 Given a number N , return a string array result[] (1-indexed),which consists the 
 answers from kid-1 to kid-N.

Input Format:
-------------
Line-1: An integer N.

Output Format:
--------------
Print a string array[].

Constraints:
• 1 <= n <= 10^4
 
Sample Input-1:
---------------
4

Sample Output-1:
----------------
1 2 Hi 4 


Sample Input-2:
---------------
15

Sample Output-2:
----------------
1 2 Hi 4 Hello Hi 7 8 Hi Hello 11 Hi 13 14 HiHello 
 


*/

import java.util.Scanner;

class SharedData {
	int i=1;
	int n = 0;
	
	SharedData(int n){
		this.n = n;
	}
	
	public synchronized int getCurrent() {
		if(i<=n)
		return i;
		else
		return -1;
	}
	
	public  synchronized void setCurrent() {
		this.i++;
	}
}

class Thread1 implements Runnable {

	SharedData data;
	
	Thread1(SharedData obj){
		data = obj;
	}
	
	@Override
	public void run() {
		synchronized(data) {
		while(data.getCurrent()!=-1) {
			if(data.getCurrent()%3 != 0 && data.getCurrent()%5 != 0) {
				System.out.print(data.getCurrent()+" ");
				data.setCurrent();
				
				data.notifyAll();
				
			} else {
				try {
				data.wait();
				} catch(Exception e) {
					System.out.println("Error");
				}
			}
		}
		}
		
	}
	
}

class Thread2 implements Runnable {

SharedData data;
	
	Thread2(SharedData obj){
		data = obj;
	}
	
	@Override
	public void run() {
		synchronized(data) {
		while(data.getCurrent()!=-1) {
			if(data.getCurrent()%3 == 0 && data.getCurrent()%5 != 0) {
				System.out.print("Hi ");
				data.setCurrent();
				data.notifyAll();
			}  else {
				try {
				data.wait();
				} catch(Exception e) {
					System.out.println("Error");
				}
			}
	}
		}
	
}
}

class Thread3 implements Runnable {
	
SharedData data;
	
	Thread3(SharedData obj){
		data = obj;
	}

	@Override
	public void run() {
		
		synchronized(data) {
		while(data.getCurrent()!=-1) {
			if(data.getCurrent()%3 != 0 && data.getCurrent()%5 == 0) {
				System.out.print("Hello ");
				data.setCurrent();
				data.notifyAll();
			} else {
				try {
				data.wait();
				} catch(Exception e) {
					System.out.println("Error");
				}
			}
		}
		}
	}
	
}

class Thread4 implements Runnable {

SharedData data;
	
	Thread4(SharedData obj){
		data = obj;
	}
	
	@Override
	public void run() {
		
	synchronized(data) {
		while(data.getCurrent()!=-1) {
			if(data.getCurrent()%3 == 0 && data.getCurrent()%5 == 0) {
				System.out.print("HiHello ");
				data.setCurrent();
				data.notifyAll();
			}  else {
				try {
				data.wait();
				} catch(Exception e) {
					System.out.println("Error");
				}
			}
	}
	}
	}
}


public class Test {
		public static void main(String args[]) {
			Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			SharedData obj = new SharedData(n);
			
			Thread t1 = new Thread(new Thread1(obj));
			Thread t2 = new Thread(new Thread2(obj));
			Thread t3 = new Thread(new Thread3(obj));
			Thread t4 = new Thread(new Thread4(obj));
			
			t1.start();
			t2.start();
			t3.start();
			t4.start();
			
			sc.close();
		}
}