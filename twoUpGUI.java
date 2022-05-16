import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.plaf.PanelUI;
import javax.swing.plaf.basic.BasicOptionPaneUI.ButtonActionListener;

import java.awt.*;
import java.awt.event.*;
import java.io.IOException;

public class twoUpGUI implements ActionListener{
    public void GUI() {
        JFrame frame = new JFrame("Two-Up");
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        JLabel label = new JLabel("Please select a guess");
        
        JButton button1 = new JButton();
        JButton button2 = new JButton();
        JButton button3 = new JButton();
        button1.setText("2 Heads");
        button2.setText("2 Tails");
        button3.setText("1 Head 1 Tails");
        button1.addActionListener(this);
        button2.addActionListener(this);
        button3.addActionListener(this);
        panel.add(label);
        panel.add(button1);
        panel.add(button2);
        panel.add(button3);
        
        frame.add(panel);
        frame.setSize(500, 100);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        
        e.getActionCommand();
        String action = e.getActionCommand();
        try {
            twoUp.procces(action);
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }
    
    }
  
}
   
    
   
   

    
    
        
    

    