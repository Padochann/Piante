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
	
	
	/**
	 * Fetches data from the API based on the provided query string.
	 * 
	 * This method extracts parameters and the table name from the provided 
	 * query string, constructs a GET request URL with the encoded parameters, 
	 * retrieves the data from the API, determines the JAXB class to use for 
	 * deserialization based on the table name, and deserializes the API response 
	 * using JAXB. If the CRUD operation is 'd' (delete), it reads all bytes from 
	 * the input stream and returns the resulting message as a string. 
	 * 
	 * @param queryString the query string containing the CRUD operation, table name, 
	 * and parameters for the API request.
	 * 
	 * @return the deserialized object representing the API response, or a string 
	 * message if the CRUD operation is 'd' (delete).
	 * 
	 * @throws JAXBException if there's an issue with the JAXB context or unmarshalling 
	 * the API response.
	 * @throws Exception if there's an issue with extracting parameters from the 
	 * query string, constructing the GET request URL, opening the input stream, 
	 * or reading bytes from the input stream.
	 * @throws IllegalArgumentException if the table name extracted from the query 
	 * string is not supported.
	 */
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
    
	/**
	 * Sends the provided object to the API using a POST request.
	 * 
	 * This method determines the JAXB class to use for marshalling the object 
	 * into XML based on its type. It then marshals the object into XML, converts 
	 * the XML data into a string, creates an HTTP connection to the API, sends 
	 * the XML string as the body of the POST request, reads the response from the 
	 * API, and returns the response as a string.
	 * 
	 * @param obj the object to send to the API.
	 * 
	 * @return the response from the API as a string.
	 * 
	 * @throws Exception if there's an issue with determining the JAXB class, 
	 * creating the JAXB context, marshalling the object into XML, opening the 
	 * connection to the API, sending data to the API, reading the response 
	 * from the API, or disconnecting the connection.
	 */
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
	
	/**
	 * Fetches plant details for a list of plants associated with an aquarium.
	 * 
	 * This method takes a list of PiantaAcquarioType objects, retrieves the 
	 * plant IDs from each object, constructs a query string for each plant ID, 
	 * executes an API request for each query string to fetch the plant details, 
	 * and adds the fetched plant details to a list of PiantaType objects. 
	 * The list of PiantaType objects is then returned.
	 * 
	 * @param piantaAcquarioList the list of PiantaAcquarioType objects 
	 *                           containing plant IDs for which details need 
	 *                           to be fetched.
	 * 
	 * @return the list of PiantaType objects containing the fetched plant details.
	 * 
	 * @throws JAXBException if there's an issue with the JAXB context or 
	 *                       unmarshalling the XML response.
	 * 
	 * @throws Exception if there's an issue with constructing the query string, 
	 *                   executing the API request, or processing the response.
	 */
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

	/**
	 * Creates a PianteAcquariType object with multiple PiantaAcquarioType items.
	 * 
	 * This method takes arrays of plant IDs and quantities, along with an aquarium ID. 
	 * It creates a new PiantaAcquarioType object for each pair of plant ID and quantity, 
	 * sets the properties for each object, and adds them to a PianteAcquariType object. 
	 * The resulting PianteAcquariType object with the populated list of 
	 * PiantaAcquarioType items is then returned.
	 * 
	 * @param idsPianta the array of plant IDs.
	 * @param quantitas the array of quantities corresponding to the plant IDs.
	 * @param idAcquario the ID of the aquarium to which the plants belong.
	 * 
	 * @return the PianteAcquariType object populated with PiantaAcquarioType items.
	 * 
	 * @throws IllegalArgumentException if the arrays idsPianta and quantitas are null, 
	 *                                  or if their lengths do not match.
	 * 
	 * @throws Exception if there's an issue with creating or setting the 
	 *                   properties of the PiantaAcquarioType objects.
	 */
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
	
	/**
	 * Creates an AcquariType object with a single AcquarioType item.
	 * 
	 * This method constructs an AcquarioType object with the provided parameters, 
	 * sets the properties for the object, and adds it to an AcquariType object. 
	 * The resulting AcquariType object with the populated AcquarioType item 
	 * is then returned.
	 * 
	 * @param idAcquario the ID of the aquarium.
	 * @param litri the capacity of the aquarium in liters.
	 * @param larghezza the width of the aquarium.
	 * @param lunghezza the length of the aquarium.
	 * @param altezza the height of the aquarium.
	 * @param descrizione the description or details of the aquarium.
	 * 
	 * @return the AcquariType object populated with the AcquarioType item.
	 * 
	 * @throws Exception if there's an issue with creating or setting the 
	 *                   properties of the AcquarioType object.
	 */
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

	/**
	 * Converts a byte array representing an image into an ImageIcon.
	 * 
	 * This method reads the byte array as an image using the ImageIO class, 
	 * creates a BufferedImage, and then constructs an ImageIcon from it. 
	 * The resulting ImageIcon can be used to display the image in a GUI component.
	 * 
	 * @param imageBytes the byte array representing the image data.
	 * 
	 * @return an ImageIcon object containing the image.
	 * 
	 * @throws IOException if there's an issue reading the image data from the byte array.
	 */
	public static ImageIcon convertToImage(byte[] imageBytes) throws IOException {
		BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(imageBytes));
	    // Visualizza l'immagine
	    ImageIcon imageIcon = new ImageIcon(bufferedImage);
		
	    return imageIcon;
	}
	
	/**
	 * Extracts key-value pairs from a given query string and stores them in a Map.
	 * 
	 * This method takes a query string as input, splits it into individual key-value pairs 
	 * separated by '&', and then further splits each pair by '=' to extract the key and value.
	 * The extracted key-value pairs are stored in a Map and returned.
	 * 
	 * @param queryString the input query string containing key-value pairs separated by '&'.
	 * 
	 * @return a Map containing the extracted key-value pairs.
	 * 
	 * @throws Exception if there's an issue parsing the query string or if the format is incorrect.
	 */
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
