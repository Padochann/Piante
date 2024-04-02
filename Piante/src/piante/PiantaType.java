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
 * <p>Classe Java per piantaType complex type.
 * 
 * <p>Il seguente frammento di schema specifica il contenuto previsto contenuto in questa classe.
 * 
 * <pre>{@code
 * <complexType name="piantaType">
 *   <complexContent>
 *     <restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       <sequence>
 *         <element name="id_pianta" type="{Piante}idPiantaType"/>
 *         <element name="nome" type="{Piante}testoType"/>
 *         <element name="link_pagina" type="{Piante}linkType"/>
 *         <element name="link_img" type="{Piante}linkImgType"/>
 *         <element name="tipo" type="{Piante}tipoPiantaType"/>
 *         <element name="origine" type="{Piante}origineType"/>
 *         <element name="tasso_crescita" type="{Piante}tassoCrescitaType"/>
 *         <element name="altezza_minima" type="{Piante}altezzaType"/>
 *         <element name="altezza_massima" type="{Piante}altezzaType"/>
 *         <element name="luce" type="{Piante}luceCO2Type"/>
 *         <element name="co2" type="{Piante}luceCO2Type"/>
 *         <element name="link_logo" type="{Piante}linkLogoType"/>
 *         <element name="difficolta" type="{Piante}difficoltaType"/>
 *       </sequence>
 *     </restriction>
 *   </complexContent>
 * </complexType>
 * }</pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "piantaType", propOrder = {
    "idPianta",
    "nome",
    "linkPagina",
    "linkImg",
    "tipo",
    "origine",
    "tassoCrescita",
    "altezzaMinima",
    "altezzaMassima",
    "luce",
    "co2",
    "linkLogo",
    "difficolta"
})
public class PiantaType {

    @XmlElement(name = "id_pianta")
    @XmlSchemaType(name = "unsignedInt")
    protected long idPianta;
    @XmlElement(required = true)
    protected String nome;
    @XmlElement(name = "link_pagina", required = true)
    protected String linkPagina;
    @XmlElement(name = "link_img", required = true)
    protected String linkImg;
    @XmlElement(required = true)
    protected String tipo;
    @XmlElement(required = true)
    protected String origine;
    @XmlElement(name = "tasso_crescita", required = true)
    @XmlSchemaType(name = "string")
    protected TassoCrescitaType tassoCrescita;
    @XmlElement(name = "altezza_minima")
    @XmlSchemaType(name = "unsignedInt")
    protected long altezzaMinima;
    @XmlElement(name = "altezza_massima")
    @XmlSchemaType(name = "unsignedInt")
    protected long altezzaMassima;
    @XmlElement(required = true)
    @XmlSchemaType(name = "string")
    protected LuceCO2Type luce;
    @XmlElement(required = true)
    @XmlSchemaType(name = "string")
    protected LuceCO2Type co2;
    @XmlElement(name = "link_logo", required = true)
    protected String linkLogo;
    @XmlElement(required = true)
    protected String difficolta;

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
     * Recupera il valore della proprietà nome.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getNome() {
        return nome;
    }

    /**
     * Imposta il valore della proprietà nome.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setNome(String value) {
        this.nome = value;
    }

    /**
     * Recupera il valore della proprietà linkPagina.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getLinkPagina() {
        return linkPagina;
    }

    /**
     * Imposta il valore della proprietà linkPagina.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setLinkPagina(String value) {
        this.linkPagina = value;
    }

    /**
     * Recupera il valore della proprietà linkImg.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getLinkImg() {
        return linkImg;
    }

    /**
     * Imposta il valore della proprietà linkImg.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setLinkImg(String value) {
        this.linkImg = value;
    }

    /**
     * Recupera il valore della proprietà tipo.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getTipo() {
        return tipo;
    }

    /**
     * Imposta il valore della proprietà tipo.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setTipo(String value) {
        this.tipo = value;
    }

    /**
     * Recupera il valore della proprietà origine.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getOrigine() {
        return origine;
    }

    /**
     * Imposta il valore della proprietà origine.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setOrigine(String value) {
        this.origine = value;
    }

    /**
     * Recupera il valore della proprietà tassoCrescita.
     * 
     * @return
     *     possible object is
     *     {@link TassoCrescitaType }
     *     
     */
    public TassoCrescitaType getTassoCrescita() {
        return tassoCrescita;
    }

    /**
     * Imposta il valore della proprietà tassoCrescita.
     * 
     * @param value
     *     allowed object is
     *     {@link TassoCrescitaType }
     *     
     */
    public void setTassoCrescita(TassoCrescitaType value) {
        this.tassoCrescita = value;
    }

    /**
     * Recupera il valore della proprietà altezzaMinima.
     * 
     */
    public long getAltezzaMinima() {
        return altezzaMinima;
    }

    /**
     * Imposta il valore della proprietà altezzaMinima.
     * 
     */
    public void setAltezzaMinima(long value) {
        this.altezzaMinima = value;
    }

    /**
     * Recupera il valore della proprietà altezzaMassima.
     * 
     */
    public long getAltezzaMassima() {
        return altezzaMassima;
    }

    /**
     * Imposta il valore della proprietà altezzaMassima.
     * 
     */
    public void setAltezzaMassima(long value) {
        this.altezzaMassima = value;
    }

    /**
     * Recupera il valore della proprietà luce.
     * 
     * @return
     *     possible object is
     *     {@link LuceCO2Type }
     *     
     */
    public LuceCO2Type getLuce() {
        return luce;
    }

    /**
     * Imposta il valore della proprietà luce.
     * 
     * @param value
     *     allowed object is
     *     {@link LuceCO2Type }
     *     
     */
    public void setLuce(LuceCO2Type value) {
        this.luce = value;
    }

    /**
     * Recupera il valore della proprietà co2.
     * 
     * @return
     *     possible object is
     *     {@link LuceCO2Type }
     *     
     */
    public LuceCO2Type getCo2() {
        return co2;
    }

    /**
     * Imposta il valore della proprietà co2.
     * 
     * @param value
     *     allowed object is
     *     {@link LuceCO2Type }
     *     
     */
    public void setCo2(LuceCO2Type value) {
        this.co2 = value;
    }

    /**
     * Recupera il valore della proprietà linkLogo.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getLinkLogo() {
        return linkLogo;
    }

    /**
     * Imposta il valore della proprietà linkLogo.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setLinkLogo(String value) {
        this.linkLogo = value;
    }

    /**
     * Recupera il valore della proprietà difficolta.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getDifficolta() {
        return difficolta;
    }

    /**
     * Imposta il valore della proprietà difficolta.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setDifficolta(String value) {
        this.difficolta = value;
    }

	@Override
	public String toString() {
		return "PiantaType [idPianta=" + idPianta + ", nome=" + nome + ", linkPagina=" + linkPagina + ", linkImg="
				+ linkImg + ", tipo=" + tipo + ", origine=" + origine + ", tassoCrescita=" + tassoCrescita
				+ ", altezzaMinima=" + altezzaMinima + ", altezzaMassima=" + altezzaMassima + ", luce=" + luce
				+ ", co2=" + co2 + ", linkLogo=" + linkLogo + ", difficolta=" + difficolta + "]";
	}

	
    
    

}
