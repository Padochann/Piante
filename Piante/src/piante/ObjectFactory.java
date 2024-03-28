//
// Questo file è stato generato dall'Eclipse Implementation of JAXB, v4.0.3 
// Vedere https://eclipse-ee4j.github.io/jaxb-ri 
// Qualsiasi modifica a questo file andrà persa durante la ricompilazione dello schema di origine. 
//


package piante;

import javax.xml.namespace.QName;
import jakarta.xml.bind.JAXBElement;
import jakarta.xml.bind.annotation.XmlElementDecl;
import jakarta.xml.bind.annotation.XmlRegistry;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the piante package. 
 * <p>An ObjectFactory allows you to programmatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private static final QName _Piante_QNAME = new QName("Piante", "piante");
    private static final QName _Acquari_QNAME = new QName("Piante", "acquari");
    private static final QName _Immagini_QNAME = new QName("Piante", "immagini");
    private static final QName _PianteAcquari_QNAME = new QName("Piante", "piante_acquari");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: piante
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link PianteType }
     * 
     * @return
     *     the new instance of {@link PianteType }
     */
    public PianteType createPianteType() {
        return new PianteType();
    }

    /**
     * Create an instance of {@link AcquariType }
     * 
     * @return
     *     the new instance of {@link AcquariType }
     */
    public AcquariType createAcquariType() {
        return new AcquariType();
    }

    /**
     * Create an instance of {@link ImmaginiType }
     * 
     * @return
     *     the new instance of {@link ImmaginiType }
     */
    public ImmaginiType createImmaginiType() {
        return new ImmaginiType();
    }

    /**
     * Create an instance of {@link PianteAcquariType }
     * 
     * @return
     *     the new instance of {@link PianteAcquariType }
     */
    public PianteAcquariType createPianteAcquariType() {
        return new PianteAcquariType();
    }

    /**
     * Create an instance of {@link AcquarioType }
     * 
     * @return
     *     the new instance of {@link AcquarioType }
     */
    public AcquarioType createAcquarioType() {
        return new AcquarioType();
    }

    /**
     * Create an instance of {@link ImmagineType }
     * 
     * @return
     *     the new instance of {@link ImmagineType }
     */
    public ImmagineType createImmagineType() {
        return new ImmagineType();
    }

    /**
     * Create an instance of {@link PiantaType }
     * 
     * @return
     *     the new instance of {@link PiantaType }
     */
    public PiantaType createPiantaType() {
        return new PiantaType();
    }

    /**
     * Create an instance of {@link PiantaAcquarioType }
     * 
     * @return
     *     the new instance of {@link PiantaAcquarioType }
     */
    public PiantaAcquarioType createPiantaAcquarioType() {
        return new PiantaAcquarioType();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link PianteType }{@code >}
     * 
     * @param value
     *     Java instance representing xml element's value.
     * @return
     *     the new instance of {@link JAXBElement }{@code <}{@link PianteType }{@code >}
     */
    @XmlElementDecl(namespace = "Piante", name = "piante")
    public JAXBElement<PianteType> createPiante(PianteType value) {
        return new JAXBElement<>(_Piante_QNAME, PianteType.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link AcquariType }{@code >}
     * 
     * @param value
     *     Java instance representing xml element's value.
     * @return
     *     the new instance of {@link JAXBElement }{@code <}{@link AcquariType }{@code >}
     */
    @XmlElementDecl(namespace = "Piante", name = "acquari")
    public JAXBElement<AcquariType> createAcquari(AcquariType value) {
        return new JAXBElement<>(_Acquari_QNAME, AcquariType.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link ImmaginiType }{@code >}
     * 
     * @param value
     *     Java instance representing xml element's value.
     * @return
     *     the new instance of {@link JAXBElement }{@code <}{@link ImmaginiType }{@code >}
     */
    @XmlElementDecl(namespace = "Piante", name = "immagini")
    public JAXBElement<ImmaginiType> createImmagini(ImmaginiType value) {
        return new JAXBElement<>(_Immagini_QNAME, ImmaginiType.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link PianteAcquariType }{@code >}
     * 
     * @param value
     *     Java instance representing xml element's value.
     * @return
     *     the new instance of {@link JAXBElement }{@code <}{@link PianteAcquariType }{@code >}
     */
    @XmlElementDecl(namespace = "Piante", name = "piante_acquari")
    public JAXBElement<PianteAcquariType> createPianteAcquari(PianteAcquariType value) {
        return new JAXBElement<>(_PianteAcquari_QNAME, PianteAcquariType.class, null, value);
    }

}
