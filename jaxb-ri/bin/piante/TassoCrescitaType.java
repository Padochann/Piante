//
// Questo file è stato generato dall'Eclipse Implementation of JAXB, v4.0.3 
// Vedere https://eclipse-ee4j.github.io/jaxb-ri 
// Qualsiasi modifica a questo file andrà persa durante la ricompilazione dello schema di origine. 
//


package piante;

import jakarta.xml.bind.annotation.XmlEnum;
import jakarta.xml.bind.annotation.XmlEnumValue;
import jakarta.xml.bind.annotation.XmlType;


/**
 * <p>Classe Java per tassoCrescitaType.
 * 
 * <p>Il seguente frammento di schema specifica il contenuto previsto contenuto in questa classe.
 * <pre>{@code
 * <simpleType name="tassoCrescitaType">
 *   <restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *     <enumeration value="lento"/>
 *     <enumeration value="medio"/>
 *     <enumeration value="veloce"/>
 *   </restriction>
 * </simpleType>
 * }</pre>
 * 
 */
@XmlType(name = "tassoCrescitaType")
@XmlEnum
public enum TassoCrescitaType {

    @XmlEnumValue("lento")
    LENTO("lento"),
    @XmlEnumValue("medio")
    MEDIO("medio"),
    @XmlEnumValue("veloce")
    VELOCE("veloce");
    private final String value;

    TassoCrescitaType(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static TassoCrescitaType fromValue(String v) {
        for (TassoCrescitaType c: TassoCrescitaType.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}
