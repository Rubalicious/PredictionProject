import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;


public class Controller extends JFrame {
	
	
	private static int SIZE = 500;
	//The menu bar
	private JMenuBar theMenuBar;
	private JMenu file;
	private JMenuItem about;
	
	private JPanel view;
	private ArrayList<GridPanel> panels;
	private IsingModel simulation;
	
	public Controller(){
		super("Simulation");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		this.setSize(new Dimension(SIZE, SIZE));
		
		simulation = new IsingModel(SIZE);
		//The GridLayout should be the same size as the ising model
		view = new JPanel(new GridLayout(SIZE,SIZE));
		panels = new ArrayList<GridPanel>();
		
//		setUpMenuBar();
		
		setUpView();
		JLabel trial = new JLabel("Test");
		trial.setLocation(50, 50);
		trial.setVisible(true);
		add(trial);
		add(view);
//		pack();
	}
	
	private class GridPanel extends Component{
		private boolean up;
		public GridPanel(){
			super();
			setSize(5,5);
			up = false;
		}
		public void setOrientation(boolean u){
			up = u;
		}
		
		@Override
		public void paint(Graphics g){
			g.setColor(up ? Color.YELLOW:Color.BLUE);
			g.fillRect(0, 0, (int)getSize().getWidth(), (int)getSize().getHeight());
		}
	}
	
	private void setUpView() {
		for (int i = 0; i < SIZE; i ++){
			for (int j = 0; j < SIZE; j++){
				GridPanel no_ref = new GridPanel();
				view.add(no_ref);
				panels.add(no_ref);
			}
		}
		recolorView();
	}

	private void recolorView() {
		for (int i = 0; i < SIZE; i++){
			for (int j = 0; j < SIZE; j++){
				panels.get(i*SIZE+j).setOrientation(simulation.getOrientation(i, j)>0 ? true:false);
			}
		}
		
	}

	@SuppressWarnings("unused")
	private void setUpMenuBar() {
		theMenuBar = new JMenuBar();
		file = new JMenu("File");
		about = new JMenuItem("About");
		
		file.add(about);
		theMenuBar.add(file);
		this.setJMenuBar(theMenuBar);
		
		about.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				JOptionPane.showMessageDialog(null, new JLabel("My Ising Model Project"));
			}
		});
		
	}

	public static void main (String []args){
		System.out.println("Start");
		Controller window = new Controller();
		System.out.println("Done");
	}
}
