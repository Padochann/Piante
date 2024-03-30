package control;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import view.Window;

public class Controller implements ActionListener{
	
	private Window w;
	
	public Controller(Window w) {
		this.w= w;
		this.w.registerEvent(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		try
		{
			
		}
		catch(Exception e1) {
			w.messageDialog(e1.getMessage());
		}
	}
	
}
