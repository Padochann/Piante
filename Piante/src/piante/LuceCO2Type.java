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
 * <p>Classe Java per luceCO2Type.
 * 
 * <p>Il seguente frammento di schema specifica il contenuto previsto contenuto in questa classe.
 * <pre>{@code
 * <simpleType name="luceCO2Type">
 *   <restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *     <enumeration value="poca"/>
 *     <enumeration value="media"/>
 *     <enumeration value="tanta"/>
 *   </restriction>
 * </simpleType>
 * }</pre>
 * 
 */
@XmlType(name = "luceCO2Type")
@XmlEnum
public enum LuceCO2Type {

    @XmlEnumValue("poca")
    POCA("poca"),
    @XmlEnumValue("media")
    MEDIA("media"),
    @XmlEnumValue("tanta")
    TANTA("tanta");
    private final String value;

    LuceCO2Type(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static LuceCO2Type fromValue(String v) {
        for (LuceCO2Type c: LuceCO2Type.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}
