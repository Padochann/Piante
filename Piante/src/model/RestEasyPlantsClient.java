package model;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
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
