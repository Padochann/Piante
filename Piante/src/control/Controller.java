package control;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Desktop;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JEditorPane;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.UIManager;
import javax.swing.event.AncestorEvent;
import javax.swing.event.AncestorListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.HyperlinkEvent;

import model.RestEasyPlantsClient;
import piante.AcquariType;
import piante.AcquarioType;
import piante.ImmagineType;
import piante.ImmaginiType;
import piante.PiantaAcquarioType;
import piante.PiantaType;
import piante.PianteAcquariType;
import piante.PianteType;
import view.Window;
import view.Window;


public class Controller implements ActionListener, MouseListener, KeyListener{
	
	private Window w;
	private RestEasyPlantsClient requester;
	private JButton lastToken;

	/**
	 * Constructor for the Controller class.
	 * 
	 * This constructor initializes a Controller object with a given Window instance.
	 * It registers itself as an event listener with the provided Window instance.
	 * Additionally, it creates a new instance of RestEasyPlantsClient for making API requests
	 * and updates the list of acquari in the Window instance.
	 * 
	 * @param w the Window instance to associate with this Controller.
	 * 
	 * @throws Exception if there's an issue initializing the Controller or registering the event.
	 */
	public Controller(Window w) throws Exception {
		this.w= w;
		this.w.registerEvent(this);
		this.requester= new RestEasyPlantsClient();
		w.updateListAcquari(this.getAcquariList());
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
		
		
	        try {
	            if (e.getSource() == w.getBtnAcquari()) {
	                w.showPanel("cardLayout", "panelAcquari");
	                w.getBtnAcquari().setBackground(Color.CYAN);
	                if (lastToken != null && lastToken != w.getBtnAcquari()) {
	                    lastToken.setBackground(UIManager.getColor("Button.background"));
	                }
	                lastToken = w.getBtnAcquari();
	               w.updateListAcquari(getAcquariList());
	                w.resetViewAndNew();
	            }
	            if (e.getSource() == w.getBtnCerca()) {
	                w.showPanel("cardLayout", "panelCerca");
	                w.getBtnCerca().setBackground(Color.CYAN);
	                if (lastToken != null && lastToken != w.getBtnCerca()) {
	                    lastToken.setBackground(UIManager.getColor("Button.background"));
	                }
	                lastToken = w.getBtnCerca();
	               
	            }
	            if (e.getSource() == w.getBtnSalva()) {
	                w.showPanel("cardLayout", "panelSalva");
	                w.getBtnSalva().setBackground(Color.CYAN);
	                if (lastToken != null && lastToken != w.getBtnSalva()) {
	                    lastToken.setBackground(UIManager.getColor("Button.background"));
	                }
	                lastToken = w.getBtnSalva();
	            
	            }
			
		
			if(e.getSource() == w.getBtnView())
			{
				w.showPanel("acquarioLayout", "panelView");
				
				this.viewAcquario();
			}
			if(e.getSource() == w.getBtnNew())
			{
				w.resetViewAndNew();
				
				w.showPanel("acquarioLayout", "panelNew");
			}
			
			
			if(e.getSource() == w.getBtnDelete())
			{
				
				this.cancellaAcquario();
			}
			if(e.getSource() == w.getBtnSalvaNewAcquario())
			{
			
				this.salvaAcquario();
			}
			if(e.getSource() == w.getBtnCancellaPianteAcquario())
			{
				
				this.cancellaPiantaDaAcquario();
			}
			
			
			if(e.getSource() == w.getBtnCercaPianta())
			{
				
				w.removeAllItemsFromListCercaPiante();
				this.cercaPianta();
			}
			if(e.getSource() == w.getBtnCercaAggiungiPianta())
			{
				
				List<PiantaType> tmp= w.getSelectedItemsListCercaPiante();
				w.addItemsToListaCarrello(tmp);
			}
			
			
			if(e.getSource() == w.getBtnSalvaAggiungiPiante())
			{
				this.salvaPiante();
			}
			
		}
		
		catch(Exception e1) {
			w.messageDialog(e1.getMessage());
		}
	}

	
	/**
	 * Searches for plants based on various criteria.
	 * 
	 * This method constructs a query string for searching plants based on the values obtained 
	 * from various UI components of the application. The constructed query string is then 
	 * URL-encoded and appended to the base CRUD operation and table name to form a complete 
	 * query string. After building the query string, an API call is made to fetch the plant 
	 * data based on the constructed query. The fetched plant data is then printed and added 
	 * to the list used for searching plants in the UI.
	 * 
	 * @throws Exception if there's an issue with constructing the query string or fetching data from the API.
	 */
	private void cercaPianta() throws Exception {
	    // Costruisci la query string in base ai valori ottenuti dai metodi
	    StringBuilder queryStringBuilder = new StringBuilder("crud=r&table=piante");
	    
	    String txtCercaNome = w.getTxtCercaNome();
	    String itemOrigine = w.getItemComboBoxCercaOrigine();
	    String itemTassoCrescita = w.getItemComboBoxCercaTassoCrescita();
	    String itemLuce = w.getItemComboBoxCercaLuce();
	    String itemCo2 = w.getItemComboBoxCercaCo2();
	    String itemDifficolta = w.getItemComboBoxCercaDifficolta();
	    
	    if (txtCercaNome != null && !txtCercaNome.isEmpty()) {
	        queryStringBuilder.append("&nome=").append(URLEncoder.encode(txtCercaNome, StandardCharsets.UTF_8.toString()));
	    }
	    if (itemOrigine != null) {
	        queryStringBuilder.append("&origine=").append(URLEncoder.encode(itemOrigine, StandardCharsets.UTF_8.toString()));
	    }
	    if (itemTassoCrescita != null) {
	        queryStringBuilder.append("&tasso_crescita=").append(URLEncoder.encode(itemTassoCrescita, StandardCharsets.UTF_8.toString()));
	    }
	    if (itemLuce != null) {
	        queryStringBuilder.append("&luce=").append(URLEncoder.encode(itemLuce, StandardCharsets.UTF_8.toString()));
	    }
	    if (itemCo2 != null) {
	        queryStringBuilder.append("&co2=").append(URLEncoder.encode(itemCo2, StandardCharsets.UTF_8.toString()));
	    }
	    if (itemDifficolta != null) {
	        queryStringBuilder.append("&difficolta=").append(URLEncoder.encode(itemDifficolta, StandardCharsets.UTF_8.toString()));
	    }

	    String queryString = queryStringBuilder.toString();
	    System.out.println(queryString);
	    // Esegui la chiamata API con la query string costruita
	    PianteType pianteData = (PianteType) requester.fetchDataFromApi(queryString);
	    System.out.println(pianteData.getItem().toString());
	    w.addItemsToListCercaPiante(pianteData.getItem());
	}

