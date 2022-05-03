
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.ArrayList;
import java.util.List;
public class MyApp{
    public static void main(String[] args) throws IOException {
    int num =RanGen.NumGen();
    String Name=Input.InputName();
    String check=Integer.toString(num);
    System.out.println(Name + "'s Ticket Number Is :"+ num);
    try {
      FileWriter myWriter = new FileWriter("filename.txt",true);
      myWriter.write(Name + "'s Ticket Number Is :"+ num+  "\r\n"   );
      myWriter.close();
      System.out.println(" Successfully wrote to the file.");
    } catch (IOException e) {
      System.out.println(" An error occurred.");
      e.printStackTrace();
    }
 // list that holds strings of a file
 List<String> listOfStrings = new ArrayList<String>();

// load data from file
BufferedReader bf = new BufferedReader(new FileReader("filename.txt"));

// read entire line as string
String line = bf.readLine();

// checking for end of file
while (line != null) {listOfStrings.add(line);
line = bf.readLine();
}

// closing bufferreader object
bf.close();

// storing the data in arraylist to array
String[] array= listOfStrings.toArray(new String[0]);

 }}
    