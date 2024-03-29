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
import javax.swing.SpinnerNumberModel;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.forms.layout.ColumnSpec;
import com.jgoodies.forms.layout.RowSpec;
import com.jgoodies.forms.layout.FormSpecs;
import net.miginfocom.swing.MigLayout;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.LayoutStyle.ComponentPlacement;

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
	private JComboBox comboBoxAcquari;
	private JScrollPane scrollPane;
	private JPanel panel;
	private JCheckBox chckbxNewCheckBox;
	private JPanel panel_1;
	private JCheckBox chckbxNewCheckBox_1;
	private JSpinner spinner;
	private JButton btnAggiungiPiante;
	private JScrollPane scrollPane_1;
	private JPanel panel_2;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private JLabel lblNewLabel_1;
	private JLabel lblNewLabel_2;
	private JLabel lblNewLabel_3;
	private JLabel lblNewLabel_4;
	private JScrollPane scrollPane_2;
	private JTextArea textArea_1;
	private JLabel lblNewLabel_5;
	private JScrollPane scrollPane_3;
	private JList list;
	private JComboBox comboBox;
	private JComboBox comboBox_1;
	private JComboBox comboBox_2;
	private JComboBox comboBox_3;
	private JLabel lblNewLabel_6;
	private JLabel label;
	private JLabel lblNewLabel_7;
	private JLabel lblNewLabel_8;
	private JButton btnNewButton;
	private JTextField textField_4;
	private JScrollPane scrollPane_4;
	private JLabel lblNewLabel_9;
	private JList list_12;

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
		setBounds(100, 100, 956,446);
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
		listAcquari.setModel(new AbstractListModel() {
			String[] values = new String[] {};
			public int getSize() {
				return values.length;
			}
			public Object getElementAt(int index) {
				return values[index];
			}
		});
		scrollPaneAcquari.setViewportView(listAcquari);
		panelCardAcquari.setLayout(new CardLayout(0, 0));
		
		panelNew = new JPanel();
		panelCardAcquari.add(panelNew, "name_507475470980800");
		SpringLayout sl_panelNew = new SpringLayout();
		panelNew.setLayout(sl_panelNew);
		
		btnSalvaAcquario = new JButton("Salva");
		sl_panelNew.putConstraint(SpringLayout.SOUTH, btnSalvaAcquario, -10, SpringLayout.SOUTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, btnSalvaAcquario, -10, SpringLayout.EAST, panelNew);
		panelNew.add(btnSalvaAcquario);
		
		scrollPaneDescrizione = new JScrollPane();
		sl_panelNew.putConstraint(SpringLayout.WEST, scrollPaneDescrizione, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.SOUTH, scrollPaneDescrizione, -6, SpringLayout.NORTH, btnSalvaAcquario);
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
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblDescrizione, 4, SpringLayout.NORTH, btnSalvaAcquario);
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
		
		scrollPane_1 = new JScrollPane();
		scrollPane_1.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		panelView.add(scrollPane_1);
		
		panel_2 = new JPanel();
		scrollPane_1.setViewportView(panel_2);
		
		textField = new JTextField();
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setColumns(10);
		
		textField_2 = new JTextField();
		textField_2.setColumns(10);
		
		textField_3 = new JTextField();
		textField_3.setColumns(10);
		
		lblNewLabel_1 = new JLabel("New label");
		
		lblNewLabel_2 = new JLabel("New label");
		
		lblNewLabel_3 = new JLabel("New label");
		
		lblNewLabel_4 = new JLabel("New label");
		
		scrollPane_2 = new JScrollPane();
		
		lblNewLabel_5 = new JLabel("New label");
		
		scrollPane_3 = new JScrollPane();
		GroupLayout gl_panel_2 = new GroupLayout(panel_2);
		gl_panel_2.setHorizontalGroup(
			gl_panel_2.createParallelGroup(Alignment.TRAILING)
				.addGroup(gl_panel_2.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_panel_2.createParallelGroup(Alignment.LEADING)
						.addComponent(scrollPane_3, GroupLayout.DEFAULT_SIZE, 311, Short.MAX_VALUE)
						.addComponent(scrollPane_2, GroupLayout.DEFAULT_SIZE, 311, Short.MAX_VALUE)
						.addGroup(gl_panel_2.createSequentialGroup()
							.addComponent(textField, GroupLayout.DEFAULT_SIZE, 184, Short.MAX_VALUE)
							.addGap(81)
							.addComponent(lblNewLabel_1))
						.addGroup(gl_panel_2.createSequentialGroup()
							.addComponent(textField_1, GroupLayout.DEFAULT_SIZE, 184, Short.MAX_VALUE)
							.addGap(81)
							.addComponent(lblNewLabel_2))
						.addGroup(gl_panel_2.createSequentialGroup()
							.addComponent(textField_2, GroupLayout.DEFAULT_SIZE, 184, Short.MAX_VALUE)
							.addGap(81)
							.addComponent(lblNewLabel_3))
						.addGroup(gl_panel_2.createSequentialGroup()
							.addComponent(textField_3, GroupLayout.DEFAULT_SIZE, 184, Short.MAX_VALUE)
							.addGap(81)
							.addComponent(lblNewLabel_4))
						.addComponent(lblNewLabel_5))
					.addContainerGap())
		);
		gl_panel_2.setVerticalGroup(
			gl_panel_2.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_panel_2.createSequentialGroup()
					.addContainerGap()
					.addGroup(gl_panel_2.createParallelGroup(Alignment.BASELINE)
						.addComponent(textField, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addComponent(lblNewLabel_1))
					.addGap(18)
					.addGroup(gl_panel_2.createParallelGroup(Alignment.BASELINE)
						.addComponent(textField_1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addComponent(lblNewLabel_2))
					.addGap(18)
					.addGroup(gl_panel_2.createParallelGroup(Alignment.BASELINE)
						.addComponent(textField_2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addComponent(lblNewLabel_3))
					.addGap(18)
					.addGroup(gl_panel_2.createParallelGroup(Alignment.BASELINE)
						.addComponent(textField_3, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addComponent(lblNewLabel_4))
					.addPreferredGap(ComponentPlacement.UNRELATED)
					.addComponent(scrollPane_2, GroupLayout.PREFERRED_SIZE, 93, GroupLayout.PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(lblNewLabel_5)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(scrollPane_3, GroupLayout.DEFAULT_SIZE, 189, Short.MAX_VALUE)
					.addContainerGap())
		);
		
		list = new JList();
		scrollPane_3.setViewportView(list);
		
		textArea_1 = new JTextArea();
		textArea_1.setEditable(false);
		scrollPane_2.setViewportView(textArea_1);
		panel_2.setLayout(gl_panel_2);
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
		comboBoxAcquari.setMaximumRowCount(12);
		comboBoxAcquari.setModel(new DefaultComboBoxModel(new String[] {"SELEZIONA ACQUARIO", "1", "2", "3", "4", "5", "6", "7", "8"}));
		comboBoxAcquari.setToolTipText("Selezione acquario");
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
	    
	    comboBox = new JComboBox();
	    
	    comboBox_1 = new JComboBox();
	    
	    comboBox_2 = new JComboBox();
	    
	    comboBox_3 = new JComboBox();
	    
	    lblNewLabel_6 = new JLabel("New label");
	    
	    label = new JLabel("New label");
	    
	    lblNewLabel_7 = new JLabel("New label");
	    
	    lblNewLabel_8 = new JLabel("New label");
	    
	    btnNewButton = new JButton("New button");
	    
	    textField_4 = new JTextField();
	    textField_4.setColumns(10);
	    
	    scrollPane_4 = new JScrollPane();
	    
	    lblNewLabel_9 = new JLabel("New label");
	    GroupLayout gl_panelCerca = new GroupLayout(panelCerca);
	    gl_panelCerca.setHorizontalGroup(
	    	gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    		.addGroup(gl_panelCerca.createSequentialGroup()
	    			.addContainerGap()
	    			.addGroup(gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    				.addGroup(gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    					.addGroup(gl_panelCerca.createSequentialGroup()
	    						.addComponent(label)
	    						.addGap(104))
	    					.addGroup(gl_panelCerca.createSequentialGroup()
	    						.addComponent(lblNewLabel_6)
	    						.addPreferredGap(ComponentPlacement.RELATED))
	    					.addGroup(gl_panelCerca.createSequentialGroup()
	    						.addComponent(lblNewLabel_7)
	    						.addPreferredGap(ComponentPlacement.RELATED))
	    					.addGroup(gl_panelCerca.createSequentialGroup()
	    						.addComponent(lblNewLabel_8)
	    						.addPreferredGap(ComponentPlacement.RELATED))
	    					.addGroup(gl_panelCerca.createSequentialGroup()
	    						.addGroup(gl_panelCerca.createParallelGroup(Alignment.TRAILING, false)
	    							.addComponent(btnNewButton, Alignment.LEADING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
	    							.addComponent(comboBox_3, Alignment.LEADING, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
	    							.addComponent(comboBox_2, Alignment.LEADING, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
	    							.addComponent(comboBox_1, Alignment.LEADING, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
	    							.addComponent(comboBox, Alignment.LEADING, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
	    							.addComponent(textField_4, Alignment.LEADING, 166, 166, Short.MAX_VALUE))
	    						.addPreferredGap(ComponentPlacement.RELATED)))
	    				.addGroup(gl_panelCerca.createSequentialGroup()
	    					.addComponent(lblNewLabel_9)
	    					.addPreferredGap(ComponentPlacement.RELATED)))
	    			.addComponent(scrollPane_4, GroupLayout.DEFAULT_SIZE, 689, Short.MAX_VALUE)
	    			.addContainerGap())
	    );
	    gl_panelCerca.setVerticalGroup(
	    	gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    		.addGroup(gl_panelCerca.createSequentialGroup()
	    			.addGap(6)
	    			.addGroup(gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    				.addGroup(gl_panelCerca.createSequentialGroup()
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(textField_4, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblNewLabel_6)
	    					.addGap(11)
	    					.addComponent(comboBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addGap(4)
	    					.addComponent(label)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBox_1, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblNewLabel_7)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBox_2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblNewLabel_8)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBox_3, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblNewLabel_9)
	    					.addPreferredGap(ComponentPlacement.RELATED, 13, Short.MAX_VALUE)
	    					.addComponent(btnNewButton))
	    				.addComponent(scrollPane_4, Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 286, Short.MAX_VALUE))
	    			.addGap(26))
	    );
	    
	    list_12 = new JList();
	    scrollPane_4.setViewportView(list_12);
	    panelCerca.setLayout(gl_panelCerca);
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
	    panel.setToolTipText("Carrello piante");
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
	    gbl_panel_1.rowWeights = new double[]{1.0, Double.MIN_VALUE};
	    panel_1.setLayout(gbl_panel_1);
	    
	    chckbxNewCheckBox_1 = new JCheckBox("");
	    GridBagConstraints gbc_chckbxNewCheckBox_1 = new GridBagConstraints();
	    gbc_chckbxNewCheckBox_1.fill = GridBagConstraints.VERTICAL;
	    gbc_chckbxNewCheckBox_1.insets = new Insets(0, 0, 0, 5);
	    gbc_chckbxNewCheckBox_1.gridx = 0;
	    gbc_chckbxNewCheckBox_1.gridy = 0;
	    panel_1.add(chckbxNewCheckBox_1, gbc_chckbxNewCheckBox_1);
	    
	    JLabel lblNewLabel = new JLabel("Rotala rotundifollia var \"hraa\"");
	    lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
	    GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
	    gbc_lblNewLabel.insets = new Insets(0, 0, 0, 5);
	    gbc_lblNewLabel.gridx = 1;
	    gbc_lblNewLabel.gridy = 0;
	    panel_1.add(lblNewLabel, gbc_lblNewLabel);
	    
	    spinner = new JSpinner();
	    spinner.setModel(new SpinnerNumberModel(Integer.valueOf(1), Integer.valueOf(0), null, Integer.valueOf(1)));
	    GridBagConstraints gbc_spinner = new GridBagConstraints();
	    gbc_spinner.fill = GridBagConstraints.VERTICAL;
	    gbc_spinner.gridx = 2;
	    gbc_spinner.gridy = 0;
	    panel_1.add(spinner, gbc_spinner);
	    
	    btnAggiungiPiante = new JButton("Aggiungi Piante");
	    sl_panelSalva.putConstraint(SpringLayout.WEST, btnAggiungiPiante, 85, SpringLayout.EAST, scrollPane);
	    sl_panelSalva.putConstraint(SpringLayout.SOUTH, btnAggiungiPiante, -39, SpringLayout.SOUTH, panelSalva);
	    panelSalva.add(btnAggiungiPiante);
	    
	
	    
	 // Aggiungi un ActionListener ai bottoni per cambiare il pannello visualizzato
	    btnAcquari.addActionListener(e -> cardLayout.show(panelCardMain, "panelAcquari"));
	    btnCerca.addActionListener(e -> cardLayout.show(panelCardMain, "panelCerca"));
	    btnSalva.addActionListener(e -> cardLayout.show(panelCardMain, "panelSalva"));
	}
}