	/**
	 * Retrieves a list of aquariums from the database.
	 * 
	 * This method constructs a query string specifically for fetching aquarium data from 
	 * the database. The constructed query string is then used to make an API call to fetch 
	 * the aquarium data. The fetched aquarium data is printed and returned as a list of 
	 * AcquarioType objects.
	 * 
	 * @return a list of AcquarioType objects containing the fetched aquarium data.
	 * @throws Exception if there's an issue with constructing the query string or fetching 
	 * data from the API.
	 */
	private List<AcquarioType> getAcquariList() throws Exception{
		StringBuilder queryStringBuilder = new StringBuilder("crud=r&table=acquari");
		String queryString = queryStringBuilder.toString();
		System.out.println(queryString);
		AcquariType acquariData = (AcquariType) requester.fetchDataFromApi(queryString);
		System.out.println(acquariData.getItem().toString());
		return acquariData.getItem();
	}
	
	/**
	 * Displays the details of a selected aquarium.
	 * 
	 * This method resets the view to its initial state and retrieves the selected aquarium 
	 * from the view. Based on the selected aquarium, it constructs a query string to fetch 
	 * associated plant-aquarium data. After fetching the data, it extracts the quantities of 
	 * plants associated with the aquarium and then fetches the details of these plants from 
	 * the database. Finally, it displays the selected aquarium along with the associated 
	 * plants and their quantities on the view.
	 * 
	 * @throws Exception if there's an issue with resetting the view, constructing the query 
	 * string, fetching data from the API, or processing the retrieved data.
	 */
	private void viewAcquario() throws Exception{
		w.resetViewAndNew();
		AcquarioType selectedAcquario = w.getSelectedItemListAcquari();
		
		// Costruisci la query string in base ai valori ottenuti dai metodi
	    StringBuilder queryStringBuilder = new StringBuilder("crud=r&table=piante_acquari");
		
	    queryStringBuilder.append("&id_acquario=").append(URLEncoder.encode(Long.toString(selectedAcquario.getIdAcquario()), StandardCharsets.UTF_8.toString()));
	    
	    String queryString = queryStringBuilder.toString();
	    System.out.println(queryString);
	    PianteAcquariType pianteAcquariData = (PianteAcquariType) requester.fetchDataFromApi(queryString);
	    System.out.println(pianteAcquariData.getItem().toString());
	    
	    //ora devo fare un metodo sulla classe del model che da questa lista prende le pk di piante e fa n richieste al database e mette insieme le risposte restituendo una lista tipo PiantaType
	    List<Long> quantitas= new ArrayList<Long>();
	    
	    for(PiantaAcquarioType pa : pianteAcquariData.getItem()) {
	    	quantitas.add(pa.getQuantita());
	    }
	    
	    // Esegui le richieste per ottenere i dettagli delle piante
	    List<PiantaType> pianteForAcquario = requester.fetchPianteForAcquario(pianteAcquariData.getItem());
	    
	   
		w.viewSelectedAcquario(pianteForAcquario, quantitas);
		
	}
	
