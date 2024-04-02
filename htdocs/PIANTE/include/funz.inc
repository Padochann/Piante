<?php
    function prova(){
        echo "prova";
    }

/**
 * Generates an XML document from a result set.
 *
 * @param mixed $resultSet The result set to generate XML from.
 * @param string $xsdPath The path to the XSD file for validation.
 * @param string $rootTagName The name of the root XML element.
 * @param string $namespace The namespace to be used in the XML.
 * @return string The generated XML document.
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



?>