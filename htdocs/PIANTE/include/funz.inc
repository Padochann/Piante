<?php
    function prova(){
        echo "prova";
    }

    
    /**
     * Generates an XML document from a result set.
     *
     * @param mixed $resultSet The result set to generate XML from.
     * @param string $xsdPath The path to the XSD file for validation.
     * @param string $rootTagName The root tag name for the XML document.
     * @param string $namespace The namespace for the XML document.
     * @return void
     */
    function generateXmlFromResultSet($resultSet, $xsdPath, $rootTagName, $namespace) {
        $xmlWriter = new XMLWriter();
        $xmlWriter->openMemory();
        $xmlWriter->setIndent(true);
        $xmlWriter->startDocument('1.0', 'UTF-8');
        
        $xmlWriter->startElement($rootTagName);
        
        // Imposta lo schema XSD
        $xmlWriter->writeAttribute('xmlns', $namespace);
        
        while ($row = $resultSet->fetch_assoc()) {
            $xmlWriter->startElement('item');
            
            foreach ($row as $key => $value) {
                $xmlWriter->startElement($key);
        
                // Se il valore è un BLOB, converte in base64
                if ($key === 'immagine_pianta') {
                    $value = base64_encode($value);
                }
        
                $xmlWriter->text($value);
                $xmlWriter->endElement();
            }
            
            $xmlWriter->endElement();
        }
        
        $xmlWriter->endElement(); // Chiudi il tag radice
        $xmlWriter->endDocument();
        
        return $xmlWriter->outputMemory();
    }

    /**
     * Creates a query for performing CRUD operations on a specified table.
     *
     * @param string $crud The type of operation to perform (create, read, update, delete) implemented only r(read) and d(delete) mandatory field.
     * @param string $table The name of the table to perform the operation on, mandatory field.
     * @param string $nome The name of the plant.
     * @param string $origine The origin of the plant.
     * @param float $tasso_crescita The growth rate of the plant.
     * @param string $luce The light requirements of the plant.
     * @param string $co2 The CO2 requirements of the plant.
     * @param string $difficolta The difficulty level of growing the plant.
     * @param int $id_pianta The ID of the plant.
     * @param int $id_acquario The ID of the aquarium.
     * @return string The generated query.
     */
    function createQuery($crud,$table, $nome, $origine, $tasso_crescita, $luce, $co2, $difficolta, $id_pianta, $id_acquario){
        // Costruisci la query SQL dinamicamente
        if($crud == 'r')
        {
            $sql = "SELECT * FROM $table WHERE 1=1";
        }
        if($crud == 'd')
        {
            $sql = "DELETE FROM $table WHERE 1=1";
        }

        if ($nome !== null) {
            $sql .= " AND nome LIKE '%$nome%'";
        }
        if ($origine !== null) {
            $sql .= " AND origine = '$origine'";
        }
        if ($tasso_crescita !== null) {
            $sql .= " AND tasso_crescita = '$tasso_crescita'";
        }
        if ($luce !== null) {
            $sql .= " AND luce = '$luce'";
        }
        if ($co2 !== null) {
            $sql .= " AND co2 = '$co2'";
        }
        if ($difficolta !== null) {
            $sql .= " AND difficolta LIKE '%$difficolta%'";
        }
        if ($id_pianta !== null) {
            $sql .= " AND id_pianta = '$id_pianta'";
        }
        if ($id_acquario !== null) {
            $sql .= " AND id_acquario = '$id_acquario'";
        }

        return $sql;
    }

    /**
     * Inserts an XML string into the database.
     *
     * @param string $xmlString The XML string to insert.
     * @param object $conn The database connection object.
     * @return void
     */
    function insertXmlIntoDatabase($xmlString, $conn) {
        // Disabilita la visualizzazione degli errori XML
        libxml_use_internal_errors(true);
    
        // Carica l'XML
        $xml = simplexml_load_string($xmlString);
    
        // Controlla gli errori XML
        if ($xml === false) {
            foreach (libxml_get_errors() as $error) {
                echo "Errore XML: ", $error->message;
            }
            libxml_clear_errors();
            return;
        }
    
        // Riabilita la visualizzazione degli errori XML
        libxml_use_internal_errors(false);
    
        // Ottieni il nome del nodo radice come nome della tabella
        $tableName = $xml->getName();
    
        // Cicla attraverso ogni item e inserisci nel database
        foreach ($xml->item as $item) {
            $columns = [];
            $values = [];
            $params = [];
            $types = '';
    
            // Ottieni colonne, valori e parametri per la query preparata
            foreach ($item->children() as $key => $value) {
                $columns[] = $key;
                $values[] = $value;
                $params[] = '?';
                $types .= 's'; // Supponendo che tutti i valori siano stringhe. Adatta se necessario.
            }
    
            // Crea e esegui la query preparata
            $sql = "INSERT INTO $tableName (" . implode(',', $columns) . ") VALUES (" . implode(',', $params) . ")";
    
            try {
                $stmt = $conn->prepare($sql);
                if ($stmt) {
                    $stmt->bind_param($types, ...$values);
                    if ($stmt->execute()) {
                        echo "Inserito con successo\r\n";
                    } else {
                        echo "Errore durante l'inserimento: " . $stmt->error;
                    }
                    $stmt->close();
                } else {
                    echo "Errore nella preparazione della query: " . $conn->error;
                }
            } catch (mysqli_sql_exception $e) {
                if ($e->getCode() == 1062) { // Codice per "Duplicate entry"
                    echo "Errore: Duplicate entry trovata, inserimento fallito\r\n";
                } else {
                    echo "Errore generico: " . $e->getMessage() . "\r\n";
                }
            }
        }
    }
    
    

?>