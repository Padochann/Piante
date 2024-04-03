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
 * <p>Classe Java per pianta_acquarioType complex type.
 * 
 * <p>Il seguente frammento di schema specifica il contenuto previsto contenuto in questa classe.
 * 
 * <pre>{@code
 * <complexType name="pianta_acquarioType">
 *   <complexContent>
 *     <restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       <sequence>
 *         <element name="id_pianta" type="{Piante}idPiantaType"/>
 *         <element name="id_acquario" type="{Piante}idAcquarioType"/>
 *         <element name="quantita" type="{Piante}quantitaType"/>
 *       </sequence>
 *     </restriction>
 *   </complexContent>
 * </complexType>
 * }</pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "pianta_acquarioType", propOrder = {
    "idPianta",
    "idAcquario",
    "quantita"
})
public class PiantaAcquarioType {

    @XmlElement(name = "id_pianta")
    @XmlSchemaType(name = "unsignedInt")
    protected long idPianta;
    @XmlElement(name = "id_acquario")
    @XmlSchemaType(name = "unsignedInt")
    protected long idAcquario;
    @XmlSchemaType(name = "unsignedInt")
    protected long quantita;

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
     * Recupera il valore della proprietà quantita.
     * 
     */
    public long getQuantita() {
        return quantita;
    }

    /**
     * Imposta il valore della proprietà quantita.
     * 
     */
    public void setQuantita(long value) {
        this.quantita = value;
    }

	@Override
	public String toString() {
		return "PiantaAcquarioType [idPianta=" + idPianta + ", idAcquario=" + idAcquario + ", quantita=" + quantita
				+ "]";
	}

    
    
}
