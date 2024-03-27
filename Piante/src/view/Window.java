package view;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.SpringLayout;
import java.awt.CardLayout;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;

import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JEditorPane;
import javax.swing.DropMode;
import javax.swing.JList;
import javax.swing.JComboBox;
import javax.swing.AbstractListModel;
import javax.swing.JTextPane;
import javax.swing.JCheckBox;
import javax.swing.SwingConstants;
import javax.swing.BoxLayout;
import java.awt.Component;
import javax.swing.ScrollPaneConstants;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import javax.swing.DefaultComboBoxModel;
import javax.swing.border.MatteBorder;
import java.awt.Color;

public class Window extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JPanel panelCardMain;
	private JPanel panelAcquari;
	private JPanel panelCerca;
	private JPanel panelSalva;
	private JPanel panelSections;
	private JScrollPane scrollPaneAcquari;
	private JPanel panelCardAcquari;
	private JPanel panelBtnAcquari;
	private JButton btnNew;
	private JButton btnView;
	private JButton btnDelete;
	private JPanel panelNew;
	private JPanel panelView;
	private JButton btnAcquari;
	private JButton btnCerca;
	private JButton btnSalva;
	private JButton btnSalvaAcquario;
	private JScrollPane scrollPaneDescrizione;
	private JTextArea textArea;
	private JTextField textFieldLitraggio;
	private JTextField textFieldLunghezza;
	private JTextField textFieldLarghezza;
	private JTextField textFieldAltezza;
	private JList listAcquari;
	private JLabel lblDescrizione;
	private JLabel lblLitraggio;
	private JLabel lblLunghezza;
	private JLabel lblLarghezza;
	private JLabel lblAltezza;
	private JList listPlants;
	private JComboBox comboBoxAcquari;
	private JScrollPane scrollPane;
	private JPanel panel;
	private JCheckBox chckbxNewCheckBox;
	private JPanel panel_1;
	private JCheckBox chckbxNewCheckBox_1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Window frame = new Window();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Window() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 956, 440);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		SpringLayout sl_contentPane = new SpringLayout();
		contentPane.setLayout(sl_contentPane);
		
		panelCardMain = new JPanel();
		sl_contentPane.putConstraint(SpringLayout.NORTH, panelCardMain, 15, SpringLayout.NORTH, contentPane);
		sl_contentPane.putConstraint(SpringLayout.WEST, panelCardMain, 11, SpringLayout.WEST, contentPane);
		sl_contentPane.putConstraint(SpringLayout.EAST, panelCardMain, -12, SpringLayout.EAST, contentPane);
		contentPane.add(panelCardMain);
		CardLayout cardLayout = new CardLayout();
		panelCardMain.setLayout(cardLayout);
		
		
		
		panelAcquari = new JPanel();
		panelCardMain.add(panelAcquari, "name_945515184868000");
		SpringLayout sl_panelAcquari = new SpringLayout();
		panelAcquari.setLayout(sl_panelAcquari);
		
		scrollPaneAcquari = new JScrollPane();
		sl_panelAcquari.putConstraint(SpringLayout.NORTH, scrollPaneAcquari, 10, SpringLayout.NORTH, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.WEST, scrollPaneAcquari, 10, SpringLayout.WEST, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.SOUTH, scrollPaneAcquari, -10, SpringLayout.SOUTH, panelAcquari);
		panelAcquari.add(scrollPaneAcquari);
		
		panelCardAcquari = new JPanel();
		sl_panelAcquari.putConstraint(SpringLayout.NORTH, panelCardAcquari, 10, SpringLayout.NORTH, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.WEST, panelCardAcquari, 544, SpringLayout.WEST, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.SOUTH, panelCardAcquari, -10, SpringLayout.SOUTH, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.EAST, panelCardAcquari, -13, SpringLayout.EAST, panelAcquari);
		panelAcquari.add(panelCardAcquari);
		
		panelBtnAcquari = new JPanel();
		sl_panelAcquari.putConstraint(SpringLayout.NORTH, panelBtnAcquari, 10, SpringLayout.NORTH, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.SOUTH, panelBtnAcquari, -10, SpringLayout.SOUTH, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.EAST, scrollPaneAcquari, -6, SpringLayout.WEST, panelBtnAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.WEST, panelBtnAcquari, 456, SpringLayout.WEST, panelAcquari);
		sl_panelAcquari.putConstraint(SpringLayout.EAST, panelBtnAcquari, -6, SpringLayout.WEST, panelCardAcquari);
		
		listAcquari = new JList();
		scrollPaneAcquari.setViewportView(listAcquari);
		panelCardAcquari.setLayout(new CardLayout(0, 0));
		
		panelNew = new JPanel();
		panelCardAcquari.add(panelNew, "name_507475470980800");
		SpringLayout sl_panelNew = new SpringLayout();
		panelNew.setLayout(sl_panelNew);
		
		btnSalvaAcquario = new JButton("Salva");
		sl_panelNew.putConstraint(SpringLayout.NORTH, btnSalvaAcquario, 227, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, btnSalvaAcquario, -10, SpringLayout.EAST, panelNew);
		panelNew.add(btnSalvaAcquario);
		
		scrollPaneDescrizione = new JScrollPane();
		sl_panelNew.putConstraint(SpringLayout.SOUTH, scrollPaneDescrizione, -6, SpringLayout.NORTH, btnSalvaAcquario);
		sl_panelNew.putConstraint(SpringLayout.WEST, scrollPaneDescrizione, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, scrollPaneDescrizione, -10, SpringLayout.EAST, panelNew);
		panelNew.add(scrollPaneDescrizione);
		
		textArea = new JTextArea();
		scrollPaneDescrizione.setViewportView(textArea);
		
		textFieldLitraggio = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldLitraggio, 10, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldLitraggio, -153, SpringLayout.EAST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldLitraggio, 10, SpringLayout.WEST, panelNew);
		panelNew.add(textFieldLitraggio);
		textFieldLitraggio.setColumns(10);
		
		textFieldLunghezza = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.SOUTH, textFieldLitraggio, -17, SpringLayout.NORTH, textFieldLunghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldLunghezza, 0, SpringLayout.EAST, textFieldLitraggio);
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldLunghezza, 47, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldLunghezza, 10, SpringLayout.WEST, panelNew);
		textFieldLunghezza.setColumns(10);
		panelNew.add(textFieldLunghezza);
		
		textFieldLarghezza = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldLarghezza, 86, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldLarghezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldLarghezza, 0, SpringLayout.EAST, textFieldLitraggio);
		sl_panelNew.putConstraint(SpringLayout.SOUTH, textFieldLunghezza, -19, SpringLayout.NORTH, textFieldLarghezza);
		textFieldLarghezza.setColumns(10);
		panelNew.add(textFieldLarghezza);
		
		textFieldAltezza = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.NORTH, scrollPaneDescrizione, 20, SpringLayout.SOUTH, textFieldAltezza);
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldAltezza, 122, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.SOUTH, textFieldLarghezza, -16, SpringLayout.NORTH, textFieldAltezza);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldAltezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldAltezza, 0, SpringLayout.EAST, textFieldLitraggio);
		textFieldAltezza.setColumns(10);
		panelNew.add(textFieldAltezza);
		
		lblDescrizione = new JLabel("Descrizione");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblDescrizione, 231, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, lblDescrizione, 10, SpringLayout.WEST, panelNew);
		panelNew.add(lblDescrizione);
		
		lblLitraggio = new JLabel("Litraggio");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblLitraggio, 10, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblLitraggio, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblLitraggio);
		
		lblLunghezza = new JLabel("Lunghezza");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblLunghezza, 23, SpringLayout.SOUTH, lblLitraggio);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblLunghezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblLunghezza);
		
		lblLarghezza = new JLabel("Larghezza");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblLarghezza, 25, SpringLayout.SOUTH, lblLunghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblLarghezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblLarghezza);
		
		lblAltezza = new JLabel("Altezza");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblAltezza, 22, SpringLayout.SOUTH, lblLarghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblAltezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblAltezza);
		
		panelView = new JPanel();
		panelCardAcquari.add(panelView, "name_507487369534400");
		panelView.setLayout(new GridLayout(1, 0, 0, 0));
		
		listPlants = new JList();
		panelView.add(listPlants);
		panelAcquari.add(panelBtnAcquari);
		panelBtnAcquari.setLayout(new GridLayout(3, 0, 0, 0));
		
		btnNew = new JButton("New");
		panelBtnAcquari.add(btnNew);
		
		btnView = new JButton("View");
		panelBtnAcquari.add(btnView);
		
		btnDelete = new JButton("Delete");
		panelBtnAcquari.add(btnDelete);
		
		panelCerca = new JPanel();
		panelCardMain.add(panelCerca, "name_945526498430100");
		
		panelSalva = new JPanel();
		panelCardMain.add(panelSalva, "name_453599213935200");
		SpringLayout sl_panelSalva = new SpringLayout();
		panelSalva.setLayout(sl_panelSalva);
		
		comboBoxAcquari = new JComboBox();
		sl_panelSalva.putConstraint(SpringLayout.EAST, comboBoxAcquari, -41, SpringLayout.EAST, panelSalva);
		panelSalva.add(comboBoxAcquari);
		
		panelSections = new JPanel();
		sl_contentPane.putConstraint(SpringLayout.SOUTH, panelCardMain, -24, SpringLayout.NORTH, panelSections);
		sl_contentPane.putConstraint(SpringLayout.NORTH, panelSections, -40, SpringLayout.SOUTH, contentPane);
		sl_contentPane.putConstraint(SpringLayout.WEST, panelSections, 10, SpringLayout.WEST, contentPane);
		sl_contentPane.putConstraint(SpringLayout.SOUTH, panelSections, -10, SpringLayout.SOUTH, contentPane);
		sl_contentPane.putConstraint(SpringLayout.EAST, panelSections, -10, SpringLayout.EAST, contentPane);
		contentPane.add(panelSections);
		panelSections.setLayout(new GridLayout(0, 3, 0, 0));
		
		btnAcquari = new JButton("Acquari");
		panelSections.add(btnAcquari);
		
		btnCerca = new JButton("Cerca");
		panelSections.add(btnCerca);
		
		btnSalva = new JButton("Salva");
		panelSections.add(btnSalva);
		
		 // Aggiungi i pannelli al CardLayout
	    panelCardMain.add(panelAcquari, "panelAcquari");
	    panelCardMain.add(panelCerca, "panelCerca");
	    panelCardMain.add(panelSalva, "panelSalva");
	    
	    scrollPane = new JScrollPane();
	    sl_panelSalva.putConstraint(SpringLayout.NORTH, comboBoxAcquari, 0, SpringLayout.NORTH, scrollPane);
	    sl_panelSalva.putConstraint(SpringLayout.WEST, comboBoxAcquari, 22, SpringLayout.EAST, scrollPane);
	    sl_panelSalva.putConstraint(SpringLayout.NORTH, scrollPane, 10, SpringLayout.NORTH, panelSalva);
	    sl_panelSalva.putConstraint(SpringLayout.SOUTH, scrollPane, -10, SpringLayout.SOUTH, panelSalva);
	    sl_panelSalva.putConstraint(SpringLayout.EAST, scrollPane, -286, SpringLayout.EAST, panelSalva);
	    sl_panelSalva.putConstraint(SpringLayout.WEST, scrollPane, 10, SpringLayout.WEST, panelSalva);
	    panelSalva.add(scrollPane);
	    
	    panel = new JPanel();
	    scrollPane.setViewportView(panel);
	    GridLayout panelCart= new GridLayout(30, 1, 0, 0);
	    panel.setLayout(panelCart);
	    
	    panel_1 = new JPanel();
	    panel_1.setBorder(new MatteBorder(1, 1, 1, 1, (Color) new Color(0, 0, 0)));
	    panel.add(panel_1);
	    GridBagLayout gbl_panel_1 = new GridBagLayout();
	    gbl_panel_1.columnWidths = new int[]{0, 0, 0, 0};
	    gbl_panel_1.rowHeights = new int[]{0, 0};
	    gbl_panel_1.columnWeights = new double[]{0.0, 1.0, 0.0, Double.MIN_VALUE};
	    gbl_panel_1.rowWeights = new double[]{0.0, Double.MIN_VALUE};
	    panel_1.setLayout(gbl_panel_1);
	    
	    chckbxNewCheckBox_1 = new JCheckBox("");
	    GridBagConstraints gbc_chckbxNewCheckBox_1 = new GridBagConstraints();
	    gbc_chckbxNewCheckBox_1.insets = new Insets(0, 0, 0, 5);
	    gbc_chckbxNewCheckBox_1.anchor = GridBagConstraints.NORTHWEST;
	    gbc_chckbxNewCheckBox_1.gridx = 0;
	    gbc_chckbxNewCheckBox_1.gridy = 0;
	    panel_1.add(chckbxNewCheckBox_1, gbc_chckbxNewCheckBox_1);
	    
	    JLabel lblNewLabel = new JLabel("Rotala rotundifollia var \"hraa\"");
	    lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
	    GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
	    gbc_lblNewLabel.fill = GridBagConstraints.HORIZONTAL;
	    gbc_lblNewLabel.insets = new Insets(0, 0, 0, 5);
	    gbc_lblNewLabel.gridx = 1;
	    gbc_lblNewLabel.gridy = 0;
	    panel_1.add(lblNewLabel, gbc_lblNewLabel);
	    
	    JSpinner s = new JSpinner();
	    JComboBox comboBox = new JComboBox();
	    comboBox.setModel(new DefaultComboBoxModel(new String[] {"Q", "1", "2", "3"}));
	    comboBox.setEnabled(true);
	    comboBox.setEditable(false);
	    GridBagConstraints gbc_comboBox = new GridBagConstraints();
	    gbc_comboBox.fill = GridBagConstraints.HORIZONTAL;
	    gbc_comboBox.gridx = 2;
	    gbc_comboBox.gridy = 0;
	    panel_1.add(comboBox, gbc_comboBox);
	    
	
	    
	 // Aggiungi un ActionListener ai bottoni per cambiare il pannello visualizzato
	    btnAcquari.addActionListener(e -> cardLayout.show(panelCardMain, "panelAcquari"));
	    btnCerca.addActionListener(e -> cardLayout.show(panelCardMain, "panelCerca"));
	    btnSalva.addActionListener(e -> cardLayout.show(panelCardMain, "panelSalva"));
	}
}
