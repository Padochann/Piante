package control;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.event.AncestorEvent;
import javax.swing.event.AncestorListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import model.RestEasyPlantsClient;
import piante.AcquariType;
import piante.AcquarioType;
import piante.PiantaAcquarioType;
import piante.PiantaType;
import piante.PianteAcquariType;
import piante.PianteType;
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
				List<AcquarioType> tmp = this.getAcquariList();
				//metodo che updeita la arrayListAcquari e che riupdeita la combo box e la list acquari nella card acquari id+litri display
				w.updateListAcquari(tmp);
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
				List<AcquarioType> tmp = this.getAcquariList();
				//metodo che updeita la arrayListAcquari e che riupdeita la combo box e la list acquari nella card acquari id+litri display
				w.updateListAcquari(tmp);
			}
			if(e.getSource() == w.getBtnView())
			{
				w.showPanel("acquarioLayout", "panelView");
				
				this.viewAcquario();
			}
			if(e.getSource() == w.getBtnNew())
			{
				w.showPanel("acquarioLayout", "panelNew");
			}
			
			
			if(e.getSource() == w.getBtnDelete())
			{
				this.cancellaAcquario();
			}
			if(e.getSource() == w.getBtnSalvaNewAcquario())
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
	
	private void cancellaAcquario() throws Exception{
		Long idAcquarioToDelete = w.getSelectedItemListAcquari().getIdAcquario();
		
		StringBuilder queryStringBuilder = new StringBuilder("crud=d&table=acquari");
		queryStringBuilder.append("&id_acquario=").append(URLEncoder.encode(Long.toString(idAcquarioToDelete), StandardCharsets.UTF_8.toString()));
		String queryString = queryStringBuilder.toString();
		System.out.println(queryString);
		
		String echo = (String) requester.fetchDataFromApi(queryString);
		w.updateListAcquari(this.getAcquariList());
		w.messageDialog(echo);
	}
	
	private void salvaPiante() throws Exception{
		int[] indexesOfPlantsToSave = w.getSelectedCheckBoxIndices();
		Long idAcquario = w.getIdOfAcquarioSelectedInComboBoxSalvaAcquario();
		Long[] idsPianta = new Long[indexesOfPlantsToSave.length];
		Long[]  quantitas = new Long[indexesOfPlantsToSave.length];
		
		for(int i=0; i<indexesOfPlantsToSave.length;i++) {
			idsPianta[i] = w.getIdOfPiantaListaCarrello(i);
			quantitas[i] = w.getValueOfSpinnerListaCarrello(i);
		}
		
		PianteAcquariType pianteToSave = requester.createObjectPianteAcquariTypeMulti(idsPianta, quantitas, idAcquario);
		
		String echo = requester.sendDataToApi(pianteToSave);
		w.messageDialog(echo);
	}
	
	@Override
	public void mouseClicked(MouseEvent e) {
	    if (e.isAltDown() && e.getButton() == MouseEvent.BUTTON1) {
	        if (e.getSource() == w.getListCercaPiante()) {
	            int index = w.getIndexOfElemenListCercaPiantaForMouseClick(e.getPoint());
	            if (index != -1) {
	                // Simula il percorso del file immagine sul tuo computer
	            	System.out.println("l'indice è:" + index);
	                String imageFilePath = "images\\1.jpg";
	                displayPlantImage(imageFilePath);
	            }
	        } else if (e.getSource() == w.getListViewPianteAcquario()) {
	            int index = w.getIndexOfElemenListViewPianteAcquarioForMouseClick(e.getPoint());
	            if (index != -1) {
	                // Simula il percorso del file immagine sul tuo computer
	            	System.out.println("l'indice è:" + index);
	            	String imageFilePath = "images\\1.jpg";
	                displayPlantImage(imageFilePath);
	            }
	        }
	    }
	}

	// Metodo per visualizzare l'immagine in una nuova finestra
	private void displayPlantImage(String imageFilePath) {
	    ImageIcon plantIcon = new ImageIcon(imageFilePath);
	    JLabel imageLabel = new JLabel(plantIcon);

	    JFrame imageFrame = new JFrame("Immagine Pianta Selezionata");
	    imageFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	    imageFrame.add(imageLabel);
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
        }
		if (e.getKeyCode() == KeyEvent.VK_ESCAPE && e.getSource() == w.getListCercaPiante()) {
            w.clearSelectionListCercaPiante();
        }
		if (e.getKeyCode() == KeyEvent.VK_ESCAPE && e.getSource() == w.getListViewPianteAcquario()) {
            w.clearSelectionListViewPianteAcquario();
        }
	}
	
	
	
}
