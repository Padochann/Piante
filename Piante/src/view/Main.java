package view;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Main {
    private static List<JPanel> panels = new ArrayList<>();

    public static void main(String[] args) {
        JFrame frame = new JFrame("GridBagLayout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);


        frame.setLayout(new GridLayout(31, 1)); // Imposta un layout di griglia per visualizzare 30 pannelli in una colonna
        JButton removeButton = new JButton("Remove All");
        removeButton.addActionListener(e -> removeAllPanels(frame, panels));

        frame.add(removeButton);
        // Imposta la visibilità del frame
        // Crea 30 pannelli e aggiungili alla lista
        for (int i = 0; i < 30; i++) {
        	JPanel panel = createPanelWithComponents(i);
        	panels.add(panel);
        	frame.add(panel);
        }
        frame.setVisible(true);
    }

    private static JPanel createPanelWithComponents(int num) {
        JPanel panel = new JPanel();
        GridBagLayout gridBagLayout = new GridBagLayout();
        panel.setLayout(gridBagLayout);

        // Aggiungi componenti al pannello
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.fill = GridBagConstraints.HORIZONTAL;

        JButton button1 = new JButton("Button 1");
        constraints.gridx = 0;
        constraints.gridy = 0;
        panel.add(button1, constraints);

        JLabel label = new JLabel("Label"+num);
        constraints.gridx = 1;
        constraints.gridy = 0;
        panel.add(label, constraints);

        JButton button2 = new JButton("Button 2");
        constraints.gridx = 2;
        constraints.gridy = 0;
        panel.add(button2, constraints);

        // Aggiungi un ascoltatore al button2 per rimuovere il pannello
        button2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Rimuovi il pannello dalla tabella
                JPanel parentPanel = (JPanel) button2.getParent();
                parentPanel.removeAll();
                parentPanel.revalidate();
                parentPanel.repaint();

                // Rimuovi il pannello dalla lista
                Iterator<JPanel> iterator = panels.iterator();
                while (iterator.hasNext()) {
                    JPanel currentPanel = iterator.next();
                    if (currentPanel == parentPanel) {
                        iterator.remove();
                        break;
                    }
                }

                // Rimuovi tutti i componenti dal frame
                JFrame frame = (JFrame) SwingUtilities.getWindowAncestor(parentPanel);
                frame.getContentPane().removeAll();
                
                // Aggiungi tutti i pannelli aggiornati al frame
                for (JPanel panel : panels) {
                    frame.add(panel);
                }
 
                // Aggiorna il layout del frame
                frame.setLayout(new GridLayout(panels.size(), 1));  // Imposta un layout di griglia dinamico con una sola colonna
                frame.revalidate();
                frame.repaint();
            }
        });
        
        return panel;
    }
    private static void removeAllPanels(JFrame frame, List<JPanel> panels) {
        for (JPanel panel : panels) {
            frame.remove(panel);
        }
        panels.clear();
        frame.revalidate();
        frame.repaint();
    }
}
