/*


Bob Khan is working with various number systems.
He has created two kinds of addressing systems to share information 
between any two electronic devices.

Addresses in Type-I has following properties:
	- This addressing has four parts, each part is called as 'octet'
	- each octet can have a decimal value between 0 to 255 only
	- each part is separated by periods(.) 
	- Leading 0's are not allowed.
	- each part should conatins atmost 3 digits.

if any octet in the 4 parts, is not satisfying the rules
specified said to be  "invalid" addressing.


Addresses in Type-II has following properties:
	- This addressing has eight parts, each part is called as 'hextet'
	- each hextext can have a hexadecimal value between 0 to ffff only
	- each part is separated by colons (:) 
	- each part should conatins atmost 4 alphanumerics, 
	  as per hexademial number system.

if any hextet in the 8 parts, is not satisfying the rules
specified said to be "Invalid" addressing.
		
You will be given an address as a string	addr.
Your task is to find, whether the given address "addr" belongs to which asddress type.
And return "Type-I" if belongs to "Type-I" Addressing, 
return "Type-II" if belongs to "Type-II" Addressing, 
return "Invalid" if not belongs to either "Type-I"  or "Type-II"Addressing.


Input Format:
-------------
A string, an address addr.

Output Format:
--------------
Print a string output, as mentioned in above statement.


Sample Input-1:
---------------
213.234.45.12

Sample Output-1:
----------------
Type-I


Sample Input-2:
---------------
abcd:ef12:3456:7:dce8:fab9:1:0cda

Sample Output-2:
----------------
Type-II


Sample Input-3:
---------------
abcd:ef12:3456:7:0dce8:fab9:1:0cda

Sample Output-3:
----------------
Invalid


Sample Input-4:
---------------
123.234.34@.31

Sample Output-4:
----------------
Invalid


*/

//Solution

import java.util.*;


class Day_81_P_2 {
    public static String AddresSystem(String queryIP) {
        if(queryIP.indexOf(".") != -1){
            String arr[] = queryIP.split("[.]", -1);
                        
            if(arr.length != 4){
                return "Invalid";
            }
            
            for(String s : arr){
                if(s.equals("")){
                    return "Invalid";
                }
                if(s.charAt(0) == '0' && s.length() > 1){
                    return "Invalid";
                }
                try{
                    int num = Integer.parseInt(s);
                    if(num > 255 || num < 0){
                        return "Invalid";
                    }
                }
                catch(Exception e){
                    return "Invalid";
                }
            }
            
            return "Type-I";
        }   
        
        if(queryIP.indexOf(":") != -1){
            String arr[] = queryIP.split(":", -1);
                        
            if(arr.length != 8){
                return "Invalid";
            }
            
            for(String s : arr){
                if(s.equals("")){
                    return "Invalid";
                }
                if(s.length() < 1 || s.length() > 4){
                    return "Invalid";
                }
                
                for(int i = 0; i < s.length(); i++){
                    char ch = s.charAt(i);
                    if(Character.isDigit(ch)){
                        continue;
                    }
                    else{
                        if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')){
                            if((ch >= 'a' && ch <= 'f') || (ch >= 'A' && ch <= 'F')){
                                continue;
                            }
                            else{
                                return "Invalid";
                            }
                        }
                        else{
                            return "Invalid";
                        }
                    }
                }
            }
            
            return "Type-II";
        }
        
        return "Invalid";
    }
    public static void main(String[] args){
        
        String queryIP;
        Scanner sc = new Scanner(System.in);
        
        queryIP = sc.next();
        System.out.println(AddresSystem(queryIP));
        
        
    }
}