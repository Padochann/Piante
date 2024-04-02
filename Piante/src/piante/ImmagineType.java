//
// Questo file è stato generato dall'Eclipse Implementation of JAXB, v4.0.3 
// Vedere https://eclipse-ee4j.github.io/jaxb-ri 
// Qualsiasi modifica a questo file andrà persa durante la ricompilazione dello schema di origine. 
//


package piante;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlSchemaType;
import jakarta.xml.bind.annotation.XmlType;


/**
 * <p>Classe Java per immagineType complex type.
 * 
 * <p>Il seguente frammento di schema specifica il contenuto previsto contenuto in questa classe.
 * 
 * <pre>{@code
 * <complexType name="immagineType">
 *   <complexContent>
 *     <restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       <sequence>
 *         <element name="id_immagine" type="{http://www.w3.org/2001/XMLSchema}unsignedInt"/>
 *         <element name="immagine_pianta" type="{Piante}base64Binary"/>
 *         <element name="id_pianta" type="{http://www.w3.org/2001/XMLSchema}unsignedInt"/>
 *       </sequence>
 *     </restriction>
 *   </complexContent>
 * </complexType>
 * }</pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "immagineType", propOrder = {
    "idImmagine",
    "immaginePianta",
    "idPianta"
})
public class ImmagineType {

    @XmlElement(name = "id_immagine")
    @XmlSchemaType(name = "unsignedInt")
    protected long idImmagine;
    @XmlElement(name = "immagine_pianta", required = true)
    protected byte[] immaginePianta;
    @XmlElement(name = "id_pianta")
    @XmlSchemaType(name = "unsignedInt")
    protected long idPianta;

    /**
     * Recupera il valore della proprietà idImmagine.
     * 
     */
    public long getIdImmagine() {
        return idImmagine;
    }

    /**
     * Imposta il valore della proprietà idImmagine.
     * 
     */
    public void setIdImmagine(long value) {
        this.idImmagine = value;
    }


    /**
     * Recupera il valore della proprietà immaginePianta.
     * 
     * @return
     *     possible object is
     *     byte[]
     */
    public byte[] getImmaginePianta() {
        return immaginePianta;
    }

    /**
     * Imposta il valore della proprietà immaginePianta.
     * 
     * @param value
     *     allowed object is
     *     byte[]
     */
    public void setImmaginePianta(byte[] value) {
        this.immaginePianta = value;
    }

    /**
     * Recupera il valore della proprietà idPianta.
     * 
     */
    public long getIdPianta() {
    	return idPianta;
    }
    
    /**
     * Imposta il valore della proprietà idPianta.
     * 
     */
    public void setIdPianta(long value) {
    	this.idPianta = value;
    }
}
