package View;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentEvent;
import java.awt.event.ComponentListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.Timer;

import Model.IsingModel;



@SuppressWarnings("serial")
public class Controller extends JFrame {
//	GLOBAL VARIABLES <-- global variables are "static"
//	changed everything to class variables,
//	which are instantiated in the constructor.
//	Don't mix them up and try to instantiate class variables outside of constructor!
	private class GridPanel extends Component {
		private boolean up;
		public GridPanel(){
			super();
			setSize(5,5);
			up=false;
		}
		public void setOrientation(boolean u){
			up = u;
		}
		
		@Override
		public void paint(Graphics g){
			g.setColor(up ? Color.YELLOW:Color.BLUE);
			g.fillRect(0,0, (int)getSize().getWidth(), (int)getSize().getHeight());
		}
	}
	/*
	 * We want the animation to be in a thread. It's the "center
	 * of attention" for the thread created by actionPerformed in runButton. 
	 * This means the run sequence is to start the repaintTimer 
	 * (separate timer thread), let our animation run on runButton's thread, and 
	 * exit the runButton thread when we're done.
	 */
	private Thread t;
//	the Timer to track when to refresh
	private Timer repaintTimer;
	private static int SIZE = 500;
	private IsingModel simulation;
	private JPanel view;
	private ArrayList<GridPanel> panels;
	
	//The menu bar
	private JMenuBar theMenuBar;
	private JMenu file;
	private JMenuItem about;
	/*
	 * So you want to keep as few moving pieces as possible. (Java is
	 * very complicated when it comes to painting.) You cannot change
	 * references to components in a container and expect them to get
	 * painted. Hence, the GridPanel class above that contains logic
	 * for painting itself, and we'll keep track of them in an arraylist.
	 */
	
	//Constructor
	public Controller(){
		super("Ising Model Simulation");
		this.setSize(new Dimension(SIZE,SIZE));
		this.setResizable(false);
		this.setVisible(true);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		
		/*
		 * TODO: modify count and thread.sleep values to control
		 * break between steps and the length of the run animation.
		 */
		t = new Thread(new Runnable(){
			public void run(){
				int count = 0;
				while (count<1000) {
					try {
						step();
						count++;
						Thread.sleep(10);
					} catch (InterruptedException e) {
						System.err.println("Animation thread interrupted while sleeping:");
						System.err.println(e.getMessage());
					}
				}
			}
		});

		repaintTimer = new Timer(100, new ActionListener(){
			public void actionPerformed(ActionEvent e){
				repaint();
			}
		});
		simulation = new IsingModel(SIZE);
		// The GridLayout should be the same size as the ising model
		view = new JPanel(new GridLayout(SIZE,SIZE));
		panels = new ArrayList<GridPanel>();
		

//		int sizeOfRunButton = 73;
		
//		this.setBackground(Color.YELLOW);
//		setLocation(200, 100);
//		setLayout(new BorderLayout());
//		setSize(new Dimension(SIZE,SIZE));
		
		
		
		// initializing view
		setUpView();
		
		// final is fine here, it means you won't reassign 
		// the variable name to a different object
		final JButton runButton = new JButton("run");

		//add in a dropdown box for pixels
		
		runButton.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				try {
					runButton.setText("pause");
					repaintTimer.start(); // put timer on a new thread
					t.join(); // here we wait for the thread to animate
					repaintTimer.stop(); // and stop worring about repainting
					runButton.setText("run");
				} catch (InterruptedException e1) {
					System.err.println("Animation thread interrupted:");
					System.err.println(e1.getMessage());
					runButton.setText("run");
				}
			}
		});
		
// To be added: commented out for now until slider actions are implemented.
//		Consider instead of a full ComponentListener searching for a lighter-
//		weight class to use specifically for sliders.
//		JSlider slider = new JSlider();
//		slider.addComponentListener(new ComponentListener(){
//			@SuppressWarnings("unused")
//			public void actionPerformed(ActionEvent e){
//				
//			}
//		});
//		
//		add(slider, BorderLayout.SOUTH);
		add(view);
		add(runButton);
		
		pack();
		
		
		

	}
	
	private void setUpMenuBar() {
		//the menu bar
		theMenuBar = new JMenuBar();
		file = new JMenu("File");
		about = new JMenuItem("about");
		
		//adding responsiveness to the menu bar
		about.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				JOptionPane.showMessageDialog(null, new JLabel("some string"));
			}
		});
		file.add(about);
		theMenuBar.add(file);
		this.setJMenuBar(theMenuBar);
	}

	private void setUpView() {
		for (int i = 0; i < SIZE; i ++){
			for (int j = 0; j < SIZE; j++){
				// we don't need this variable name after
				// this if we're smart and grab by index
				GridPanel no_ref = new GridPanel();
				view.add(no_ref);
				panels.add(no_ref);
			}
		}
		recolorView();
	}
	/*
	 * TODO: check over this code to make sure it is selecting
	 * the right panel from the ising model and correctly 
	 * computing up or down orientation. Here, i is row and j
	 * is column, and the JPanel GridLayout reads from L-R then U-D.
	 */
	private void recolorView(){
		for (int i = 0; i < SIZE; i ++){
			for (int j = 0; j < SIZE; j++){
				panels.get(i*SIZE+j).
				setOrientation(simulation.getOrientation(i,j)>0 ? true:false);
			}
		}
	}
	/*
	 * I'm not sure what to do here with the acceptDecision boolean
	 * here, if that's supposed to change something in the controller
	 * or if we can assume everything will change in the IsingModel 
	 * (if so, why return something?)
	 */
	private void step(){
		simulation.step();
		recolorView();
	}

	public static void main (String [] args){
		Controller q = new Controller();
	}
	
}