	/**
	 * Saves a new aquarium or updates an existing one.
	 * 
	 * This method retrieves the details of the aquarium to be saved from the view, 
	 * constructs an `AcquariType` object with the provided details, and sends this 
	 * object to the API to either create a new aquarium or update an existing one. 
	 * After saving the aquarium, it displays a message dialog with the response 
	 * received from the API. Additionally, it resets the view to its initial state 
	 * and updates the list of aquariums displayed on the view.
	 * 
	 * @throws Exception if there's an issue with retrieving the aquarium details 
	 * from the view, constructing the `AcquariType` object, sending data to the 
	 * API, or updating the view with the new list of aquariums.
	 */
	private void salvaAcquario() throws Exception{
		//w.resetViewAndNew();
		Long idAcquario = new Long(0);
		Long litraggio = w.getValueSpinnerLitraggio();
		Long larghezza = w.getValueSpinnerLarghezza();
		Long lunghezza = w.getValueSpinnerLunghezza();
		Long altezza = w.getValueSpinnerAltezza();
		String descrizione = w.getTextAreaDescrizione();
		
		AcquariType acquarioToSave = requester.createObjectAcquariTypeSolo(idAcquario, litraggio, larghezza, lunghezza, altezza, descrizione);
		
		System.out.println(acquarioToSave.getItem().toString());
		
		String echo = requester.sendDataToApi(acquarioToSave);
		w.messageDialog(echo);
		w.resetViewAndNew();
		w.updateListAcquari(getAcquariList());
	}
	
