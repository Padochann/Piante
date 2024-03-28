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
 * <p>Classe Java per acquarioType complex type.
 * 
 * <p>Il seguente frammento di schema specifica il contenuto previsto contenuto in questa classe.
 * 
 * <pre>{@code
 * <complexType name="acquarioType">
 *   <complexContent>
 *     <restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       <sequence>
 *         <element name="id_acquario" type="{Piante}idAcquarioType"/>
 *         <element name="litri" type="{Piante}dimensioneType"/>
 *         <element name="larghezza" type="{Piante}dimensioneType"/>
 *         <element name="lunghezza" type="{Piante}dimensioneType"/>
 *         <element name="altezza" type="{Piante}dimensioneType"/>
 *         <element name="descrizione" type="{Piante}testoType"/>
 *       </sequence>
 *     </restriction>
 *   </complexContent>
 * </complexType>
 * }</pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "acquarioType", propOrder = {
    "idAcquario",
    "litri",
    "larghezza",
    "lunghezza",
    "altezza",
    "descrizione"
})
public class AcquarioType {

    @XmlElement(name = "id_acquario")
    @XmlSchemaType(name = "unsignedInt")
    protected long idAcquario;
    @XmlSchemaType(name = "unsignedInt")
    protected long litri;
    @XmlSchemaType(name = "unsignedInt")
    protected long larghezza;
    @XmlSchemaType(name = "unsignedInt")
    protected long lunghezza;
    @XmlSchemaType(name = "unsignedInt")
    protected long altezza;
    @XmlElement(required = true)
    protected String descrizione;

    /**
     * Recupera il valore della proprietà idAcquario.
     * 
     */
    public long getIdAcquario() {
        return idAcquario;
    }

    /**
     * Imposta il valore della proprietà idAcquario.
     * 
     */
    public void setIdAcquario(long value) {
        this.idAcquario = value;
    }

    /**
     * Recupera il valore della proprietà litri.
     * 
     */
    public long getLitri() {
        return litri;
    }

    /**
     * Imposta il valore della proprietà litri.
     * 
     */
    public void setLitri(long value) {
        this.litri = value;
    }

    /**
     * Recupera il valore della proprietà larghezza.
     * 
     */
    public long getLarghezza() {
        return larghezza;
    }

    /**
     * Imposta il valore della proprietà larghezza.
     * 
     */
    public void setLarghezza(long value) {
        this.larghezza = value;
    }

    /**
     * Recupera il valore della proprietà lunghezza.
     * 
     */
    public long getLunghezza() {
        return lunghezza;
    }

    /**
     * Imposta il valore della proprietà lunghezza.
     * 
     */
    public void setLunghezza(long value) {
        this.lunghezza = value;
    }

    /**
     * Recupera il valore della proprietà altezza.
     * 
     */
    public long getAltezza() {
        return altezza;
    }

    /**
     * Imposta il valore della proprietà altezza.
     * 
     */
    public void setAltezza(long value) {
        this.altezza = value;
    }

    /**
     * Recupera il valore della proprietà descrizione.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getDescrizione() {
        return descrizione;
    }

    /**
     * Imposta il valore della proprietà descrizione.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setDescrizione(String value) {
        this.descrizione = value;
    }

}
