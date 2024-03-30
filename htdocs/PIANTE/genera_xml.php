<?php
// Attivazione della visualizzazione degli errori
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Credenziali di accesso al database
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "progetto_padoan_rossetti";

// Creazione della connessione al database
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica della connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
} else {
    echo "Connessione eseguita<br>";
}

// Percorso dello schema XSD
$xsdPath = 'tipi.xsd';

// Esecuzione delle query e generazione degli XML
generateXmlForTable($conn, 'piante', $xsdPath, 'piante.xml');
generateXmlForTable($conn, 'acquari', $xsdPath, 'acquari.xml');
generateXmlForTable($conn, 'immagini', $xsdPath, 'immagini.xml');
generateXmlForTable($conn, 'piante_acquari', $xsdPath, 'piante_acquari.xml');

// Chiusura della connessione al database
$conn->close();

// Funzione per generare un XML per una specifica tabella
function generateXmlForTable($conn, $tableName, $xsdPath, $xmlFileName) {
    $sql = "SELECT * FROM $tableName;";
    $result = $conn->query($sql);
    $xmlString = generateXmlFromResultSet($result, $xsdPath, $tableName);
    file_put_contents($xmlFileName, $xmlString);
    echo "<br/>$xmlFileName creato con successo";
}

// Funzione per visualizzare un'immagine da un campo BLOB
function displayImageFromBlob($blobData, $contentType) {
    header("Content-type: $contentType");
    echo $blobData;
}

// Funzione per generare un XML da un ResultSet con gestione BLOB
function generateXmlFromResultSet($resultSet, $xsdPath, $rootTagName) {
    $xmlWriter = new XMLWriter();
    $xmlWriter->openMemory();
    $xmlWriter->setIndent(true);
    $xmlWriter->startDocument('1.0', 'UTF-8');

    // Impostazione dello schema XSD
    $xmlWriter->writeAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    $xmlWriter->writeAttribute('xsi:noNamespaceSchemaLocation', $xsdPath);

    $xmlWriter->startElement($rootTagName);

    while ($row = $resultSet->fetch_assoc()) {
        $xmlWriter->startElement('item');
        
        foreach ($row as $key => $value) {
            $xmlWriter->startElement($key);

            // Conversione in base64 se il valore è un BLOB
            if ($key === 'immagine_pianta') {
                $value = base64_encode($value);
            }

            $xmlWriter->text($value);
            $xmlWriter->endElement();
        }
        
        $xmlWriter->endElement();
    }

    $xmlWriter->endElement();
    $xmlWriter->endDocument();

    return $xmlWriter->outputMemory();
}

?>