	/**
	 * Deletes an aquarium from the database.
	 * 
	 * This method retrieves the selected aquarium's ID from the view, constructs 
	 * a query string for deleting the aquarium based on the ID, and sends this query 
	 * to the API to delete the corresponding aquarium from the database. After 
	 * deleting the aquarium, it displays a message dialog with the response received 
	 * from the API. Additionally, it updates the view by refreshing the list of 
	 * aquariums displayed.
	 * 
	 * @throws Exception if there's an issue with retrieving the selected aquarium's 
	 * ID from the view, constructing the query string, sending data to the API, or 
	 * updating the view with the new list of aquariums.
	 */
	private void cancellaAcquario() throws Exception{
		Long idAcquarioToDelete = w.getSelectedItemListAcquari().getIdAcquario();
		
		StringBuilder queryStringBuilder = new StringBuilder("crud=d&table=acquari");
		queryStringBuilder.append("&id_acquario=").append(URLEncoder.encode(Long.toString(idAcquarioToDelete), StandardCharsets.UTF_8.toString()));
		String queryString = queryStringBuilder.toString();
		System.out.println(queryString);
		
		String echo = (String) requester.fetchDataFromApi(queryString);
		w.messageDialog(echo);
		w.updateListAcquari(this.getAcquariList());
	}
	
	
	/**
	 * Saves selected plants to an aquarium.
	 * 
	 * This method retrieves the indexes of selected plants from the view, the ID 
	 * of the selected aquarium from a combo box, and the quantities of the selected 
	 * plants from spinners in the view. It constructs an object representing the 
	 * plants to be saved to the aquarium, sends this object to the API to save the 
	 * data, and displays a message dialog with the response received from the API. 
	 * Additionally, it updates the view by refreshing the list of aquariums displayed.
	 * 
	 * @throws Exception if there's an issue with retrieving the selected plants' 
	 * indexes, retrieving the ID of the selected aquarium, getting the ID of plants 
	 * from the view, getting the quantities of plants from the view, removing items 
	 * from the view's cart, sending data to the API, or updating the view with the 
	 * new list of aquariums.
	 */
	private void salvaPiante() throws Exception{
		int[] indexesOfPlantsToSave = w.getSelectedCheckBoxIndices();
		if(indexesOfPlantsToSave.length==0)
			throw new Exception("Attenzione: selezionare almeno una pianta all'interno del carrello");
		Long idAcquario = w.getIdOfAcquarioSelectedInComboBoxSalvaAcquario();
		Long[] idsPianta = new Long[indexesOfPlantsToSave.length];
		Long[]  quantitas = new Long[indexesOfPlantsToSave.length];
		
		for(int i=0; i<indexesOfPlantsToSave.length;i++) {
			idsPianta[i] = w.getIdOfPiantaListaCarrello(indexesOfPlantsToSave[i]);
			quantitas[i] = w.getValueOfSpinnerListaCarrello(indexesOfPlantsToSave[i]);
		}
		for(int i=indexesOfPlantsToSave.length-1; i>=0;i--) {
			w.removeItemFromListaCarrello(indexesOfPlantsToSave[i]);
		}
		
		PianteAcquariType pianteToSave = requester.createObjectPianteAcquariTypeMulti(idsPianta, quantitas, idAcquario);
		
		String echo = requester.sendDataToApi(pianteToSave);
		w.messageDialog(echo);
		w.updateListAcquari(this.getAcquariList());
	}
	
	/**
	 * Deletes a plant from an aquarium.
	 * 
	 * This method retrieves the ID of the selected aquarium and the ID of the 
	 * selected plant from the view. It constructs a query string to specify the 
	 * deletion of the selected plant from the selected aquarium, sends this query 
	 * string to the API to delete the data, displays a message dialog with the 
	 * response received from the API, and refreshes the view by calling the 
	 * {@code viewAcquario} method to display the updated list of plants in the 
	 * selected aquarium.
	 * 
	 * @throws Exception if there's an issue with retrieving the ID of the selected 
	 * aquarium, retrieving the ID of the selected plant, constructing the query 
	 * string, sending data to the API, displaying the message dialog, or refreshing 
	 * the view with the updated list of plants in the selected aquarium.
	 */
	private void cancellaPiantaDaAcquario() throws Exception{
		
		Long idAcquario = w.getSelectedItemListAcquari().getIdAcquario();
		Long idPianta = w.getSelectedItemOfListPlantsOfAcquario().getIdPianta();
		
		StringBuilder queryStringBuilder = new StringBuilder("crud=d&table=piante_acquari");
		
		queryStringBuilder.append("&id_acquario=").append(URLEncoder.encode(Long.toString(idAcquario), StandardCharsets.UTF_8.toString()));
		queryStringBuilder.append("&id_pianta=").append(URLEncoder.encode(Long.toString(idPianta), StandardCharsets.UTF_8.toString()));
		
		String queryString = queryStringBuilder.toString();
		System.out.println(queryString);
		
		String echo = (String) requester.fetchDataFromApi(queryString);
		w.messageDialog(echo);
		this.viewAcquario();
		
	}
	
