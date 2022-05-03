import java.util.Scanner;
public class Input{
    public static String InputName() {
    Scanner inputname = new Scanner(System.in); 
    System.out.println("Enter username");

    String Name = inputname.nextLine();  
    inputname.close();

    return Name.toString();
    }
}
