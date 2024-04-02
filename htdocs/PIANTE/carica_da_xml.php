<?php
//stringa di test per verificare il funzionamento 
$xmlString='<?xml version="1.0" encoding="utf-8"?>
<acquari>
  <item>
    <id_acquario>0</id_acquario>
    <litri>100</litri>
    <larghezza>100</larghezza>
    <lunghezza>100</lunghezza>
    <altezza>100</altezza>
    <descrizione>acquario di test</descrizione>
  </item>
</acquari>
';

//credenziali accesso al db
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

// Inserisci XML nel database
insertXmlIntoDatabase($xmlString, $conn);

// Chiudi la connessione
$conn->close();



// Funzione per inserire i dati XML nel database
function insertXmlIntoDatabase($xmlString, $conn) {
    // Carica l'XML
    $xml = simplexml_load_string($xmlString);
    
    // Ottieni il nome del nodo radice come nome della tabella
    $tableName = $xml->getName();

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
        }else{
            echo "inserito con successo";
        }
    }
}
?>
