package view;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.SpringLayout;
import java.awt.CardLayout;
import javax.swing.JScrollPane;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JEditorPane;
import javax.swing.DropMode;
import javax.swing.JList;

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
		panelCardMain.setLayout(new CardLayout(0, 0));
		
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
	}
}
