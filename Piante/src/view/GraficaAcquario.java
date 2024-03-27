package view;

import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.awt.event.*;

public class GraficaAcquario {
    public static void main(String[] args) {
        JFrame frame = new JFrame("ComboBox List Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        DefaultListModel<JPanel> model = new DefaultListModel<>();
        
        for (int i = 1; i <= 10; i++) {
            JPanel panel = new JPanel(new BorderLayout());
            JComboBox<String> comboBox = new JComboBox<>(new String[]{"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"});
            JSpinner spinner = new JSpinner(new SpinnerNumberModel(1, 1, 100, 1));
            
            panel.add(comboBox, BorderLayout.WEST);
            panel.add(spinner, BorderLayout.EAST);
            
            model.addElement(panel);
        }
        
        JList<JPanel> list = new JList<>(model);
        list.setCellRenderer(new ListCellRenderer<JPanel>() {
            @Override
            public Component getListCellRendererComponent(JList<? extends JPanel> list, JPanel value, int index, boolean isSelected, boolean cellHasFocus) {
                return value;
            }
        });
        
        frame.add(new JScrollPane(list));
        
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
