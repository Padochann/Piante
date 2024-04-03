package view;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.SpringLayout;
import java.awt.CardLayout;
import java.awt.Checkbox;

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
import javax.swing.JOptionPane;
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
import java.awt.Point;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import javax.swing.DefaultComboBoxModel;
import javax.swing.DefaultListModel;
import javax.swing.border.MatteBorder;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.awt.Color;
import javax.swing.SpinnerNumberModel;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.forms.layout.ColumnSpec;
import com.jgoodies.forms.layout.RowSpec;

import control.Controller;

import com.jgoodies.forms.layout.FormSpecs;
import net.miginfocom.swing.MigLayout;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.LayoutStyle.ComponentPlacement;

import piante.AcquarioType;
import piante.PiantaType;
import piante.TassoCrescitaType;
import javax.swing.ListSelectionModel;

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
	private JButton btnSalvaNewAcquario;
	private JScrollPane scrollPaneNewDescrizione;
	private JTextArea textAreaNewDescrizione;
	private JTextField textFieldNewLitraggio;
	private JTextField textFieldNewLunghezza;
	private JTextField textFieldNewLarghezza;
	private JTextField textFieldNewAltezza;
	private JList<String> listAcquari;
	private JLabel lblDescrizione;
	private JLabel lblNewLitraggio;
	private JLabel lblNewLunghezza;
	private JLabel lblNewLarghezza;
	private JLabel lblNewAltezza;
	private JComboBox<String> comboBoxSalvaAcquari;
	private JScrollPane scrollPaneSalvaListaCarrello;
	private JPanel panelSalvaListaCarrello;
	//private JCheckBox chckbxNewCheckBox;
	//private JPanel panel_1;
	//private JCheckBox chckbxNewCheckBox_1;
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
	private JList<String> listViewPianteAcquario;
	private JComboBox<String> comboBoxCercaOrigine;
	private JComboBox<String> comboBoxCercaTassoCrescita;
	private JComboBox<String> comboBoxCercaLuce;
	private JComboBox<String> comboBoxCercaCo2;
	private JLabel lblCercaNome;
	private JLabel lblCercaOrigine;
	private JLabel lblCercaTassoCrescita;
	private JLabel lblCercaLuce;
	private JButton btnCercaAggiungiPianta;
	private JTextField textFieldCercaNome;
	private JScrollPane scrollPaneCercaListaPiante;
	private JLabel lblCercaCo2;
	private JList<String> listCercaPiante;
	private JComboBox<String> comboBoxCercaDifficolta;
	private JLabel lblCercaDifficolta;
	private JButton btnCercaPianta;
	private CardLayout cardLayout;
	private CardLayout acquarioLayout;
	private List<JPanel> arrayPanelsListaCarrello = new ArrayList<JPanel>();
	//private List<JCheckBox> arrayChckBxListaCarrello = new ArrayList<JCheckBox>();
	//private List<JSpinner> arraySpinListaCarrello = new ArrayList<JSpinner>();
	private List<PiantaType> arrayListaCarrello = new ArrayList<PiantaType>();
	private List<PiantaType> arrayListCercaPiante = new ArrayList<PiantaType>();
	private List<AcquarioType> arrayListAcquari = new ArrayList<AcquarioType>();
	private List<PiantaType> arrayListViewPianteForAcquario = new ArrayList<PiantaType>();
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Window frame = new Window();
					frame.setVisible(true);
					Controller controller = new Controller(frame);
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
		setBounds(100, 100, 978,530);
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
		cardLayout = new CardLayout();
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
		
		listAcquari = new JList<String>();
		listAcquari.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		listAcquari.setModel(new DefaultListModel<String>() {
	        /**
	         * 
	         */
	    		
	        private static final long serialVersionUID = 1L;
	        @Override
            public int getSize() {
                return arrayListAcquari.size();
            }

            @Override
            public String getElementAt(int index) {
                return Long.toString(arrayListAcquari.get(index).getIdAcquario())+")   litri:"+Long.toString(arrayListAcquari.get(index).getLitri());
            }

			@Override
			public void fireIntervalAdded(Object source, int index0, int index1) {
				// TODO Auto-generated method stub
				super.fireIntervalAdded(source, index0, index1);
			}

            
	        
	        
	    });
		scrollPaneAcquari.setViewportView(listAcquari);
		acquarioLayout= new CardLayout();
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
		
		listViewPianteAcquario = new JList<String>();
		listViewPianteAcquario.setModel(new DefaultListModel<String>() {
	        /**
	         * 
	         */
	    		
	        private static final long serialVersionUID = 1L;
	        @Override
            public int getSize() {
                return arrayListViewPianteForAcquario.size();
            }

            @Override
            public String getElementAt(int index) {
                return arrayListViewPianteForAcquario.get(index).getNome();
            }

			@Override
			public void fireIntervalAdded(Object source, int index0, int index1) {
				// TODO Auto-generated method stub
				super.fireIntervalAdded(source, index0, index1);
			}

            
	        
	        
	    });
		listViewPianteAcquario.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
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
							.addComponent(textFieldViewLitraggio, GroupLayout.DEFAULT_SIZE, 177, Short.MAX_VALUE)
							.addGap(98)
							.addComponent(lblViewLitraggio))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLunghezza, GroupLayout.DEFAULT_SIZE, 177, Short.MAX_VALUE)
							.addGap(88)
							.addComponent(lblViewLunghezza))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLarghezza, GroupLayout.DEFAULT_SIZE, 177, Short.MAX_VALUE)
							.addGap(90)
							.addComponent(lblViewLarghezza))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewAltezza, GroupLayout.DEFAULT_SIZE, 177, Short.MAX_VALUE)
							.addGap(102)
							.addComponent(lblViewAltezza))
						.addComponent(scrollPaneViewDescrizioneAcquario, GroupLayout.DEFAULT_SIZE, 313, Short.MAX_VALUE)
						.addComponent(lblViewDescrizione)
						.addComponent(scrollPaneViewListaPianteAcquario, GroupLayout.DEFAULT_SIZE, 313, Short.MAX_VALUE))
					.addGap(8))
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
					.addComponent(scrollPaneViewListaPianteAcquario, GroupLayout.DEFAULT_SIZE, 189, Short.MAX_VALUE))
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
		
		comboBoxSalvaAcquari = new JComboBox<String>();
		comboBoxSalvaAcquari.setModel(new DefaultComboBoxModel<String>() {
	        /**
	         * 
	         */
	    		
	        private static final long serialVersionUID = 1L;
	        @Override
            public int getSize() {
                return arrayListAcquari.size();
            }

            @Override
            public String getElementAt(int index) {
                return Long.toString(arrayListAcquari.get(index).getIdAcquario())+")   litri:"+Long.toString(arrayListAcquari.get(index).getLitri());
            }

			@Override
			public void fireIntervalAdded(Object source, int index0, int index1) {
				// TODO Auto-generated method stub
				super.fireIntervalAdded(source, index0, index1);
			}

            
	        
	        
	    });
		comboBoxSalvaAcquari.setMaximumRowCount(12);
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
	    
	    comboBoxCercaOrigine = new JComboBox<String>();
	    comboBoxCercaOrigine.setModel(new DefaultComboBoxModel<String>(new String[] {"Qualsiasi", "Cosmopolitan", "Cultivar", "South America", "Africa", "North America", "Asia", "Europe/Asia", "Australia"}));
	    
	    comboBoxCercaTassoCrescita = new JComboBox<String>();
	    comboBoxCercaTassoCrescita.setModel(new DefaultComboBoxModel<String>(new String[] {"Qualsiasi", "Lento", "Medio", "Veloce"}));
	    
	    comboBoxCercaLuce = new JComboBox<String>();
	    comboBoxCercaLuce.setModel(new DefaultComboBoxModel<String>(new String[] {"Qualsiasi", "Poca", "Media", "Tanta"}));
	    
	    comboBoxCercaCo2 = new JComboBox<String>();
	    comboBoxCercaCo2.setModel(new DefaultComboBoxModel<String>(new String[] {"Qualsiasi", "Poca", "Media", "Tanta"}));
	    
	    lblCercaNome = new JLabel("nome");
	    
	    lblCercaOrigine = new JLabel("origine");
	    
	    lblCercaTassoCrescita = new JLabel("tasso crescita");
	    
	    lblCercaLuce = new JLabel("luce");
	    
	    btnCercaAggiungiPianta = new JButton("Aggiungi Piante");
	    
	    textFieldCercaNome = new JTextField();
	    textFieldCercaNome.setColumns(10);
	    
	    scrollPaneCercaListaPiante = new JScrollPane();
	    
	    lblCercaCo2 = new JLabel("co2");
	    
	    comboBoxCercaDifficolta = new JComboBox<String>();
	    comboBoxCercaDifficolta.setModel(new DefaultComboBoxModel<String>(new String[] {"Qualsiasi", "Easy", "Medium", "Advanced"}));
	    
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
	    
	    listCercaPiante = new JList<String>();
	    listCercaPiante.setVisibleRowCount(1000);
	    listCercaPiante.setModel(new DefaultListModel<String>() {
	        /**
	         * 
	         */
	    		
	        private static final long serialVersionUID = 1L;
	        @Override
            public int getSize() {
                return arrayListCercaPiante.size();
            }

            @Override
            public String getElementAt(int index) {
                return arrayListCercaPiante.get(index).getNome();
            }

			@Override
			public void fireIntervalAdded(Object source, int index0, int index1) {
				// TODO Auto-generated method stub
				super.fireIntervalAdded(source, index0, index1);
			}

            
	        
	        
	    });


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
	    GridLayout gl_panelSalvaListaCarrello= new GridLayout(39, 1, 0, 0);
	    panelSalvaListaCarrello.setLayout(gl_panelSalvaListaCarrello);
	    
	    //((GridLayout)panelSalvaListaCarrello.getLayout()).setRows(((GridLayout)panelSalvaListaCarrello.getLayout()).getRows()+30);
	
	    /*panel_1 = new JPanel();
	    MatteBorder borderPanelSalvaListaPiante = new MatteBorder(1, 1, 1, 1, (Color) new Color(0, 0, 0));
	    panel_1.setBorder(borderPanelSalvaListaPiante);
	    panelSalvaListaCarrello.add(panel_1);
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
	    panel_1.add(spinner, gbc_spinner);*/
	    
	    btnSalvaAggiungiPiante = new JButton("Aggiungi Piante");
	    sl_panelSalva.putConstraint(SpringLayout.WEST, btnSalvaAggiungiPiante, 85, SpringLayout.EAST, scrollPaneSalvaListaCarrello);
	    sl_panelSalva.putConstraint(SpringLayout.SOUTH, btnSalvaAggiungiPiante, -39, SpringLayout.SOUTH, panelSalva);
	    panelSalva.add(btnSalvaAggiungiPiante);
	    
	
	    
	 /*Aggiungi un ActionListener ai bottoni per cambiare il pannello visualizzato
	    btnAcquari.addActionListener(e -> cardLayout.show(panelCardMain, "panelAcquari"));
	    btnCerca.addActionListener(e -> cardLayout.show(panelCardMain, "panelCerca"));
	    btnSalva.addActionListener(e -> cardLayout.show(panelCardMain, "panelSalva"));
	    btnNew.addActionListener(e -> acquarioLayout.show(panelCardAcquari, "panelNew"));
	    btnView.addActionListener(e -> acquarioLayout.show(panelCardAcquari, "panelView"));*/
	    
	    
	    
	}
	
	

	/**
	 * @return the btnNew
	 */
	public JButton getBtnNew() {
		return btnNew;
	}

	/**
	 * @return the btnView
	 */
	public JButton getBtnView() {
		return btnView;
	}

	/**
	 * @return the btnDelete
	 */
	public JButton getBtnDelete() {
		return btnDelete;
	}

	/**
	 * @return the btnAcquari
	 */
	public JButton getBtnAcquari() {
		return btnAcquari;
	}

	/**
	 * @return the btnCerca
	 */
	public JButton getBtnCerca() {
		return btnCerca;
	}

	/**
	 * @return the btnSalva
	 */
	public JButton getBtnSalva() {
		return btnSalva;
	}

	/**
	 * @return the btnSalvaNewAcquario
	 */
	public JButton getBtnSalvaNewAcquario() {
		return btnSalvaNewAcquario;
	}

	/**
	 * @return the spinner
	 */
	public JSpinner getSpinner() {
		return spinner;
	}

	/**
	 * @return the btnSalvaAggiungiPiante
	 */
	public JButton getBtnSalvaAggiungiPiante() {
		return btnSalvaAggiungiPiante;
	}

	/**
	 * @return the btnCercaAggiungiPianta
	 */
	public JButton getBtnCercaAggiungiPianta() {
		return btnCercaAggiungiPianta;
	}

	/**
	 * @return the btnCercaPianta
	 */
	public JButton getBtnCercaPianta() {
		return btnCercaPianta;
	}
	
	
	
	/**
	 * @return the listAcquari
	 */
	public JList<String> getListAcquari() {
		return listAcquari;
	}

	/**
	 * @return the listViewPianteAcquario
	 */
	public JList<String> getListViewPianteAcquario() {
		return listViewPianteAcquario;
	}

	/**
	 * @return the listCercaPiante
	 */
	public JList<String> getListCercaPiante() {
		return listCercaPiante;
	}

	public String getTxtCercaNome() {
		if(textFieldCercaNome.getText().equals(""))
			return null;
		return textFieldCercaNome.getText();
	}
	
	public String getItemComboBoxCercaOrigine() {
		if(comboBoxCercaOrigine.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaOrigine.getSelectedItem().toString();
	}
	
	public String getItemComboBoxCercaTassoCrescita() {
		if(comboBoxCercaTassoCrescita.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaTassoCrescita.getSelectedItem().toString();
	}
	
	public String getItemComboBoxCercaLuce() {
		if(comboBoxCercaLuce.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaLuce.getSelectedItem().toString();
	}
	
	public String getItemComboBoxCercaCo2() {
		if(comboBoxCercaCo2.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaCo2.getSelectedItem().toString();
	}
	
	public String getItemComboBoxCercaDifficolta() {
		if(comboBoxCercaDifficolta.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaDifficolta.getSelectedItem().toString();
	}
	
	
	
	/**
	 * Retrieves a list of strings of the selected items in the JList used for searching plants.
	 * 
	 * @return a list containing the strings of the selected items
	 */
	public List<PiantaType> getSelectedItemsListCercaPiante() {
	    List<PiantaType> selectedItems = new ArrayList<>();
	    int[] selectedIndices = listCercaPiante.getSelectedIndices();
	    
	    // Ordina gli indici in ordine decrescente
	    Arrays.sort(selectedIndices);
	    for (int i = selectedIndices.length - 1; i >= 0; i--) {
	        int index = selectedIndices[i];
	        selectedItems.add(arrayListCercaPiante.get(index));
	        
	        // Rimuovi l'elemento dalla lista
	        arrayListCercaPiante.remove(index);
	        
	        // Rimuovi l'elemento dal modello della JList
	        DefaultListModel<String> model = (DefaultListModel<String>) listCercaPiante.getModel();
	        model.remove(index);
	    }
	    
	    return selectedItems;
	}

	
    /**
     * Adds a list of PiantaType items to the existing list of PiantaType items.
     * After adding the new items to the ArrayList, this method updates the JList model 
     * to reflect the changes by adding the names of the newly added items to the model.
     *
     * @param itemsToAdd A List of PiantaType items to be added to the existing list.
     */
    public void addItemsToListCercaPiante(List<PiantaType> itemsToAdd) {
        int startIndex = arrayListCercaPiante.size();

        arrayListCercaPiante.addAll(itemsToAdd);

        int endIndex = arrayListCercaPiante.size() - 1;

        // Aggiorna direttamente il modello della JList
        DefaultListModel<String> model = (DefaultListModel<String>) listCercaPiante.getModel();
        for (int i = startIndex; i <= endIndex; i++) {
            model.addElement(arrayListCercaPiante.get(i).getNome());
        }
    }
    
    /**
     * Removes all items from both the ArrayList and the DefaultListModel associated with the JList.
     * This method clears all the items from the ArrayList and updates the JList model to reflect the changes.
     */
    public void removeAllItemsFromListCercaPiante() {
        arrayListCercaPiante.clear(); // Rimuove tutti gli elementi dall'ArrayList
        DefaultListModel<String> model = (DefaultListModel<String>) listCercaPiante.getModel();
        model.removeAllElements(); // Rimuove tutti gli elementi dal DefaultListModel
    }
    
    /**
     * Adds items to the list of carrello piante and updates the display.
     * 
     * @param itemsToAdd the list of items to add PiantaType
     */
    public void addItemsToListaCarrello(List<PiantaType> itemsToAdd) {
    	
    	for(PiantaType plant : itemsToAdd) {
    		JPanel panelToAdd = this.createPanelWithComponentsForListaCarrello(plant);
    		arrayPanelsListaCarrello.add(panelToAdd);
    		arrayListaCarrello.add(plant);
    	}
    	
    	for(JPanel panel : arrayPanelsListaCarrello) {
    		panelSalvaListaCarrello.add(panel);
    		
    	}
    	
    	 panelSalvaListaCarrello.setLayout(new GridLayout(arrayPanelsListaCarrello.size(), 1,0 ,0));  // Imposta un layout di griglia dinamico con una sola colonna
         panelSalvaListaCarrello.revalidate();
         panelSalvaListaCarrello.repaint();
    	
    }
    
    
    /**
     * Creates a JPanel with components for a specific PiantaType.
     * 
     * @param plant The PiantaType object for which the panel is created.
     * @return The JPanel with the components.
     */
    public JPanel createPanelWithComponentsForListaCarrello(PiantaType plant) {
		
    	JPanel panel_1 = new JPanel();
	    MatteBorder borderPanelSalvaListaPiante = new MatteBorder(1, 1, 1, 1, (Color) new Color(0, 0, 0));
	    panel_1.setBorder(borderPanelSalvaListaPiante);
	    panel_1.setName(Long.toString(plant.getIdPianta()));
	    GridBagLayout gbl_panel_1 = new GridBagLayout();
	    gbl_panel_1.columnWidths = new int[]{0, 0, 0, 0};
	    gbl_panel_1.rowHeights = new int[]{0, 0};
	    gbl_panel_1.columnWeights = new double[]{0.0, 1.0, 0.0, Double.MIN_VALUE};
	    gbl_panel_1.rowWeights = new double[]{1.0, Double.MIN_VALUE};
	    panel_1.setLayout(gbl_panel_1);
	    
	    
	    
	    
	    JCheckBox chckbxNewCheckBox_1 = new JCheckBox("");
	    chckbxNewCheckBox_1.setName(Long.toString(plant.getIdPianta()));
	    GridBagConstraints gbc_chckbxNewCheckBox_1 = new GridBagConstraints();
	    gbc_chckbxNewCheckBox_1.fill = GridBagConstraints.VERTICAL;
	    gbc_chckbxNewCheckBox_1.insets = new Insets(0, 0, 0, 5);
	    gbc_chckbxNewCheckBox_1.gridx = 0;
	    gbc_chckbxNewCheckBox_1.gridy = 0;
	    panel_1.add(chckbxNewCheckBox_1, gbc_chckbxNewCheckBox_1);
	    
	    
	    
	    JLabel lblNewLabel = new JLabel(plant.getNome());
	    lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
	    lblNewLabel.setName(Long.toString(plant.getIdPianta()));
	    GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
	    gbc_lblNewLabel.insets = new Insets(0, 0, 0, 5);
	    gbc_lblNewLabel.gridx = 1;
	    gbc_lblNewLabel.gridy = 0;
	    panel_1.add(lblNewLabel, gbc_lblNewLabel);
	    
	    JSpinner spinner = new JSpinner();
	    spinner.setModel(new SpinnerNumberModel(Integer.valueOf(1), Integer.valueOf(0), null, Integer.valueOf(1)));      
	    spinner.setName(Long.toString(plant.getIdPianta()));
	    GridBagConstraints gbc_spinner = new GridBagConstraints();
	    gbc_spinner.fill = GridBagConstraints.VERTICAL;
	    gbc_spinner.gridx = 2;
	    gbc_spinner.gridy = 0;
	    panel_1.add(spinner, gbc_spinner);
	    
	    spinner.addChangeListener(new ChangeListener() {
	        @Override
	        public void stateChanged(ChangeEvent e) {
	            JSpinner source = (JSpinner) e.getSource();
	            int value = (int) source.getValue();

	            if (value == 0) {
	                // Ottieni il pannello padre dello spinner
	                JPanel parentPanel = (JPanel) spinner.getParent();

	                // Rimuovi il pannello dalla tabella
	                parentPanel.removeAll();
	                parentPanel.revalidate();
	                parentPanel.repaint();

	                // Rimuovi il pannello dalla lista
	                Iterator<JPanel> iterator = arrayPanelsListaCarrello.iterator();
	                int index=0;
	                while (iterator.hasNext()) {
	                    JPanel currentPanel = iterator.next();
	                    if (currentPanel == parentPanel) {
	                        iterator.remove();
	                        arrayListaCarrello.remove(index);
	                        
	                        break;
	                    }
	                    index++;
	                }
	                
	                // Rimuovi tutti i componenti dal frame
	                //JFrame frame = (JFrame) SwingUtilities.getWindowAncestor(parentPanel);
	                //frame.getContentPane().removeAll();
	                
	                panelSalvaListaCarrello.removeAll();
	                
	                // Aggiungi tutti i pannelli aggiornati al frame
	                for (JPanel panel : arrayPanelsListaCarrello) {
	                    panelSalvaListaCarrello.add(panel);
	                }

	                // Aggiorna il layout del frame
	                panelSalvaListaCarrello.setLayout(new GridLayout(arrayPanelsListaCarrello.size(), 1,0,0));  // Imposta un layout di griglia dinamico con una sola colonna
	                panelSalvaListaCarrello.revalidate();
	                panelSalvaListaCarrello.repaint();
	                System.out.println(arrayPanelsListaCarrello.toString());
	                System.out.println(arrayListaCarrello.toString());
	            }
	        }

			
	    });

	    
    	return panel_1;
    	
    }

    /**
     * Updates the list of aquariums with the given items.
     *
     * @param itemsToUpdate The list of aquarium items to update.
     */
    public void updateListAcquari(List<AcquarioType> itemsToUpdate) {
        arrayListAcquari.clear();
        arrayListAcquari.addAll(itemsToUpdate);
        
        DefaultComboBoxModel<String> comboBoxModel = (DefaultComboBoxModel<String>) comboBoxSalvaAcquari.getModel();
        
        for (AcquarioType acquario : arrayListAcquari) {
            String itemText = Long.toString(acquario.getIdAcquario()) + ")   litri:" + Long.toString(acquario.getLitri());
            comboBoxModel.addElement(itemText);
        }
        
        comboBoxSalvaAcquari.setModel(comboBoxModel);
        
        // Aggiornamento della JList listAcquari
        DefaultListModel<String> listModel = (DefaultListModel<String>) listAcquari.getModel();
        for (AcquarioType acquario : arrayListAcquari) {
            String itemText = Long.toString(acquario.getIdAcquario()) + ")   litri:" + Long.toString(acquario.getLitri());
            listModel.addElement(itemText);
        }
        listAcquari.setModel(listModel);
    }

    public AcquarioType getSelectedItemListAcquari() throws Exception{

    	AcquarioType selectedItem;
	    int selectedIndex = listAcquari.getSelectedIndex();
	    if(selectedIndex == -1)
	    	throw new Exception("Attenzione: selezionare un acquario dalla lista per poterlo visualizzare");
	    
	    selectedItem = arrayListAcquari.get(selectedIndex);
	    
	    return selectedItem;
    }

    //aggiungere come parametro una lista di PiantaType filtrata per l'id dell'acquario selezionato
    //contr chiama getSelectedItemListAcquari prende la pk
    //fa la richiesta su piante_acquari id_acquario=pk
    //per ogni item del risultato prende la pk della pianta e fa una richiesta a piante e salva il singolo item ottenuto add in una lista di PiantaType che viene passata a questo metodo
    public void viewSelectedAcquario(List<PiantaType> plantsToView) throws Exception{
    	AcquarioType selectedItem = this.getSelectedItemListAcquari();
    	//listAcquari.clearSelection();
    	textFieldViewLitraggio.setText(Long.toString(selectedItem.getLitri()));
    	textFieldViewLarghezza.setText(Long.toString(selectedItem.getLarghezza()));
    	textFieldViewLunghezza.setText(Long.toString(selectedItem.getLunghezza()));
    	textFieldViewAltezza.setText(Long.toString(selectedItem.getAltezza()));
    	textAreaViewDescrizioneAcquario.setText(selectedItem.getDescrizione());
    	
    	arrayListViewPianteForAcquario.clear();
    	arrayListViewPianteForAcquario.addAll(plantsToView);
    	
    	this.updateViewListPianteForAcquario();
    }
    
    private void updateViewListPianteForAcquario() {
    	// Aggiornamento della JList listAcquari
        DefaultListModel<String> listModel = new DefaultListModel<String>();
        for (PiantaType pianta : arrayListViewPianteForAcquario) {
            
            listModel.addElement(pianta.getNome());
        }
        listViewPianteAcquario.setModel(listModel);
    }
    
    public void resetViewAndNew() {
    	textFieldViewLitraggio.setText(null);
    	textFieldViewLarghezza.setText(null);
    	textFieldViewLunghezza.setText(null);
    	textFieldViewAltezza.setText(null);
    	textAreaViewDescrizioneAcquario.setText(null);
    	
    	arrayListViewPianteForAcquario.clear();
    	this.updateViewListPianteForAcquario();
    	
    	textFieldNewLitraggio.setText(null);
    	textFieldNewLarghezza.setText(null);
    	textFieldNewLunghezza.setText(null);
    	textFieldNewAltezza.setText(null);
    	textAreaNewDescrizione.setText(null);
    }
    
	/**
	 * This method add to all buttons the reference of the class who manage the actions.
	 * @param c the reference of the class.
	 */
	public void registerEvent(Controller controller) {
		// TODO Auto-generated method stub
		btnAcquari.addActionListener(controller);
	    btnCerca.addActionListener(controller);
	    btnSalva.addActionListener(controller);
	    btnNew.addActionListener(controller);
	    btnView.addActionListener(controller);
	    
	    btnSalvaNewAcquario.addActionListener(controller);
	    btnDelete.addActionListener(controller);
	    
	    btnCercaPianta.addActionListener(controller);
	    btnCercaAggiungiPianta.addActionListener(controller);
	    
	    //spinner.addChangeListener(controller);//devo mettere questo nel metodo crea panel with components
	    btnSalvaAggiungiPiante.addActionListener(controller);
	    
	    listCercaPiante.addMouseListener(controller);
	    listViewPianteAcquario.addMouseListener(controller);
	    
	    listCercaPiante.addKeyListener(controller);
	    listAcquari.addKeyListener(controller);
	    listViewPianteAcquario.addKeyListener(controller);
	    
	    
	}
	
	/**
	 * Displays the specified panel within the given layout.
	 *
	 * @param layoutName The name of the layout to use ("cardLayout" or "acquarioLayout").
	 * @param panelName The name of the panel to display within the specified layout.
	 *
	 * @throws IllegalArgumentException if the provided layout name is neither "cardLayout" nor "acquarioLayout".
	 */
	public void showPanel(String layoutName, String panelName) throws Exception {
	    switch (layoutName) {
	        case "cardLayout":
	            this.cardLayout.show(panelCardMain, panelName);
	            break;
	        case "acquarioLayout":
	            this.acquarioLayout.show(panelCardAcquari, panelName);
	            break;
	        default:
	            throw new IllegalArgumentException("Layout non valido: " + layoutName);
	    }
	}


	/**
	 * This method create a message dialog.
	 * @param message the string that will be shown.
	 */
	public void messageDialog(String message) {
		JOptionPane.showMessageDialog(this, message);
		System.out.println(message);
	}
	
	/**
	 * Returns the index of the element in the listCercaPiante that corresponds to the given mouse click point.
	 *
	 * @param p the mouse click point
	 * @return the index of the element in the listCercaPiante, or -1 if no element is found
	 */
	public int getIndexOfElemenListCercaPiantaForMouseClick(Point p) {
		return listCercaPiante.locationToIndex(p);
	}
	
	/**
	 * Returns the index of the element in the listViewPianteAcquario that corresponds to the given mouse click point.
	 *
	 * @param p the mouse click point
	 * @return the index of the element in the listViewPianteAcquario, or -1 if no element is found
	 */
	public int getIndexOfElemenListViewPianteAcquarioForMouseClick(Point p) {
		return listViewPianteAcquario.locationToIndex(p);
	}
	
	public void clearSelectionListAcquari() {
		listAcquari.clearSelection();
	}
	
	public void clearSelectionListCercaPiante() {
		listCercaPiante.clearSelection();
	}
	
	public void clearSelectionListViewPianteAcquario() {
		listViewPianteAcquario.clearSelection();
	}
	
	
}
