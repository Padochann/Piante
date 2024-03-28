<?php

$xmlString='<?xml version="1.0" encoding="utf-8"?>
<piante_acquari >
  <item>
    <id_pianta>203</id_pianta>
    <id_acquario>9</id_acquario>
    <quantita>2</quantita>
  </item>
</piante_acquari>
';

// Funzione per inserire i dati XML nel database
function insertXmlIntoDatabase($xmlString) {
    // Carica l'XML
    $xml = simplexml_load_string($xmlString);
    
    // Ottieni il nome del nodo radice come nome della tabella
    $tableName = $xml->getName();
    
    // Connessione al database
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "progetto_padoan_rossetti";

    // Crea la connessione
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Controlla la connessione
    if ($conn->connect_error) {
        die("Connessione fallita: " . $conn->connect_error);
    }

    // Cicla attraverso ogni item e inserisci nel database
    foreach ($xml->item as $item) {
        $columns = [];
        $values = [];
        
        // Ottieni colonne e valori
        foreach ($item->children() as $key => $value) {
            $columns[] = $key;
            $values[] = "'" . $conn->real_escape_string((string)$value) . "'";
        }

        // Crea e esegui la query di inserimento
        $sql = "INSERT INTO $tableName (" . implode(',', $columns) . ") VALUES (" . implode(',', $values) . ")";
        if ($conn->query($sql) !== TRUE) {
            echo "Errore durante l'inserimento: " . $conn->error;
        }
    }

    // Chiudi la connessione
    $conn->close();
}



// Inserisci XML nel database
insertXmlIntoDatabase($xmlString);

echo "Dati XML inseriti nel database con successo!";




?>