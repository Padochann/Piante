<?php
// Funzione per generare XML da ResultSet con gestione BLOB
function generateXmlFromResultSet($resultSet, $xsdPath, $rootTagName) {
    $xmlWriter = new XMLWriter();
    $xmlWriter->openMemory();
    $xmlWriter->setIndent(true);
    $xmlWriter->startDocument('1.0', 'UTF-8');

    // Imposta lo schema XSD
    $xmlWriter->writeAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    $xmlWriter->writeAttribute('xsi:noNamespaceSchemaLocation', $xsdPath);

    $xmlWriter->startElement($rootTagName);

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

    $xmlWriter->endElement();
    $xmlWriter->endDocument();

    return $xmlWriter->outputMemory();
}
// Funzione per visualizzare un'immagine da un campo BLOB
function displayImageFromBlob($blobData, $contentType) {
    header("Content-type: $contentType");
    echo $blobData;
}

// Attiva la visualizzazione degli errori
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$servername = "localhost";
$username = "root"; 
$password = ""; 
$dbname = "progetto_padoan_rossetti";

// Crea la connessione
$conn = new mysqli($servername, $username, $password, $dbname);

// Controlla la connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
} else {
    echo "Connessione eseguita<br>";
}




// Definizione del percorso XSD
$xsdPath = 'plants.xsd';

// Genera l'XML per piante
// Esegui la query
$sql = "SELECT * FROM piante ;";
$result = $conn->query($sql);
$xmlStringPiante = generateXmlFromResultSet($result, $xsdPath, 'piante');
file_put_contents('piante.xml', $xmlStringPiante);
/*
// Genera l'XML per acquari
$sqlAcquari = "SELECT * FROM acquari;";
$resultAcquari = $conn->query($sqlAcquari);
$xmlStringAcquari = generateXmlFromResultSet($resultAcquari, $xsdPath, 'acquari');
file_put_contents('acquari.xml', $xmlStringAcquari);

// Genera l'XML per immagini
$sqlImmagini = "SELECT * FROM immagini;";
$resultImmagini = $conn->query($sqlImmagini);
$xmlStringImmagini = generateXmlFromResultSet($resultImmagini, $xsdPath, 'immagini');
file_put_contents('immagini.xml', $xmlStringImmagini);

// Genera l'XML per piante_acquari
$sqlPianteAcquari = "SELECT * FROM piante_acquari;";
$resultPianteAcquari = $conn->query($sqlPianteAcquari);
$xmlStringPianteAcquari = generateXmlFromResultSet($resultPianteAcquari, $xsdPath, 'piante_acquari');
file_put_contents('piante_acquari.xml', $xmlStringPianteAcquari);
*/
// Chiudi la connessione
$conn->close();

echo "Documenti XML generati con successo!";
?>
