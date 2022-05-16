import java.io.FileWriter;
import java.io.IOException;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class twoUp {
    static boolean coin1 = coinToss.coinToss1();
    static boolean coin2 = coinToss.coinToss2();
    static String name=JOptionPane.showInputDialog("Please Enter Your Name");
    public static void main(String[] args) throws IOException {
        fileHandler.createFile();
        twoUpGUI GUI = new twoUpGUI();
        procces(name);
        GUI.GUI();
    }
    public static void procces(String action) throws IOException {
        
        JFrame jFrame = new JFrame();
        
        switch (action) {
            case "2 Heads":{
                if ((coin1) && (coin2)) {
                    string 
                    JOptionPane.showMessageDialog(jFrame, "You win!");
                    FileWriter myWriter = new FileWriter("Results.txt",true);
                    myWriter.write(name+" Won!"+"\r\n");
                    myWriter.close();
                    
                    break;
                } else {
                    JOptionPane.showMessageDialog(jFrame, "Tou lose");
                    FileWriter myWriter = new FileWriter("Results.txt",true);
                    myWriter.write(name+" Lost!"+"\r\n");
                    myWriter.close();
                    break;
                }}
            case "2 Tails":
                if ((coin1 == false) && (coin2 == false)) {
                    JOptionPane.showMessageDialog(jFrame, "You win!");
                    FileWriter myWriter = new FileWriter("Results.txt",true);
                    myWriter.write(name+" Won!"+"Guess was:" +action+"\r\n");
                    myWriter.close();
                    break;
                } else {
                    JOptionPane.showMessageDialog(jFrame, "You lose");
                    FileWriter myWriter = new FileWriter("Results.txt",true);
                    myWriter.write(name+" Lost!"+"\r\n");
                    myWriter.close();
                    break;
                }
            case "1 Head 1 Tails":
                if (coin1 != coin2) {
                    JOptionPane.showMessageDialog(jFrame, "You win!");
                    FileWriter myWriter = new FileWriter("Results.txt",true);
                    myWriter.write(name+" Won!"+"\r\n");
                    myWriter.close();
                } else {
                    JOptionPane.showMessageDialog(jFrame, "You lose");
                    FileWriter myWriter = new FileWriter("Results.txt",true);
                    myWriter.write(name+" Lost!"+"\r\n");
                    myWriter.close();
                    break;
                }
    
        }
}
}