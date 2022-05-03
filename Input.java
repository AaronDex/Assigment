import java.util.Scanner;
public class Input {
    public static String InputName() {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter username");

    final String Name = myObj.nextLine();  // Read user input
    
    return Name;
    }
}
