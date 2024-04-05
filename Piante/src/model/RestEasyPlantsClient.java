package model;

import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;
import piante.AcquariType;
import piante.AcquarioType;
import piante.ImmaginiType;
import piante.LuceCO2Type;
import piante.PiantaAcquarioType;
import piante.PiantaType;
import piante.PianteAcquariType;
import piante.PianteType;
import piante.TassoCrescitaType;

public class RestEasyPlantsClient {

	private static final String API_URL = "http://localhost/PIANTE/restEasy.php";
	
	public Object fetchDataFromApi(String queryString) throws JAXBException, Exception{
        // Estrai i parametri e la tabella dalla query string
        Map<String, String> params = extractParameters(queryString);
        String table = params.get("table");
        String crud = params.get("crud");
        
        
        
       
        
        try {
            // Costruisci l'URL della richiesta GET con i parametri codificati
            URL url = new URL(API_URL + "?" + queryString);
            InputStream input = url.openStream();
            
            
            
            // Decidi il tipo di classe JAXB da utilizzare per la deserializzazione in base alla tabella
            Class<?> responseClass;
            
            switch (table.toLowerCase()) {
                case "piante":
                    responseClass = PianteType.class;
                    break;
                case "acquari":
                    responseClass = AcquariType.class;
                    break;
                case "immagini":
                    responseClass = ImmaginiType.class;
                    break;
                case "piante_acquari":
                    responseClass = PianteAcquariType.class;
                    break;
                default:
                    throw new IllegalArgumentException("Tabella non supportata: " + table);
            }
            
            // Deserializza la risposta usando JAXB
            JAXBContext jaxbContext = JAXBContext.newInstance(responseClass);
            Unmarshaller jaxbUnmarshaller = jaxbContext.createUnmarshaller();
            
            if(crud.equals("d"))
            {
            	byte[] bytes = input.readAllBytes();
                String message = new String(bytes);
                
                return message;
            }
            	
            
            return jaxbUnmarshaller.unmarshal(input);
            
        } catch (Exception e) {
            e.printStackTrace();
            throw new JAXBException("Errore durante la richiesta e la deserializzazione dei dati", e);
        }
    }
    
	public String sendDataToApi(Object obj) throws Exception {
		
		// Decidi il tipo di classe JAXB da utilizzare per la deserializzazione in base alla tabella
        Class<?> requestClass ;
		if(obj instanceof PianteAcquariType)
		{
			requestClass = PianteAcquariType.class;
			
		}else if(obj instanceof AcquariType)
		{
			requestClass = AcquariType.class;
		}else
		{
			throw new Exception("Errore, classe non supportata");
		}
		
		
		JAXBContext context = JAXBContext.newInstance(requestClass);
		Marshaller marshaller= context.createMarshaller();
		marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
		
		// Convertire l'oggetto in XML e ottenere i dati come array di byte
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        marshaller.marshal(requestClass.cast(obj), byteArrayOutputStream);
        
        
     // Convertire i dati in una stringa
        String xmlString = new String(byteArrayOutputStream.toByteArray(), "UTF-8");

        // Creare una connessione HTTP
        URL url = new URL(API_URL);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setDoOutput(true);

        // Invia l'XML come corpo della richiesta
        OutputStream out = connection.getOutputStream();
        out.write(xmlString.getBytes("UTF-8"));
        out.close();

     // Leggere la risposta (se necessario)
        InputStream in = connection.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(in));

        String line;
        String echo="";
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
            echo=echo.concat(line+"\n");
        }

        reader.close();
        in.close();
        
      
        connection.disconnect();
   
        return echo;
	}
	
	public List<PiantaType> fetchPianteForAcquario(List<PiantaAcquarioType> piantaAcquarioList) throws JAXBException, Exception {
	    List<PiantaType> pianteForAcquarioList = new ArrayList<PiantaType>();

	    // Per ogni elemento PianteAcquariType nella lista, esegui una richiesta API
	    for (PiantaAcquarioType piantaAcquario : piantaAcquarioList) {
	        Long idPianta = piantaAcquario.getIdPianta(); // Assumendo che esista un metodo getIdPianta() in PianteAcquariType

	        StringBuilder queryStringBuilder = new StringBuilder("crud=r&table=piante");
	        queryStringBuilder.append("&id_pianta=").append(URLEncoder.encode(Long.toString(idPianta), StandardCharsets.UTF_8.toString()));

	        String queryString = queryStringBuilder.toString();

	        
            // Esegui la richiesta e ottieni i dettagli della pianta
            PianteType piantaData = (PianteType) this.fetchDataFromApi(queryString);
            System.out.println(piantaData.getItem());
            if (piantaData != null) {
                pianteForAcquarioList.addAll(piantaData.getItem());
            }

	        
	    }

	    return pianteForAcquarioList;
	}

	public PianteAcquariType createObjectPianteAcquariTypeMulti(Long[] idsPianta, Long[] quantitas, Long idAcquario) throws Exception {
	    if (idsPianta == null || quantitas == null || idsPianta.length != quantitas.length)
	        throw new IllegalArgumentException("Gli array idsPianta e quantitas devono avere la stessa lunghezza e non possono essere nulli");
	    

	    PianteAcquariType pianteAcquariDataResult = new PianteAcquariType();

	    for (int i = 0; i < idsPianta.length; i++) {
	        PiantaAcquarioType piantaAcquario = new PiantaAcquarioType();
	        
	        piantaAcquario.setIdPianta(idsPianta[i]);
	        piantaAcquario.setQuantita(quantitas[i]);
	        piantaAcquario.setIdAcquario(idAcquario);  // Imposta l'idAcquario su tutti gli oggetti PiantaAcquarioType
	        
	        pianteAcquariDataResult.getItem().add(piantaAcquario);
	    }

	    return pianteAcquariDataResult;
	}
	
	public AcquariType createObjectAcquariTypeSolo(long idAcquario, long litri, long larghezza, long lunghezza, long altezza, String descrizione) throws Exception {
	    AcquariType acquariTypeResult = new AcquariType();
	    AcquarioType acquario = new AcquarioType();
	    
	    acquario.setIdAcquario(idAcquario);
	    acquario.setLitri(litri);
	    acquario.setLarghezza(larghezza);
	    acquario.setLunghezza(lunghezza);
	    acquario.setAltezza(altezza);
	    acquario.setDescrizione(descrizione);
	    
	    acquariTypeResult.getItem().add(acquario);

	    return acquariTypeResult;
	}


	public static ImageIcon convertToImage(byte[] imageBytes) throws IOException {
		BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(imageBytes));
	    // Visualizza l'immagine
	    ImageIcon imageIcon = new ImageIcon(bufferedImage);
		
	    return imageIcon;
	}
	
    private Map<String, String> extractParameters(String queryString) throws Exception{
        Map<String, String> params = new HashMap<>();
        String[] keyValuePairs = queryString.split("&");
        
        for (String pair : keyValuePairs) {
            String[] entry = pair.split("=");
            if (entry.length == 2) {
                params.put(entry[0], entry[1]);
            }
        }
        
        return params;
    }
}
