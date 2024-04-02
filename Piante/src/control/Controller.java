package control;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

import javax.swing.event.AncestorEvent;
import javax.swing.event.AncestorListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import model.RestEasyPlantsClient;
import piante.AcquarioType;
import piante.PiantaType;
import piante.PianteType;
import view.Window;

public class Controller implements ActionListener, MouseListener{
	
	private Window w;
	private RestEasyPlantsClient requester;
	
	public Controller(Window w) {
		this.w= w;
		this.w.registerEvent(this);
		this.requester= new RestEasyPlantsClient();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		try
		{
			if(e.getSource() == w.getBtnAcquari())
			{
				w.showPanel("cardLayout", "panelAcquari");
			}
			if(e.getSource() == w.getBtnCerca())
			{
				w.showPanel("cardLayout", "panelCerca");
			}
			if(e.getSource() == w.getBtnSalva())
			{
				w.showPanel("cardLayout", "panelSalva");
				//metodo che ti ritorna un List di AcquarioType facendo la richiesta in get con jaxb
				//metodo che updeita la arrayListAcquari e che riupdeita la combo box e la list acquari nella card acquari id+litri display
			}
			if(e.getSource() == w.getBtnView())
			{
				w.showPanel("acquarioLayout", "panelView");
			}
			if(e.getSource() == w.getBtnNew())
			{
				w.showPanel("acquarioLayout", "panelNew");
			}
			
			
			if(e.getSource() == w.getBtnDelete())
			{
			
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
		
		
		return null;
	}
	
	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		// Verifica se il tasto CTRL è premuto
        if (e.isAltDown() && e.getButton() == MouseEvent.BUTTON1) {
            // Ottieni l'indice dell'elemento cliccato
            int index = w.getIndexOfElemenListCercaPiantaForMouseClick(e.getPoint());
            
            // Verifica se l'indice è valido
            if (index != -1) {
                // Apri una nuova finestra Java e mostra l'indice
                w.messageDialog("trovato a indice "+ index);;
            }
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
	
}
