package control;

import java.awt.BorderLayout;
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
import javax.swing.JEditorPane;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
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
	
	public Controller(Window w) throws Exception {
		this.w= w;
		this.w.registerEvent(this);
		this.requester= new RestEasyPlantsClient();
		w.updateListAcquari(this.getAcquariList());
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		try
		{
			if(e.getSource() == w.getBtnAcquari())
			{
				w.showPanel("cardLayout", "panelAcquari");
				w.resetViewAndNew();
				//questo sotto lo fai solo nel COSTRUTTORE e nel bottone salva nuovo acquario
				//metodo che ti ritorna un List di AcquarioType facendo la richiesta in get con jaxb
				//List<AcquarioType> tmp = this.getAcquariList();
				//metodo che updeita la arrayListAcquari e che riupdeita la combo box e la list acquari nella card acquari id+litri display
				//w.updateListAcquari(tmp);
			}
			if(e.getSource() == w.getBtnCerca())
			{
				w.showPanel("cardLayout", "panelCerca");
			}
			if(e.getSource() == w.getBtnSalva())
			{
				w.showPanel("cardLayout", "panelSalva");
				//questo sotto lo fai solo nel COSTRUTTORE e nel bottone salva nuovo acquario
				//metodo che ti ritorna un List di AcquarioType facendo la richiesta in get con jaxb
				//List<AcquarioType> tmp = this.getAcquariList();
				//metodo che updeita la arrayListAcquari e che riupdeita la combo box e la list acquari nella card acquari id+litri display
				//w.updateListAcquari(tmp);
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
				
			}
			
			
			if(e.getSource() == w.getBtnCercaPianta())
			{
				/*List<PiantaType> prova = new ArrayList<PiantaType>();
			    prova.add(new PiantaType() {
			    	{
			    		setNome("lollo");
			    		setIdPianta(3);
			    	}
			    });
			    w.addItemsToListCercaPiante(prova);*/
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
				/*int[] tmp = w.getSelectedCheckBoxIndices();
				System.out.println(Arrays.toString(tmp));
				System.out.println(w.getValueOfSpinnerListaCarrello(tmp[0]));
				System.out.println(w.getIdOfPiantaListaCarrello(tmp[0]));*/
				this.salvaPiante();
			}
		}
		catch(Exception e1) {
			w.messageDialog(e1.getMessage());
		}
	}

	

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

	private List<AcquarioType> getAcquariList() throws Exception{
		StringBuilder queryStringBuilder = new StringBuilder("crud=r&table=acquari");
		String queryString = queryStringBuilder.toString();
		System.out.println(queryString);
		AcquariType acquariData = (AcquariType) requester.fetchDataFromApi(queryString);
		System.out.println(acquariData.getItem().toString());
		return acquariData.getItem();
	}
	
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
	
	private void salvaPiante() throws Exception{
		int[] indexesOfPlantsToSave = w.getSelectedCheckBoxIndices();
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
            	        // ... esegui il codice con la variabile "pianta" e accedi alle sue proprietà
            	        showImageForPianta(pianta);
            	        
            	    }
            	} catch (IndexOutOfBoundsException e1) {
            	    // ...
            	} catch (Exception e1) {
            	    // ...
            	}

                // Apri una nuova finestra Java e mostra l'indice
                //w.messageDialog("trovato a indice "+ index);;
            }
        }
	    //idem co patate ma attento che devi farti i metodi anche per questa lista arrayListViewPianteForAcquario 
        if (e.isAltDown() && e.getButton() == MouseEvent.BUTTON1 && e.getSource() == w.getListViewPianteAcquario()) {
            // Ottieni l'indice dell'elemento cliccato
            int index = w.getIndexOfElemenListViewPianteAcquarioForMouseClick(e.getPoint());
            
            // Verifica se l'indice è valido
            if (index != -1) {
                // Apri una nuova finestra Java e mostra l'indice
                //w.messageDialog("trovato a indice "+ index);;
            }
        }
	}
	
	
	
	public void showImageForPianta(PiantaType pianta) throws Exception {

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
	    BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(imageBytes));
	    // Visualizza l'immagine
	    ImageIcon imageIcon = new ImageIcon(bufferedImage);
	    JLabel label = new JLabel(imageIcon);
	    
	    
	    String link=pianta.getLinkPagina();
	    String nomePianta=pianta.getNome();
	    //da controllare che funzioni
	    try {
			displayPlantImage(nomePianta, imageIcon, link);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static Image convertToImage(byte[] imageBytes) throws IOException {
	    ByteArrayInputStream bais = new ByteArrayInputStream(imageBytes);
	    BufferedImage image = ImageIO.read(bais);
	    bais.close();
	    return image;
	}




	
	private void displayPlantImage(String nomePianta, ImageIcon immagine, String link) {
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
