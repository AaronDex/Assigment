import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors

public class WriteToFile {
  public static void Write(){
String[] Words={"Hello"};
    try {
      FileWriter myWriter = new FileWriter("filename.txt");
      myWriter.write(Input.InputName() + "'s Ticket Number Is " + RanGen.NumGen());
      myWriter.close();
      System.out.println("Successfully wrote to the file.");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}