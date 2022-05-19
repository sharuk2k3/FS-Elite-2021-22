/*

You are given a list of Students as StudentList,
Your task is to find out how many male and female students are there in 
the college?

Sample Output:
--------------
{Male=11, Female=6}



The Student class looks like this:
----------------------------------
class Student
{
    int id;
    String name;
    int age;
    String gender;
    String department;
    int yearOfJoining;
    
    public Student(int id, String name, int age, String gender, String department, int yearOfJoining ) 
    {
        this.id = id;
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.department = department;
        this.yearOfJoining = yearOfJoining;
    }
     
    public int getId() 
    {
        return id;
    }
     
    public String getName() 
    {
        return name;
    }
     
    public int getAge() 
    {
        return age;
    }
     
    public String getGender() 
    {
        return gender;
    }
     
    public String getDepartment() 
    {
        return department;
    }
     
    public int getYearOfJoining() 
    {
        return yearOfJoining;
    }
     
    @Override
    public String toString() 
    {
        return "Id : "+id
                +", Name : "+name
                +", Age : "+age
                +", Gender : "+gender
                +", Department : "+department
                +", Year Of Joining : "+yearOfJoining;
    }
}


*/
import java.util.*;


class Day_65_P_1
 {
	public Map<String, Long> numOfMaleAndFemaleStudents(List<Student> StudentList){
        //Implement your code here
        
}
}
