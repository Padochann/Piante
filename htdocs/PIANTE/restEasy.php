<?php
    require('include/funz.inc');
    // Definizione del percorso XSD
    $xsdPath = 'plants.xsd';

    
// Connessione al database 
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "progetto_padoan_rossetti";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica la connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
}

if(isset($_GET['table'])){
    // Recupera i parametri GET
    $table = $_GET['table'];

    $nome = isset($_GET['nome']) ? $_GET['nome'] : null;
    $origine = isset($_GET['origine']) ? $_GET['origine'] : null;
    $tasso_crescita = isset($_GET['tasso_crescita']) ? $_GET['tasso_crescita'] : null;
    $luce = isset($_GET['luce']) ? $_GET['luce'] : null;
    $co2 = isset($_GET['co2']) ? $_GET['co2'] : null;
    $difficolta = isset($_GET['difficolta']) ? $_GET['difficolta'] : null;
    $id_pianta = isset($_GET['id_pianta']) ? $_GET['id_pianta'] : null;
    $id_acquario = isset($_GET['id_acquario']) ? $_GET['id_acquario'] : null;
    // Costruisci la query SQL dinamicamente
    $sql = createQuery($table, $nome, $origine, $tasso_crescita, $luce, $co2, $difficolta, $id_pianta, $id_acquario);
    // Esegui la query
    $result = $conn->query($sql);
    // Genera il documento XML
    $xmlStringPiante = generateXmlFromResultSet($result, $xsdPath, $table, 'Piante');
    // Invia il documento XML al client 
    echo $xmlStringPiante;
    // Salva il documento XML su file per debug in locale
    file_put_contents("$table.xml", $xmlStringPiante);
    
}
// Leggi l'XML inviato
$xmlString = file_get_contents('php://input');

// Verifica se l'XML è stato inviato e se è un XML valido
if (!empty($xmlString) ) {
    // Inserisci XML nel database
    insertXmlIntoDatabase($xmlString, $conn);
} 


// Chiudi la connessione al database
$conn->close();
?>




