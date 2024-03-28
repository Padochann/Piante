<?php
// Imposta il limite di tempo massimo di esecuzione a 300 secondi (5 minuti)
set_time_limit(300);

// Percorso della cartella delle immagini
$imageFolder = "D:/informatica/images/";

$servername = "localhost";
$username = "root"; // Cambia con il tuo username
$password = ""; // Cambia con la tua password
$dbname = "piante"; // Cambia con il nome del tuo database

// Crea la connessione
$conn = new mysqli($servername, $username, $password, $dbname);

// Controlla la connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
} else {
    echo "Connessione eseguita<br>";
}

// Lista tutti i file nella cartella delle immagini
$files = glob($imageFolder . "*.{jpg,png,gif,jpeg}", GLOB_BRACE);

// Ordina l'array dei file in ordine numerico
natsort($files);

$i=1;
foreach ($files as $file) {
    $imageData = file_get_contents($file);
    $imageName = basename($file);
    $idPianta = pathinfo($imageName, PATHINFO_FILENAME); // Assume che il nome del file sia l'id_pianta

    // Prepara la query
    $stmt = $conn->prepare("INSERT INTO immagini (id_immagine, immagine_pianta, id_pianta) VALUES (?, ?, ?)");
    
    // Collega i parametri alla query
    $stmt->bind_param("isi", $i, $imageData, $i);

    // Esegui la query
    if ($stmt->execute() === TRUE) {
        echo "Immagine inserita con successo: " . $imageName . "<br>";
    } else {
        echo "Errore durante l'inserimento dell'immagine: " . $stmt->error . "<br>";
    }

    $i++;
}

// Chiudi la connessione
$stmt->close();
$conn->close();

echo "Tutte le immagini sono state caricate con successo nel database!";
?>
