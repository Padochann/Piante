package view;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<JPanel> panels = new ArrayList<>();

        JFrame frame = new JFrame("GridBagLayout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

        // Crea 30 pannelli e aggiungili alla lista
        for (int i = 0; i < 30; i++) {
            JPanel panel = createPanelWithComponents();
            panels.add(panel);
        }

        // Aggiungi i pannelli al frame
        for (JPanel panel : panels) {
            frame.add(panel);
        }

        frame.setLayout(new GridLayout(10, 3)); // Imposta un layout di griglia per visualizzare 10 pannelli per riga

        JButton removeButton = new JButton("Remove All");
        removeButton.addActionListener(e -> removeAllPanels(frame, panels));

        frame.add(removeButton);

        // Imposta la visibilità del frame
        frame.setVisible(true);
    }

    private static JPanel createPanelWithComponents() {
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

        JLabel label = new JLabel("Label");
        constraints.gridx = 1;
        constraints.gridy = 0;
        panel.add(label, constraints);

        JButton button2 = new JButton("Button 2");
        constraints.gridx = 2;
        constraints.gridy = 0;
        panel.add(button2, constraints);

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