	@Override
	public void mouseClicked(MouseEvent e){
		
	    
	    if (e.isAltDown() && e.getButton() == MouseEvent.BUTTON1 && e.getSource() == w.getListCercaPiante()) {
            // Ottieni l'indice dell'elemento cliccato
            int index = w.getIndexOfElemenListCercaPiantaForMouseClick(e.getPoint());
            //index++;
            // Verifica se l'indice è valido
            if (index != -1) {
            	try {
            		
            	    PiantaType pianta = w.getPiantaAltClickedInListCerca(index);
            	    if (pianta != null) {
            	        showImageForPianta(pianta);
            	        
            	    }
            	} catch (IndexOutOfBoundsException e1) {
            	    // ...
            	} catch (Exception e1) {
            	    // ...
            	}
            }
        }
	    //idem co patate ma attento che devi farti i metodi anche per questa lista arrayListViewPianteForAcquario 
        if (e.isAltDown() && e.getButton() == MouseEvent.BUTTON1 && e.getSource() == w.getListViewPianteAcquario()) {
            // Ottieni l'indice dell'elemento cliccato
            int index = w.getIndexOfElemenListViewPianteAcquarioForMouseClick(e.getPoint());
            
            // Verifica se l'indice è valido
            if (index != -1) {
            	try {
            		
            	    PiantaType pianta = w.getPiantaAltClickInPianteForAcquario(index);
            	    if (pianta != null) {
            	        showImageForPianta(pianta);
            	        
            	    }
            	} catch (IndexOutOfBoundsException e1) {
            	    // ...
            	} catch (Exception e1) {
            	    // ...
            	}
            }
        }
        
        
	}
	
	
	/**
	 * Displays an image for a specific plant.
	 * 
	 * This method constructs a query string to fetch the image associated with the 
	 * provided plant ID from the API. It retrieves the image data from the API 
	 * response, checks if the retrieved image data list is empty, converts the 
	 * byte array of the image to an actual image, retrieves the link and name of 
	 * the plant, and displays the image along with the plant's name and link using 
	 * the {@code displayPlantImage} method from the view.
	 * 
	 * @param pianta the plant for which the image needs to be displayed.
	 * 
	 * @throws Exception if there's an issue with constructing the query string, 
	 * fetching data from the API, checking for an empty image data list, converting 
	 * the byte array to an image, or displaying the image along with the plant's 
	 * name and link.
	 */
	private void showImageForPianta(PiantaType pianta) throws Exception {

	    // Costruisci la query string
	    StringBuilder queryStringBuilder = new StringBuilder("crud=r&table=immagini");
	    //queryStringBuilder.append("&id_pianta=2");
	    queryStringBuilder.append("&id_pianta=").append(URLEncoder.encode(Long.toString(pianta.getIdPianta()), StandardCharsets.UTF_8.toString()));
	    String queryString = queryStringBuilder.toString();
	    System.out.println(queryString);

	    // Recupera l'immagine
	    ImmaginiType imageToShow = (ImmaginiType) requester.fetchDataFromApi(queryString);

	    // Gestisci il caso di lista vuota
	    if (imageToShow.getItem().isEmpty()) {
	        throw new Exception("Nessuna immagine trovata per la pianta");
	    }

	    // Ottieni l'array di byte dell'immagine
	    byte[] imageBytes = imageToShow.getItem().get(0).getImmaginePianta();
	    // Converti l'array di byte in un'immagine
	    
	    
	    
	    
	    String link=pianta.getLinkPagina();
	    String nomePianta=pianta.getNome();
	    //da controllare che funzioni
	    try {
			w.displayPlantImage(nomePianta, RestEasyPlantsClient.convertToImage(imageBytes), link);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	




	
	




	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	//keylistener
	
	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyPressed(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		if (e.getKeyCode() == KeyEvent.VK_ESCAPE && e.getSource() == w.getListAcquari()) {
            w.clearSelectionListAcquari();
            w.resetViewAndNew();
        }
		if (e.getKeyCode() == KeyEvent.VK_ESCAPE && e.getSource() == w.getListCercaPiante()) {
            w.clearSelectionListCercaPiante();
        }
		if (e.getKeyCode() == KeyEvent.VK_ESCAPE && e.getSource() == w.getListViewPianteAcquario()) {
            w.clearSelectionListViewPianteAcquario();
        }
	}
	
	
	
}