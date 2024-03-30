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
import piante.TassoCrescitaType;

public class Window extends JFrame{

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
	private JButton btnSalvaNewAcquario;
	private JScrollPane scrollPaneNewDescrizione;
	private JTextArea textAreaNewDescrizione;
	private JTextField textFieldNewLitraggio;
	private JTextField textFieldNewLunghezza;
	private JTextField textFieldNewLarghezza;
	private JTextField textFieldNewAltezza;
	private JList listAcquari;
	private JLabel lblDescrizione;
	private JLabel lblNewLitraggio;
	private JLabel lblNewLunghezza;
	private JLabel lblNewLarghezza;
	private JLabel lblNewAltezza;
	private JComboBox comboBoxSalvaAcquari;
	private JScrollPane scrollPaneSalvaListaCarrello;
	private JPanel panelSalvaListaCarrello;
	private JCheckBox chckbxNewCheckBox;
	private JPanel panel_1;
	private JCheckBox chckbxNewCheckBox_1;
	private JSpinner spinner;
	private JButton btnSalvaAggiungiPiante;
	private JScrollPane scrollPaneView;
	private JPanel panelViewAcquario;
	private JTextField textFieldViewLitraggio;
	private JTextField textFieldViewLunghezza;
	private JTextField textFieldViewLarghezza;
	private JTextField textFieldViewAltezza;
	private JLabel lblViewLitraggio;
	private JLabel lblViewLunghezza;
	private JLabel lblViewLarghezza;
	private JLabel lblViewAltezza;
	private JScrollPane scrollPaneViewDescrizioneAcquario;
	private JTextArea textAreaViewDescrizioneAcquario;
	private JLabel lblViewDescrizione;
	private JScrollPane scrollPaneViewListaPianteAcquario;
	private JList listViewPianteAcquario;
	private JComboBox comboBoxCercaOrigine;
	private JComboBox comboBoxCercaTassoCrescita;
	private JComboBox comboBoxCercaLuce;
	private JComboBox comboBoxCercaCo2;
	private JLabel lblCercaNome;
	private JLabel lblCercaOrigine;
	private JLabel lblCercaTassoCrescita;
	private JLabel lblCercaLuce;
	private JButton btnCercaAggiungiPianta;
	private JTextField textFieldCercaNome;
	private JScrollPane scrollPaneCercaListaPiante;
	private JLabel lblCercaCo2;
	private JList listCercaPiante;
	private JComboBox comboBoxCercaDifficolta;
	private JLabel lblCercaDifficolta;
	private JButton btnCercaPianta;

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
		setBounds(100, 100, 956,530);
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
		CardLayout acquarioLayout= new CardLayout();
		panelCardAcquari.setLayout(acquarioLayout);
		
		panelNew = new JPanel();
		panelCardAcquari.add(panelNew, "panelNew");
		SpringLayout sl_panelNew = new SpringLayout();
		panelNew.setLayout(sl_panelNew);
		
		btnSalvaNewAcquario = new JButton("Salva Acquario");
		sl_panelNew.putConstraint(SpringLayout.SOUTH, btnSalvaNewAcquario, -10, SpringLayout.SOUTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, btnSalvaNewAcquario, -10, SpringLayout.EAST, panelNew);
		panelNew.add(btnSalvaNewAcquario);
		
		scrollPaneNewDescrizione = new JScrollPane();
		sl_panelNew.putConstraint(SpringLayout.WEST, scrollPaneNewDescrizione, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.SOUTH, scrollPaneNewDescrizione, -6, SpringLayout.NORTH, btnSalvaNewAcquario);
		sl_panelNew.putConstraint(SpringLayout.EAST, scrollPaneNewDescrizione, -10, SpringLayout.EAST, panelNew);
		panelNew.add(scrollPaneNewDescrizione);
		
		textAreaNewDescrizione = new JTextArea();
		scrollPaneNewDescrizione.setViewportView(textAreaNewDescrizione);
		
