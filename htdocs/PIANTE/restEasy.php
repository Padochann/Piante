<?php
    require('include/funz.inc');
    // Definizione del percorso XSD
    $xsdPath = 'plants.xsd';

    
// Connessione al database (sostituisci con i tuoi dati di connessione)
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "progetto_padoan_rossetti";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica la connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
}

// Recupera i parametri dalla query string
$table = $_GET['table'];

$nome = isset($_GET['nome']) ? $_GET['nome'] : null;
$origine = isset($_GET['origine']) ? $_GET['origine'] : null;
$tasso_crescita = isset($_GET['tasso_crescita']) ? $_GET['tasso_crescita'] : null;
$luce = isset($_GET['luce']) ? $_GET['luce'] : null;
$co2 = isset($_GET['co2']) ? $_GET['co2'] : null;
$difficolta = isset($_GET['difficolta']) ? $_GET['difficolta'] : null;

// Costruisci la query SQL dinamicamente
$sql = "SELECT * FROM $table WHERE 1=1";

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

// Esegui la query SQL
$result = $conn->query($sql);

$xmlStringPiante= generateXmlFromResultSet($result,$xsdPath,'piante','Piante');
echo $xmlStringPiante;

// Aggiungi l'attributo xmlns al tag radice nel XML string
//$xmlStringPiante = str_replace('<piante>', '<piante xmlns="Piante">', $xmlStringPiante);

// Salva il contenuto nel file
file_put_contents('piante.xml', $xmlStringPiante);


// Chiudi la connessione al database
$conn->close();
?>




