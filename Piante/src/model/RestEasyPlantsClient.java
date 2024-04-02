package model;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;
import piante.AcquariType;
import piante.ImmaginiType;
import piante.LuceCO2Type;
import piante.PiantaType;
import piante.PianteAcquariType;
import piante.PianteType;
import piante.TassoCrescitaType;

public class RestEasyPlantsClient {

	private static final String API_URL = "http://localhost/PIANTE/restEasy.php";
	
	public Object fetchDataFromApi(String queryString) throws JAXBException {
        // Estrai i parametri e la tabella dalla query string
        Map<String, String> params = extractParameters(queryString);
        String table = params.get("table");
        
        
        
       
        
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
            
            return jaxbUnmarshaller.unmarshal(input);
            
        } catch (Exception e) {
            e.printStackTrace();
            throw new JAXBException("Errore durante la richiesta e la deserializzazione dei dati", e);
        }
    }
    
	public void sendDataToApi(Object obj) throws Exception {
		
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
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }

        reader.close();
        in.close();


        connection.disconnect();
        
	}
	
    private Map<String, String> extractParameters(String queryString) {
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
