package model;


import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;
import piante.AcquariType;
import piante.AcquarioType;
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
		
		JAXBContext context1 = JAXBContext.newInstance(AcquariType.class);
		Marshaller marshaller1= context1.createMarshaller();
		marshaller1.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
		
		
		AcquariType a = new AcquariType();
		a.getItem().add(new AcquarioType() {
			{
				setIdAcquario(0);
				setLitri(20);
				setLarghezza(3);
				setLunghezza(3);
				setAltezza(3);
				setDescrizione("ciao cino");
			}
		});
		a.getItem().add(new AcquarioType() {
			{
				setIdAcquario(0);
				setLitri(20);
				setLarghezza(3);
				setLunghezza(3);
				setAltezza(3);
				setDescrizione("ciao guzzo");
			}
		});
		a.getItem().add(new AcquarioType() {
			{
				setIdAcquario(0);
				setLitri(20);
				setLarghezza(3);
				setLunghezza(3);
				setAltezza(3);
				setDescrizione("ciao piove");
			}
		});
		
		marshaller1.marshal(a, System.out);
		
		RestEasyPlantsClient r = new RestEasyPlantsClient();
		
		try {
			r.sendDataToApi(a);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
