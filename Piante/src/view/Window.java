package view;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.SpringLayout;

import java.awt.BorderLayout;
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
import javax.swing.UIManager;
import javax.swing.BoxLayout;
import java.awt.Component;
import java.awt.Desktop;

import javax.swing.ScrollPaneConstants;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.awt.Point;
import java.net.URI;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import javax.swing.DefaultComboBoxModel;
import javax.swing.DefaultListModel;
import javax.swing.border.MatteBorder;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.HyperlinkEvent;

import java.awt.Color;
import javax.swing.SpinnerNumberModel;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.forms.layout.ColumnSpec;
import com.jgoodies.forms.layout.RowSpec;

import control.Controller;

import com.jgoodies.forms.layout.FormSpecs;
import net.miginfocom.swing.MigLayout;
import javax.swing.GroupLayout;
import javax.swing.ImageIcon;
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
	//private JSpinner spinner;
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
	
	private List<PiantaType> arrayListaCarrello = new ArrayList<PiantaType>();
	private List<PiantaType> arrayListCercaPiante = new ArrayList<PiantaType>();
	private List<AcquarioType> arrayListAcquari = new ArrayList<AcquarioType>();
	private List<PiantaType> arrayListViewPianteForAcquario = new ArrayList<PiantaType>();
	private JSpinner spinnerLarghezza;
	private JSpinner spinnerAltezza;
	private JSpinner spinnerLitraggio;
	private JSpinner spinnerLunghezza;
	private JButton btnCancellaPianteAcquario;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
		            
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
		setBounds(100, 100, 1008,530);
		setTitle("Progetto Acquari");
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
		sl_panelNew.putConstraint(SpringLayout.NORTH, scrollPaneNewDescrizione, 26, SpringLayout.SOUTH, lblNewAltezza);
		sl_panelNew.putConstraint(SpringLayout.NORTH, lblNewAltezza, 22, SpringLayout.SOUTH, lblNewLarghezza);
		sl_panelNew.putConstraint(SpringLayout.EAST, lblNewAltezza, -10, SpringLayout.EAST, panelNew);
		panelNew.add(lblNewAltezza);
		
		spinnerLitraggio = new JSpinner();
		spinnerLitraggio.setModel(new SpinnerNumberModel(Long.valueOf(1), Long.valueOf(1), null, Long.valueOf(1)));
		sl_panelNew.putConstraint(SpringLayout.NORTH, spinnerLitraggio, 10, SpringLayout.NORTH, panelNew);
		sl_panelNew.putConstraint(SpringLayout.WEST, spinnerLitraggio, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, spinnerLitraggio, 158, SpringLayout.WEST, panelNew);
		JSpinner.DefaultEditor editor = (JSpinner.DefaultEditor) spinnerLitraggio.getEditor();
		editor.getTextField().setEditable(false);
		panelNew.add(spinnerLitraggio);
		
		spinnerLunghezza = new JSpinner();
		sl_panelNew.putConstraint(SpringLayout.NORTH, spinnerLunghezza, 10, SpringLayout.SOUTH, spinnerLitraggio);
		sl_panelNew.putConstraint(SpringLayout.WEST, spinnerLunghezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, spinnerLunghezza, 158, SpringLayout.WEST, panelNew);
		spinnerLunghezza.setModel(new SpinnerNumberModel(Long.valueOf(1), Long.valueOf(1), null, Long.valueOf(1)));
		JSpinner.DefaultEditor editor1 = (JSpinner.DefaultEditor) spinnerLunghezza.getEditor();
		editor1.getTextField().setEditable(false);
		panelNew.add(spinnerLunghezza);
		
		spinnerLarghezza = new JSpinner();
		sl_panelNew.putConstraint(SpringLayout.NORTH, spinnerLarghezza, 16, SpringLayout.SOUTH, spinnerLunghezza);
		sl_panelNew.putConstraint(SpringLayout.WEST, spinnerLarghezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, spinnerLarghezza, 158, SpringLayout.WEST, panelNew);
		spinnerLarghezza.setModel(new SpinnerNumberModel(Long.valueOf(1), Long.valueOf(1), null, Long.valueOf(1)));
		JSpinner.DefaultEditor editor2 = (JSpinner.DefaultEditor) spinnerLarghezza.getEditor();
		editor2.getTextField().setEditable(false);
		panelNew.add(spinnerLarghezza);
		
		spinnerAltezza = new JSpinner();
		spinnerAltezza.setModel(new SpinnerNumberModel(Long.valueOf(1), Long.valueOf(1), null, Long.valueOf(1)));
		sl_panelNew.putConstraint(SpringLayout.NORTH, spinnerAltezza, 16, SpringLayout.SOUTH, spinnerLarghezza);
		sl_panelNew.putConstraint(SpringLayout.WEST, spinnerAltezza, 10, SpringLayout.WEST, panelNew);
		sl_panelNew.putConstraint(SpringLayout.EAST, spinnerAltezza, 158, SpringLayout.WEST, panelNew);
		JSpinner.DefaultEditor editor3 = (JSpinner.DefaultEditor) spinnerAltezza.getEditor();
		editor3.getTextField().setEditable(false);
		panelNew.add(spinnerAltezza);
		
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
		
		btnCancellaPianteAcquario = new JButton("cancella pianta");
		GroupLayout gl_panelViewAcquario = new GroupLayout(panelViewAcquario);
		gl_panelViewAcquario.setHorizontalGroup(
			gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_panelViewAcquario.createSequentialGroup()
					.addGap(10)
					.addGroup(gl_panelViewAcquario.createParallelGroup(Alignment.LEADING)
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLitraggio, GroupLayout.DEFAULT_SIZE, 199, Short.MAX_VALUE)
							.addGap(98)
							.addComponent(lblViewLitraggio))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLunghezza, GroupLayout.DEFAULT_SIZE, 199, Short.MAX_VALUE)
							.addGap(88)
							.addComponent(lblViewLunghezza))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewLarghezza, GroupLayout.DEFAULT_SIZE, 199, Short.MAX_VALUE)
							.addGap(90)
							.addComponent(lblViewLarghezza))
						.addGroup(gl_panelViewAcquario.createSequentialGroup()
							.addComponent(textFieldViewAltezza, GroupLayout.DEFAULT_SIZE, 199, Short.MAX_VALUE)
							.addGap(102)
							.addComponent(lblViewAltezza))
						.addComponent(scrollPaneViewDescrizioneAcquario, GroupLayout.DEFAULT_SIZE, 335, Short.MAX_VALUE)
						.addComponent(lblViewDescrizione)
						.addComponent(scrollPaneViewListaPianteAcquario, GroupLayout.DEFAULT_SIZE, 335, Short.MAX_VALUE))
					.addGap(8))
				.addGroup(gl_panelViewAcquario.createSequentialGroup()
					.addContainerGap()
					.addComponent(btnCancellaPianteAcquario)
					.addContainerGap(240, Short.MAX_VALUE))
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
					.addGap(5)
					.addComponent(scrollPaneViewListaPianteAcquario, GroupLayout.DEFAULT_SIZE, 234, Short.MAX_VALUE)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(btnCancellaPianteAcquario)
					.addGap(17))
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
	    
	    
	    
	    
	   
	    
	    btnSalvaAggiungiPiante = new JButton("Aggiungi Piante");
	    sl_panelSalva.putConstraint(SpringLayout.WEST, btnSalvaAggiungiPiante, 85, SpringLayout.EAST, scrollPaneSalvaListaCarrello);
	    sl_panelSalva.putConstraint(SpringLayout.SOUTH, btnSalvaAggiungiPiante, -39, SpringLayout.SOUTH, panelSalva);
	    panelSalva.add(btnSalvaAggiungiPiante);
	    
	
	    
	    
	    
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
	 * @return the btnCancellaPianteAcquario
	 */
	public JButton getBtnCancellaPianteAcquario() {
		return btnCancellaPianteAcquario;
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

	/**
	 * Retrieves the text from the textFieldCercaNome object.
	 * Returns null if the textFieldCercaNome is empty.
	 * 
	 * @return the text from textFieldCercaNome or null if it's empty
	 */
	public String getTxtCercaNome() {
		if(textFieldCercaNome.getText().equals(""))
			return null;
		return textFieldCercaNome.getText();
	}
	
	/**
	 * Retrieves the selected item from the comboBoxCercaOrigine object.
	 * Returns null if the selected item is "Qualsiasi".
	 * 
	 * @return the selected item as a String or null if it's "Qualsiasi"
	 */
	public String getItemComboBoxCercaOrigine() {
		if(comboBoxCercaOrigine.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaOrigine.getSelectedItem().toString();
	}
	
	/**
	 * Retrieves the selected item from the comboBoxCercaTassoCrescita object.
	 * Returns null if the selected item is "Qualsiasi".
	 * 
	 * @return the selected item as a String or null if it's "Qualsiasi"
	 */
	public String getItemComboBoxCercaTassoCrescita() {
		if(comboBoxCercaTassoCrescita.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaTassoCrescita.getSelectedItem().toString();
	}
	
	/**
	 * Retrieves the selected item from the comboBoxCercaLuce object.
	 * Returns null if the selected item is "Qualsiasi".
	 * 
	 * @return the selected item as a String or null if it's "Qualsiasi"
	 */
	public String getItemComboBoxCercaLuce() {
		if(comboBoxCercaLuce.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaLuce.getSelectedItem().toString();
	}
	
	/**
	 * Retrieves the selected item from the comboBoxCercaCo2 object.
	 * Returns null if the selected item is "Qualsiasi".
	 * 
	 * @return the selected item as a String or null if it's "Qualsiasi"
	 */
	public String getItemComboBoxCercaCo2() {
		if(comboBoxCercaCo2.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaCo2.getSelectedItem().toString();
	}
	
	/**
	 * Retrieves the selected item from the comboBoxCercaDifficolta object.
	 * Returns null if the selected item is "Qualsiasi".
	 * 
	 * @return the selected item as a String or null if it's "Qualsiasi"
	 */
	public String getItemComboBoxCercaDifficolta() {
		if(comboBoxCercaDifficolta.getSelectedItem().toString().equals("Qualsiasi"))
			return null;
		return comboBoxCercaDifficolta.getSelectedItem().toString();
	}
	
	/**
	 * Retrieves the value from the spinnerLitraggio object.
	 * 
	 * @return the value as a Long
	 */
	public Long getValueSpinnerLitraggio() {
		return ((Long)spinnerLitraggio.getValue());
	}
	
	/**
	 * Retrieves the value from the spinnerLunghezza object.
	 * 
	 * @return the value as a Long
	 */
	public Long getValueSpinnerLunghezza() {
		return ((Long)spinnerLunghezza.getValue());
	}
	
	/**
	 * Retrieves the value from the spinnerLarghezza object.
	 * 
	 * @return the value as a Long
	 */
	public Long getValueSpinnerLarghezza() {
		return ((Long)spinnerLarghezza.getValue());
	}
	
	/**
	 * Retrieves the value from the spinnerAltezza object.
	 * 
	 * @return the value as a Long
	 */
	public Long getValueSpinnerAltezza() {
		return ((Long)spinnerAltezza.getValue());
	}
	
	/**
	 * Retrieves the text from the textAreaNewDescrizione object.
	 * 
	 * @return the text as a String
	 */
	public String getTextAreaDescrizione() {
		return textAreaNewDescrizione.getText();
	}
	
	/**
	 * Retrieves the selected items from the listCercaPiante object.
	 * Removes the selected items from arrayListCercaPiante and the model of listCercaPiante.
	 * 
	 * @return a list of selected PiantaType objects
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
     * Removes all items from the list used for searching plants.
     * 
     * This method clears the arrayListCercaPiante by removing all elements from it. 
     * Additionally, it retrieves the model of the listCercaPiante JList, which is assumed to be a 
     * DefaultListModel<String>, and removes all elements from this model as well. This ensures 
     * that both the underlying ArrayList and the displayed JList are cleared of all items.
     */
    public void removeAllItemsFromListCercaPiante() {
        arrayListCercaPiante.clear(); // Rimuove tutti gli elementi dall'ArrayList
        DefaultListModel<String> model = (DefaultListModel<String>) listCercaPiante.getModel();
        model.removeAllElements(); // Rimuove tutti gli elementi dal DefaultListModel
    }
    
    /**
     * Adds a list of PiantaType items to the shopping cart list.
     * 
     * This method iterates over the provided list of PiantaType items, creates a JPanel for each item 
     * using the createPanelWithComponentsForListaCarrello method, and adds the JPanel to the arrayPanelsListaCarrello 
     * list. Additionally, each PiantaType item is added to the arrayListaCarrello list. After adding all panels 
     * to the arrayPanelsListaCarrello list, the method adds each panel to the panelSalvaListaCarrello JPanel 
     * container. Finally, the layout of the panelSalvaListaCarrello is updated to a dynamic grid layout with a 
     * single column, and the panel is revalidated and repainted to reflect the changes.
     * 
     * @param itemsToAdd the list of PiantaType items to add to the shopping cart list
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
     * Creates and returns a JPanel containing components for displaying a PiantaType item in a shopping cart list.
     * 
     * This method creates a JPanel with a border and sets its name to the ID of the provided PiantaType item.
     * The panel contains a JCheckBox for selection, a JLabel to display the plant's name, and a JSpinner 
     * for quantity selection. The JSpinner is initialized with a SpinnerNumberModel to allow selecting 
     * quantities from 0 to any positive integer. If the quantity is set to 0 using the JSpinner, the item 
     * is removed from the shopping cart list.
     * 
     * @param plant the PiantaType item to display in the panel
     * @return a JPanel containing the components for the provided PiantaType item
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
	    JSpinner.DefaultEditor editor = (JSpinner.DefaultEditor) spinner.getEditor();
		editor.getTextField().setEditable(false);
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
	            	removeItemFromListaCarrello(spinner);
	            }
	        }

			
	    });

	    
    	return panel_1;
    	
    }

    /**
     * Updates the list of AcquarioType items and refreshes the comboBoxSalvaAcquari and listAcquari components.
     * 
     * This method clears the existing arrayListAcquari and populates it with the provided itemsToUpdate list.
     * It then updates the comboBoxSalvaAcquari model and the listAcquari model with the new items from the 
     * arrayListAcquari list, displaying each item's ID and liters in the respective components.
     * 
     * @param itemsToUpdate a List of AcquarioType objects representing the items to update the list with
     */
    public void updateListAcquari(List<AcquarioType> itemsToUpdate) {
        arrayListAcquari.clear();
        arrayListAcquari.addAll(itemsToUpdate);
        
        DefaultComboBoxModel<String> comboBoxModel = new DefaultComboBoxModel<String>();
        
        for (AcquarioType acquario : arrayListAcquari) {
            String itemText = Long.toString(acquario.getIdAcquario()) + ")   litri:" + Long.toString(acquario.getLitri());
            comboBoxModel.addElement(itemText);
        }
        
        comboBoxSalvaAcquari.setModel(comboBoxModel);
        
        
        // Aggiornamento della JList listAcquari
        DefaultListModel<String> listModel = new DefaultListModel<String>();
        for (AcquarioType acquario : arrayListAcquari) {
            String itemText = Long.toString(acquario.getIdAcquario()) + ")   litri:" + Long.toString(acquario.getLitri());
            listModel.addElement(itemText);
        }
        listAcquari.setModel(listModel);
    }

    /**
     * Retrieves the selected AcquarioType item from the listAcquari component.
     * 
     * This method fetches the selected index from the listAcquari component and retrieves 
     * the corresponding AcquarioType item from the arrayListAcquari list.
     * 
     * @return the selected AcquarioType item from the arrayListAcquari list
     * @throws Exception if no item is selected in the listAcquari component
     */
    public AcquarioType getSelectedItemListAcquari() throws Exception{

    	AcquarioType selectedItem;
	    int selectedIndex = listAcquari.getSelectedIndex();
	    if(selectedIndex == -1)
	    	throw new Exception("Attenzione: selezionare prima un acquario");
	    
	    selectedItem = arrayListAcquari.get(selectedIndex);
	    
	    return selectedItem;
    }

    /**
     * Displays the details of a selected AcquarioType and updates the list of plants for the selected aquarium.
     * 
     * This method fetches the selected AcquarioType item, retrieves its details, and displays them in 
     * corresponding text fields. It also populates the arrayListViewPianteForAcquario list with the provided 
     * list of plants to view. Furthermore, it updates the view of the listViewPianteAcquario with the 
     * names of the plants and their corresponding quantities.
     * 
     * @param plantsToView a List of PiantaType objects representing the plants to be viewed in the selected aquarium
     * @param quantitas a List of Long values representing the quantities of the plants to be displayed
     * @throws Exception if there's an issue retrieving the selected AcquarioType item or updating the view
     */
    public void viewSelectedAcquario(List<PiantaType> plantsToView, List<Long> quantitas) throws Exception{
    	AcquarioType selectedItem = this.getSelectedItemListAcquari();
    	
    	//listAcquari.clearSelection();
    	textFieldViewLitraggio.setText(Long.toString(selectedItem.getLitri()));
    	textFieldViewLarghezza.setText(Long.toString(selectedItem.getLarghezza()));
    	textFieldViewLunghezza.setText(Long.toString(selectedItem.getLunghezza()));
    	textFieldViewAltezza.setText(Long.toString(selectedItem.getAltezza()));
    	textAreaViewDescrizioneAcquario.setText(selectedItem.getDescrizione());
    	
    	//arrayListViewPianteForAcquario.clear();
    	arrayListViewPianteForAcquario.addAll(plantsToView);
    	
    	this.updateViewListPianteForAcquario(quantitas);
    	
    }
    
    /**
     * Updates the view of the listViewPianteAcquario with plant names and quantities.
     * 
     * This method updates the content of the listViewPianteAcquario component by creating a new 
     * DefaultListModel and populating it with the names of plants from the arrayListViewPianteForAcquario list 
     * along with their corresponding quantities from the provided quantitas list.
     * 
     * @param quantitas a List of Long values representing the quantities of plants
     */
    private void updateViewListPianteForAcquario(List<Long> quantitas) {
    	// Aggiornamento della JList listAcquari
    	
        DefaultListModel<String> listModel = new DefaultListModel<String>();
        
        int i = 0;
        for (PiantaType pianta : arrayListViewPianteForAcquario) {
            
            listModel.addElement(pianta.getNome()+"   Q:"+Long.toString(quantitas.get(i)));
            
            i++;
            
        }
        
        listViewPianteAcquario.setModel(listModel);
    }
    
    /**
     * Resets all the view components related to the aquarium and sets default values.
     * 
     * This method clears the text fields, text areas, and lists related to the aquarium view.
     * It also resets the spinners to default values and clears the array list of plants
     * associated with the aquarium. Finally, it updates the plant list view with the cleared data.
     */
    public void resetViewAndNew() {
    	textFieldViewLitraggio.setText(null);
    	textFieldViewLarghezza.setText(null);
    	textFieldViewLunghezza.setText(null);
    	textFieldViewAltezza.setText(null);
    	textAreaViewDescrizioneAcquario.setText(null);
    	
    	arrayListViewPianteForAcquario.clear();
    	this.updateViewListPianteForAcquario(new ArrayList<Long>(0));
    	
    	spinnerLitraggio.setValue(new Long(1));
    	spinnerLunghezza.setValue(new Long(1));
    	spinnerLarghezza.setValue(new Long(1));
    	spinnerAltezza.setValue(new Long(1));
    	textAreaNewDescrizione.setText(null);
    }
    
    /**
     * Retrieves the indices of selected checkboxes within the array of panels.
     * 
     * This method iterates through each panel in the arrayPanelsListaCarrello and checks
     * if it contains a selected JCheckBox component. If a checkbox is selected within a panel,
     * its index is added to a list of selected indices. The method then converts this list 
     * of indices to an array of integers and returns it.
     * 
     * @return an array of integers representing the indices of selected checkboxes
     */
    public int[] getSelectedCheckBoxIndices() {
        List<Integer> selectedIndices = new ArrayList<>();

        for (int i = 0; i < arrayPanelsListaCarrello.size(); i++) {
            JPanel panel = arrayPanelsListaCarrello.get(i);
            Component[] components = panel.getComponents();

            for (Component component : components) {
                if (component instanceof JCheckBox) {
                    JCheckBox checkBox = (JCheckBox) component;
                    if (checkBox.isSelected()) {
                        selectedIndices.add(i);
                        break;  // Esci dal ciclo se il checkbox è selezionato
                    }
                }
            }
        }
        
        // Converti la lista di indici in un array di interi
        return selectedIndices.stream().mapToInt(Integer::intValue).toArray();
    }
    
    /**
     * Retrieves the value of the JSpinner component at the specified index within the array of panels.
     * 
     * This method retrieves the JSpinner component located at the given index in the arrayPanelsListaCarrello.
     * If a JSpinner is found, its integer value is converted to a Long and returned. If no JSpinner is found
     * at the specified index, an exception is thrown with an error message indicating the failure to retrieve
     * the spinner value.
     * 
     * @param index the index of the panel containing the JSpinner component
     * @return the Long value of the JSpinner at the specified index
     * @throws Exception if no JSpinner is found at the specified index
     */
    public Long getValueOfSpinnerListaCarrello(int index) throws Exception{
    	
    	Long value = null;
    	
    	JPanel panel = arrayPanelsListaCarrello.get(index);
    	Component[] components = panel.getComponents();

        for (Component component : components) {
            if (component instanceof JSpinner) {
                JSpinner spinner = (JSpinner) component;
                value = ((Integer)spinner.getValue()).longValue();
                
                break;
            }
        }
    	
        if(value == null)
        	throw new Exception("Errore: non è stato possibile recuperare il valore dalla quantità della pianta");
    	//qui rimuovi il pannello parent dal carrello
        
    	return value;
    }
    
    /**
     * Retrieves the ID of the PiantaType object at the specified index within the array of items in the cart.
     * 
     * This method retrieves the PiantaType object located at the given index in the arrayListaCarrello.
     * If a valid PiantaType object is found, its ID is returned. If no object is found
     * at the specified index, an exception is thrown with an error message indicating the failure to retrieve
     * the ID of the selected plant in the cart.
     * 
     * @param index the index of the PiantaType object in the arrayListaCarrello
     * @return the ID of the PiantaType object at the specified index
     * @throws Exception if no PiantaType object is found at the specified index
     */
    public Long getIdOfPiantaListaCarrello(int index) throws Exception{
    	if(arrayListaCarrello.get(index)==null)
    		throw new Exception("Errore: non è stato possibile recuperare l'id della pianta selezionata nel carrello");
    	//devi fare il remove poi
    	return arrayListaCarrello.get(index).getIdPianta();
    	
    }
    
    /**
     * Retrieves the ID of the selected AcquarioType object in the comboBoxSalvaAcquari.
     * 
     * This method retrieves the AcquarioType object that corresponds to the selected index
     * in the comboBoxSalvaAcquari. If a valid AcquarioType object is found, its ID is returned.
     * If no object is found at the selected index, an exception is thrown with an error message
     * indicating the failure to retrieve the ID of the selected aquarium for saving.
     * 
     * @return the ID of the selected AcquarioType object in the comboBoxSalvaAcquari
     * @throws Exception if no AcquarioType object is found at the selected index
     */
    public Long getIdOfAcquarioSelectedInComboBoxSalvaAcquario() throws Exception{
    	if(arrayListAcquari.get(comboBoxSalvaAcquari.getSelectedIndex())==null)
    		throw new Exception("Errore: impossibile recuperare id dell'acuqario selezionato per il salvataggio");
    	
    	return arrayListAcquari.get(comboBoxSalvaAcquari.getSelectedIndex()).getIdAcquario();
    }
    
    /**
     * Removes the item associated with the given JSpinner from the shopping cart list.
     * 
     * This method removes the JPanel containing the specified JSpinner from the shopping cart.
     * It removes the panel from both the visual display and the internal data structures.
     * After removing the panel, it updates the display and layout of the shopping cart.
     * 
     * @param spinner the JSpinner whose associated item needs to be removed
     */
    public void removeItemFromListaCarrello(JSpinner spinner) {
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
    
    /**
     * Removes the item at the specified index from the shopping cart list.
     * 
     * This method removes the JPanel at the specified index from the shopping cart.
     * It clears the panel's contents, updates the display, and removes the corresponding 
     * item from both the visual display and the internal data structures.
     * After removing the item, it updates the display and layout of the shopping cart.
     * 
     * @param index the index of the item to be removed from the shopping cart
     */
    public void removeItemFromListaCarrello(int index) {
    	arrayPanelsListaCarrello.get(index).removeAll();
    	arrayPanelsListaCarrello.get(index).revalidate();
    	arrayPanelsListaCarrello.get(index).repaint();
    	
    	arrayPanelsListaCarrello.remove(index);
    	arrayListaCarrello.remove(index);
    	
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
	    btnCancellaPianteAcquario.addActionListener(controller);
	    
	    btnCercaPianta.addActionListener(controller);
	    btnCercaAggiungiPianta.addActionListener(controller);
	    
	    
	    btnSalvaAggiungiPiante.addActionListener(controller);
	    
	    listCercaPiante.addMouseListener(controller);
	    listViewPianteAcquario.addMouseListener(controller);
	    
	    listCercaPiante.addKeyListener(controller);
	    listAcquari.addKeyListener(controller);
	    listViewPianteAcquario.addKeyListener(controller);
	    
	    
	}
	
	/**
	 * Displays the specified panel within the specified layout.
	 * 
	 * This method switches between different layouts based on the provided layoutName 
	 * and shows the panel identified by the panelName within that layout.
	 * 
	 * Supported layoutNames:
	 * - "cardLayout" for CardLayout
	 * - "acquarioLayout" for another specific layout (assumed to be named "acquarioLayout")
	 * 
	 * @param layoutName the name of the layout to use ("cardLayout" or "acquarioLayout")
	 * @param panelName the name of the panel to display within the specified layout
	 * @throws Exception if an invalid layoutName is provided
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
	 * Displays a message dialog with the specified message.
	 * 
	 * This method shows a message dialog box containing the provided message.
	 * Additionally, it prints the message to the console for debugging purposes.
	 * 
	 * @param message the message to display in the message dialog
	 */
	public void messageDialog(String message) {
		JOptionPane.showMessageDialog(this, message);
		System.out.println(message);
	}
	
	/**
	 * Retrieves the index of the list element at the specified point.
	 * 
	 * This method translates the provided Point object to an index within the 
	 * listCercaPiante component. It returns the index of the list element 
	 * located at the specified point.
	 * 
	 * @param p the Point object representing the location of the mouse click
	 * @return the index of the list element at the specified point
	 */
	public int getIndexOfElemenListCercaPiantaForMouseClick(Point p) {
		return listCercaPiante.locationToIndex(p);
	}
	
	/**
	 * Retrieves the index of the list element at the specified point.
	 * 
	 * This method translates the provided Point object to an index within the 
	 * listViewPianteAcquario component. It returns the index of the list element 
	 * located at the specified point.
	 * 
	 * @param p the Point object representing the location of the mouse click
	 * @return the index of the list element at the specified point
	 */
	public int getIndexOfElemenListViewPianteAcquarioForMouseClick(Point p) {
		return listViewPianteAcquario.locationToIndex(p);
	}
	
	/**
	 * Clears the current selection in the listAcquari component.
	 * 
	 * This method clears the current selection in the listAcquari component,
	 * deselecting any items that may have been previously selected.
	 */
	public void clearSelectionListAcquari() {
		listAcquari.clearSelection();
	}
	
	/**
	 * Clears the current selection in the listCercaPiante component.
	 * 
	 * This method clears the current selection in the listCercaPiante component,
	 * deselecting any items that may have been previously selected.
	 */
	public void clearSelectionListCercaPiante() {
		listCercaPiante.clearSelection();
	}
	
	/**
	 * Clears the current selection in the listViewPianteAcquario component.
	 * 
	 * This method clears the current selection in the listViewPianteAcquario component,
	 * deselecting any items that may have been previously selected.
	 */
	public void clearSelectionListViewPianteAcquario() {
		listViewPianteAcquario.clearSelection();
	}

	/**
	 * Retrieves the PiantaType object at the specified index from the arrayListCercaPiante list.
	 * 
	 * This method retrieves the PiantaType object located at the given index in the arrayListCercaPiante list.
	 * If the provided index is out of bounds or if there's any other exception during the retrieval process,
	 * appropriate exceptions are thrown with relevant error messages.
	 * 
	 * @param index the index of the desired PiantaType object in the arrayListCercaPiante list
	 * @return the PiantaType object at the specified index
	 * @throws IndexOutOfBoundsException if the index is out of the bounds of the list
	 * @throws Exception if any other error occurs during retrieval
	 */
	public PiantaType getPiantaAltClickedInListCerca(int index) throws IndexOutOfBoundsException, Exception {
        if (index < 0 || index > arrayListCercaPiante.size()) {
            throw new IndexOutOfBoundsException("Indice fuori dai limiti della lista");
        }

        PiantaType pianta = arrayListCercaPiante.get(index);
        System.out.println("l'indice di piantaType è: "+pianta.getIdPianta());
        
        return pianta;
    }
	
	/**
	 * Retrieves the PiantaType object at the specified index from the arrayListViewPianteForAcquario list.
	 * 
	 * This method retrieves the PiantaType object located at the given index in the arrayListViewPianteForAcquario list.
	 * If the provided index is out of bounds or if there's any other exception during the retrieval process,
	 * appropriate exceptions are thrown with relevant error messages.
	 * 
	 * @param index the index of the desired PiantaType object in the arrayListViewPianteForAcquario list
	 * @return the PiantaType object at the specified index
	 * @throws IndexOutOfBoundsException if the index is out of the bounds of the list
	 * @throws Exception if any other error occurs during retrieval
	 */
	public PiantaType getPiantaAltClickInPianteForAcquario(int index)throws IndexOutOfBoundsException, Exception {
        if (index < 0 || index > arrayListViewPianteForAcquario.size()) {
            throw new IndexOutOfBoundsException("Indice fuori dai limiti della lista");
        }

        PiantaType pianta = arrayListViewPianteForAcquario.get(index);
        System.out.println("l'indice di piantaType è: "+pianta.getIdPianta());
        
        return pianta;
	}

	/**
	 * Retrieves the selected PiantaType object from the arrayListViewPianteForAcquario list.
	 * 
	 * This method retrieves the selected PiantaType object from the arrayListViewPianteForAcquario list
	 * based on the current selection index of the listViewPianteAcquario component.
	 * If the selected index is invalid or if the retrieved object is null, an exception is thrown with a relevant error message.
	 * 
	 * @return the selected PiantaType object from the arrayListViewPianteForAcquario list
	 * @throws Exception if the selected index is out of bounds or if the retrieved object is null
	 */
	public PiantaType getSelectedItemOfListPlantsOfAcquario() throws Exception{
		if(arrayListViewPianteForAcquario.get(listViewPianteAcquario.getSelectedIndex())==null)
    		throw new Exception("Errore: impossibile eliminare la pianta");
    	
    	return arrayListViewPianteForAcquario.get(listViewPianteAcquario.getSelectedIndex());
	}
	
	

	/**
	 * Displays an image of a plant along with a clickable link.
	 * 
	 * This method creates a JFrame to display an ImageIcon of a plant, along with a clickable link below the image.
	 * The provided image, name of the plant, and link are used to construct and display the JFrame.
	 * The link is clickable and will open the provided URL in the default web browser when activated.
	 * 
	 * @param nomePianta the name of the plant to be displayed in the JFrame title
	 * @param immagine the ImageIcon of the plant to be displayed
	 * @param link the URL link associated with the plant image
	 */
	public void displayPlantImage(String nomePianta, ImageIcon immagine, String link) {
	    String decodedLink = URLDecoder.decode(link, StandardCharsets.UTF_8);

	    JLabel imageLabel = new JLabel(immagine);

	    // Create a clickable link using JEditorPane
	    JEditorPane linkPane = new JEditorPane();
	    linkPane.setContentType("text/html");
	    
	    // Format the link as an HTML anchor tag
	    String htmlLink = "<a href=\"" + decodedLink + "\">" + decodedLink + "</a>";
	    linkPane.setText(htmlLink);
	    
	    linkPane.setEditable(false);  // Make it non-editable
	    linkPane.setBorder(null);  // Remove the border
	    linkPane.addHyperlinkListener(e -> {
	        try {
	            if (e.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
	                Desktop.getDesktop().browse(new URI(e.getURL().toString()));
	            }
	        } catch (Exception ex) {
	            // Handle exceptions if the link cannot be opened
	        }
	    });

	    // Create a panel for the image and link
	    JPanel contentPanel = new JPanel();
	    contentPanel.setLayout(new BorderLayout());
	    contentPanel.add(imageLabel, BorderLayout.CENTER);
	    contentPanel.add(linkPane, BorderLayout.SOUTH);  // Add linkPane below the image

	    // Create the frame
	    JFrame imageFrame = new JFrame(nomePianta);
	    imageFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	    imageFrame.add(contentPanel);  // Add the panel with image and link
	    imageFrame.pack();
	    imageFrame.setVisible(true);
	}
	
	
}
