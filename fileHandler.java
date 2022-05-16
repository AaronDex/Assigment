import java.io.File;
import java.io.IOException; 

public class fileHandler {
    public static void createFile() {
        File result = new File("Results.txt"); // Specify the filename
            try {
                result.createNewFile();
            } catch (IOException e) {
                
            }
        
    }
}
