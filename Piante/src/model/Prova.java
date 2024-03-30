package model;


import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;
import piante.LuceCO2Type;
import piante.PiantaType;
import piante.PianteType;
import piante.TassoCrescitaType;
public class Prova {

	public static void main(String[] args) throws JAXBException {
		
		JAXBContext context = JAXBContext.newInstance(PianteType.class);
		Marshaller marshaller= context.createMarshaller();
		marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
		
		PianteType p = new PianteType();
		p.getItem().add(new PiantaType(){
			{
				setNome("ciccio");
				setIdPianta(1);
				setAltezzaMassima(10);
				setAltezzaMinima(2);
				setCo2(LuceCO2Type.POCA);
				setDifficolta("Easy.png");
				setLinkImg("link img");
				setLinkLogo("link logo");
				setLinkPagina("link pagina");
				setTipo("steam");
				setLuce(LuceCO2Type.MEDIA);
				setOrigine("lollo");
				setTassoCrescita(TassoCrescitaType.LENTO);
				
			}
		});
		p.getItem().add(new PiantaType(){
			{
				setNome("ciccio");
				setIdPianta(1);
				setAltezzaMassima(10);
				setAltezzaMinima(2);
				setCo2(LuceCO2Type.POCA);
				setDifficolta("Easy.png");
				setLinkImg("link img");
				setLinkLogo("link logo");
				setLinkPagina("link pagina");
				setTipo("steam");
				setLuce(LuceCO2Type.MEDIA);
				setOrigine("lollo");
				setTassoCrescita(TassoCrescitaType.LENTO);
				
			}
		});
		p.getItem().add(new PiantaType(){
			{
				setNome("ciccio");
				setIdPianta(1);
				setAltezzaMassima(10);
				setAltezzaMinima(2);
				setCo2(LuceCO2Type.POCA);
				setDifficolta("Easy.png");
				setLinkImg("link img");
				setLinkLogo("link logo");
				setLinkPagina("link pagina");
				setTipo("steam");
				setLuce(LuceCO2Type.MEDIA);
				setOrigine("lollo");
				setTassoCrescita(TassoCrescitaType.LENTO);
				
			}
		});
		
		marshaller.marshal(p, System.out);
		
		
	}
}