		textFieldNewLitraggio = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldNewLitraggio, 10, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldNewLitraggio, -153, SpringLayout.EAST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldNewLitraggio, 10, SpringLayout.WEST, panelNew);
		panelNew.add(textFieldNewLitraggio);
		textFieldNewLitraggio.setColumns(10);
		
		textFieldNewLunghezza = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.SOUTH, textFieldNewLitraggio, -17, SpringLayout.NORTH, textFieldNewLunghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldNewLunghezza, 0, SpringLayout.EAST, textFieldNewLitraggio);
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldNewLunghezza, 47, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldNewLunghezza, 10, SpringLayout.WEST, panelNew);
		textFieldNewLunghezza.setColumns(10);
		panelNew.add(textFieldNewLunghezza);
		
		textFieldNewLarghezza = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldNewLarghezza, 86, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldNewLarghezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldNewLarghezza, 0, SpringLayout.EAST, textFieldNewLitraggio);
		sl_panelNew.putConstraint(SpringLayout.SOUTH, textFieldNewLunghezza, -19, SpringLayout.NORTH, textFieldNewLarghezza);
		textFieldNewLarghezza.setColumns(10);
		panelNew.add(textFieldNewLarghezza);
		
		textFieldNewAltezza = new JTextField();
		sl_panelNew.putConstraint(SpringLayout.NORTH, scrollPaneNewDescrizione, 20, SpringLayout.SOUTH, textFieldNewAltezza);
		sl_panelNew.putConstraint(SpringLayout.NORTH, textFieldNewAltezza, 122, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.SOUTH, textFieldNewLarghezza, -16, SpringLayout.NORTH, textFieldNewAltezza);
		sl_panelNew.putConstraint(SpringLayout.WEST, textFieldNewAltezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, textFieldNewAltezza, 0, SpringLayout.EAST, textFieldNewLitraggio);
		textFieldNewAltezza.setColumns(10);
		panelNew.add(textFieldNewAltezza);
		
		lblDescrizione = new JLabel("Descrizione");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblDescrizione, 4, SpringLayout.NORTH, btnSalvaNewAcquario);
		sl_panelNew.putConstraint(SpringLayout.WEST, lblDescrizione, 10, SpringLayout.WEST, panelNew);
		panelNew.add(lblDescrizione);
		
		lblNewLitraggio = new JLabel("litraggio");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblNewLitraggio, 10, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblNewLitraggio, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblNewLitraggio);
		
		lblNewLunghezza = new JLabel("lunghezza");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblNewLunghezza, 23, SpringLayout.SOUTH, lblNewLitraggio);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblNewLunghezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblNewLunghezza);
		
		lblNewLarghezza = new JLabel("larghezza");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblNewLarghezza, 25, SpringLayout.SOUTH, lblNewLunghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblNewLarghezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblNewLarghezza);
		
		lblNewAltezza = new JLabel("altezza");
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblNewAltezza, 22, SpringLayout.SOUTH, lblNewLarghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblNewAltezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblNewAltezza);
		
		panelView = new JPanel();
		panelCardAcquari.add(panelView, "panelView");
		panelView.setLayout(new GridLayout(1, 0, 0, 0));
		
		scrollPaneView = new JScrollPane();
		scrollPaneView.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		panelView.add(scrollPaneView);
		
		panelViewAcquario = new JPanel();
		scrollPaneView.setViewportView(panelViewAcquario);
		
		textFieldViewLitraggio = new JTextField();
		textFieldViewLitraggio.setEditable(false);
		textFieldViewLitraggio.setColumns(10);
		
		textFieldViewLunghezza = new JTextField();
		textFieldViewLunghezza.setEditable(false);
		textFieldViewLunghezza.setColumns(10);
		
		textFieldViewLarghezza = new JTextField();
		textFieldViewLarghezza.setEditable(false);
		textFieldViewLarghezza.setColumns(10);
		
		textFieldViewAltezza = new JTextField();
		textFieldViewAltezza.setEditable(false);
		textFieldViewAltezza.setColumns(10);
		
		lblViewLitraggio = new JLabel("litraggio");
		
		lblViewLunghezza = new JLabel("lunghezza");
		
		lblViewLarghezza = new JLabel("larghezza");
		
		lblViewAltezza = new JLabel("altezza");
		
		scrollPaneViewDescrizioneAcquario = new JScrollPane();
		
		lblViewDescrizione = new JLabel("descrizione");
		
		scrollPaneViewListaPianteAcquario = new JScrollPane();
		
		listViewPianteAcquario = new JList();
		scrollPaneViewListaPianteAcquario.setViewportView(listViewPianteAcquario);
		
		textAreaViewDescrizioneAcquario = new JTextArea();
		textAreaViewDescrizioneAcquario.setEditable(false);
		scrollPaneViewDescrizioneAcquario.setViewportView(textAreaViewDescrizioneAcquario);
		GroupLayout gl_panelViewAcquario = new GroupLayout(panelViewAcquario);
		gl_panelViewAcquario.setHorizontalGroup(
			gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_panelViewAcquario.createSequentialGroup()
					.addGap(10)
					.addGroup(gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLitraggio, GroupLayout.PREFERRED_SIZE, 177, GroupLayout.PREFERRED_SIZE)
							.addGap(98)
							.addComponent(lblViewLitraggio))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLunghezza, GroupLayout.PREFERRED_SIZE, 177, GroupLayout.PREFERRED_SIZE)
							.addGap(88)
							.addComponent(lblViewLunghezza))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLarghezza, GroupLayout.PREFERRED_SIZE, 177, GroupLayout.PREFERRED_SIZE)
							.addGap(90)
							.addComponent(lblViewLarghezza))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewAltezza, GroupLayout.PREFERRED_SIZE, 177, GroupLayout.PREFERRED_SIZE)
							.addGap(102)
							.addComponent(lblViewAltezza))
						.addComponent(scrollPaneViewDescrizioneAcquario, GroupLayout.PREFERRED_SIZE, 313, GroupLayout.PREFERRED_SIZE)
						.addComponent(lblViewDescrizione)
						.addComponent(scrollPaneViewListaPianteAcquario, GroupLayout.PREFERRED_SIZE, 313, GroupLayout.PREFERRED_SIZE)))
		);
		gl_panelViewAcquario.setVerticalGroup(
			gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_panelViewAcquario.createSequentialGroup()
					.addGap(11)
					.addGroup(gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
						.addComponent(textFieldViewLitraggio, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addGap(3)
							.addComponent(lblViewLitraggio)))
					.addGap(18)
					.addGroup(gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
						.addComponent(textFieldViewLunghezza, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addGap(3)
							.addComponent(lblViewLunghezza)))
					.addGap(18)
					.addGroup(gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
						.addComponent(textFieldViewLarghezza, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addGap(3)
							.addComponent(lblViewLarghezza)))
					.addGap(18)
					.addGroup(gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
						.addComponent(textFieldViewAltezza, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addGap(3)
							.addComponent(lblViewAltezza)))
					.addGap(11)
					.addComponent(scrollPaneViewDescrizioneAcquario, GroupLayout.PREFERRED_SIZE, 93, GroupLayout.PREFERRED_SIZE)
					.addGap(6)
					.addComponent(lblViewDescrizione)
					.addGap(6)
					.addComponent(scrollPaneViewListaPianteAcquario, GroupLayout.PREFERRED_SIZE, 189, GroupLayout.PREFERRED_SIZE))
		);
		panelViewAcquario.setLayout(gl_panelViewAcquario);
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
		
		comboBoxSalvaAcquari = new JComboBox();
		comboBoxSalvaAcquari.setMaximumRowCount(12);
		comboBoxSalvaAcquari.setModel(new DefaultComboBoxModel(new String[] {"SELEZIONA ACQUARIO", "1", "2", "3", "4", "5", "6", "7", "8"}));
		comboBoxSalvaAcquari.setToolTipText("Selezione acquario");
		sl_panelSalva.putConstraint(SpringLayout.EAST, comboBoxSalvaAcquari, -41, SpringLayout.EAST, panelSalva);
		panelSalva.add(comboBoxSalvaAcquari);
		
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
	    
	    comboBoxCercaOrigine = new JComboBox();
	    comboBoxCercaOrigine.setModel(new DefaultComboBoxModel(new String[] {"Qualsiasi", "Cosmopolitan", "Cultivar", "South America", "Africa", "North America", "Asia", "Europe/Asia", "Australia"}));
	    
	    comboBoxCercaTassoCrescita = new JComboBox();
	    comboBoxCercaTassoCrescita.setModel(new DefaultComboBoxModel(new String[] {"Qualsiasi", "Lento", "Medio", "Veloce"}));
	    
	    comboBoxCercaLuce = new JComboBox();
	    comboBoxCercaLuce.setModel(new DefaultComboBoxModel(new String[] {"Qualsiasi", "Poca", "Media", "Tanta"}));
	    
	    comboBoxCercaCo2 = new JComboBox();
	    comboBoxCercaCo2.setModel(new DefaultComboBoxModel(new String[] {"Qualsiasi", "Poca", "Media", "Tanta"}));
	    
	    lblCercaNome = new JLabel("nome");
	    
	    lblCercaOrigine = new JLabel("origine");
	    
	    lblCercaTassoCrescita = new JLabel("tasso crescita");
	    
	    lblCercaLuce = new JLabel("luce");
	    
	    btnCercaAggiungiPianta = new JButton("Aggiungi Piante");
	    
	    textFieldCercaNome = new JTextField();
	    textFieldCercaNome.setColumns(10);
	    
	    scrollPaneCercaListaPiante = new JScrollPane();
	    
	    lblCercaCo2 = new JLabel("co2");
	    
	    comboBoxCercaDifficolta = new JComboBox();
	    comboBoxCercaDifficolta.setModel(new DefaultComboBoxModel(new String[] {"Qualsiasi", "Easy", "Medium", "Hard"}));
	    
	    lblCercaDifficolta = new JLabel("difficoltà");
	    
	    btnCercaPianta = new JButton("Cerca Pianta");
	    GroupLayout gl_panelCerca = new GroupLayout(panelCerca);
	    gl_panelCerca.setHorizontalGroup(
	    	gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    		.addGroup(gl_panelCerca.createSequentialGroup()
	    			.addContainerGap()
	    			.addGroup(gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    				.addGroup(gl_panelCerca.createSequentialGroup()
	    					.addComponent(lblCercaOrigine)
	    					.addGap(104))
	    				.addComponent(lblCercaNome)
	    				.addComponent(lblCercaTassoCrescita)
	    				.addComponent(lblCercaLuce)
	    				.addComponent(comboBoxCercaCo2, 0, 176, Short.MAX_VALUE)
	    				.addComponent(comboBoxCercaLuce, 0, 176, Short.MAX_VALUE)
	    				.addComponent(comboBoxCercaTassoCrescita, 0, 176, Short.MAX_VALUE)
	    				.addComponent(comboBoxCercaOrigine, 0, 176, Short.MAX_VALUE)
	    				.addComponent(textFieldCercaNome, 166, 176, Short.MAX_VALUE)
	    				.addComponent(comboBoxCercaDifficolta, Alignment.TRAILING, 0, 176, Short.MAX_VALUE)
	    				.addComponent(lblCercaCo2)
	    				.addComponent(lblCercaDifficolta)
	    				.addGroup(gl_panelCerca.createSequentialGroup()
	    					.addComponent(btnCercaPianta, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(btnCercaAggiungiPianta, GroupLayout.DEFAULT_SIZE, 109, Short.MAX_VALUE)))
	    			.addPreferredGap(ComponentPlacement.RELATED)
	    			.addComponent(scrollPaneCercaListaPiante, GroupLayout.DEFAULT_SIZE, 705, Short.MAX_VALUE)
	    			.addContainerGap())
	    );
	    gl_panelCerca.setVerticalGroup(
	    	gl_panelCerca.createParallelGroup(Alignment.TRAILING)
	    		.addGroup(Alignment.LEADING, gl_panelCerca.createSequentialGroup()
	    			.addGap(6)
	    			.addGroup(gl_panelCerca.createParallelGroup(Alignment.LEADING)
	    				.addComponent(scrollPaneCercaListaPiante, GroupLayout.DEFAULT_SIZE, 334, Short.MAX_VALUE)
	    				.addGroup(gl_panelCerca.createSequentialGroup()
	    					.addComponent(textFieldCercaNome, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblCercaNome)
	    					.addGap(11)
	    					.addComponent(comboBoxCercaOrigine, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addGap(4)
	    					.addComponent(lblCercaOrigine)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBoxCercaTassoCrescita, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblCercaTassoCrescita)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBoxCercaLuce, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblCercaLuce)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBoxCercaCo2, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblCercaCo2)
	    					.addPreferredGap(ComponentPlacement.UNRELATED)
	    					.addComponent(comboBoxCercaDifficolta, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
	    					.addPreferredGap(ComponentPlacement.RELATED)
	    					.addComponent(lblCercaDifficolta)
	    					.addPreferredGap(ComponentPlacement.RELATED, 69, Short.MAX_VALUE)
	    					.addGroup(gl_panelCerca.createParallelGroup(Alignment.BASELINE)
	    						.addComponent(btnCercaAggiungiPianta)
	    						.addComponent(btnCercaPianta))))
	    			.addContainerGap())
	    );
	    
	    listCercaPiante = new JList();
	    scrollPaneCercaListaPiante.setViewportView(listCercaPiante);
	    panelCerca.setLayout(gl_panelCerca);
	    panelCardMain.add(panelSalva, "panelSalva");
	    
	    scrollPaneSalvaListaCarrello = new JScrollPane();
	    sl_panelSalva.putConstraint(SpringLayout.NORTH, comboBoxSalvaAcquari, 0, SpringLayout.NORTH, scrollPaneSalvaListaCarrello);
	    sl_panelSalva.putConstraint(SpringLayout.WEST, comboBoxSalvaAcquari, 22, SpringLayout.EAST, scrollPaneSalvaListaCarrello);
	    sl_panelSalva.putConstraint(SpringLayout.NORTH, scrollPaneSalvaListaCarrello, 10, SpringLayout.NORTH, panelSalva);
	    sl_panelSalva.putConstraint(SpringLayout.SOUTH, scrollPaneSalvaListaCarrello, -10, SpringLayout.SOUTH, panelSalva);
	    sl_panelSalva.putConstraint(SpringLayout.EAST, scrollPaneSalvaListaCarrello, -286, SpringLayout.EAST, panelSalva);
	    sl_panelSalva.putConstraint(SpringLayout.WEST, scrollPaneSalvaListaCarrello, 10, SpringLayout.WEST, panelSalva);
	    panelSalva.add(scrollPaneSalvaListaCarrello);
	    
	    panelSalvaListaCarrello = new JPanel();
	    panelSalvaListaCarrello.setToolTipText("Carrello piante");
	    scrollPaneSalvaListaCarrello.setViewportView(panelSalvaListaCarrello);
	    GridLayout gl_panelSalvaListaCarrello= new GridLayout(30, 1, 0, 0);
	    panelSalvaListaCarrello.setLayout(gl_panelSalvaListaCarrello);
	    panelSalvaListaCarrello.setLayout(gl_panelSalvaListaCarrello);
	
	    panel_1 = new JPanel();
	    MatteBorder borderPanelSalvaListaPiante = new MatteBorder(1, 1, 1, 1, (Color) new Color(0, 0, 0));
	    panel_1.setBorder(borderPanelSalvaListaPiante);
	    panelSalvaListaCarrello.add(panel_1);
	    GridBagLayout gbl_panel_1 = new GridBagLayout();
	    gbl_panel_1.columnWidths = new int[]{0, 0, 0, 0};
	    gbl_panel_1.rowHeights = new int[]{0, 0};
	    gbl_panel_1.columnWeights = new double[]{0.0, 1.0, 0.0, Double.MIN_VALUE};
	    gbl_panel_1.rowWeights = new double[]{1.0, Double.MIN_VALUE};
	    panel_1.setLayout(gbl_panel_1);
	    
	    JPanel panel_2= new JPanel();
	    panel_2.setBorder(borderPanelSalvaListaPiante);
	    panelSalvaListaCarrello.add(panel_2);
	    GridBagLayout gb2 = gbl_panel_1;
	 
	    
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
	    
	    btnSalvaAggiungiPiante = new JButton("Aggiungi Piante");
	    sl_panelSalva.putConstraint(SpringLayout.WEST, btnSalvaAggiungiPiante, 85, SpringLayout.EAST, scrollPaneSalvaListaCarrello);
	    sl_panelSalva.putConstraint(SpringLayout.SOUTH, btnSalvaAggiungiPiante, -39, SpringLayout.SOUTH, panelSalva);
	    panelSalva.add(btnSalvaAggiungiPiante);
	    
	
	    
	 // Aggiungi un ActionListener ai bottoni per cambiare il pannello visualizzato
	    btnAcquari.addActionListener(e -> cardLayout.show(panelCardMain, "panelAcquari"));
	    btnCerca.addActionListener(e -> cardLayout.show(panelCardMain, "panelCerca"));
	    btnSalva.addActionListener(e -> cardLayout.show(panelCardMain, "panelSalva"));
	    btnNew.addActionListener(e -> acquarioLayout.show(panelCardAcquari, "panelNew"));
	    btnView.addActionListener(e -> acquarioLayout.show(panelCardAcquari, "panelView"));
	}
}
