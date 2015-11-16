
import java.util.Random;
import java.util.Scanner;


public class IsingModel {
	private class block{

		private int orientation;
		
		public block(){
			orientation = 0;
		}
	}
	
	private block [][] state;
	private Random generator = new Random();
	private int size;
	private int temperature;
	
	public IsingModel(int n){
		size = n;
		state = setState(n);//square default size = 10
	}
	public IsingModel(int [][] matrix){
		state = setState(matrix);//square default size = 10
	}
	private block[][] setState(int n) {
		state = new block[n][n];
		for(int i = 0; i < state.length; i ++){
			for(int j = 0; j <state[0].length; j ++){
				state[i][j] = new block();
				//state[i][j].ID = ""+cellTypes.A;
				state[i][j].orientation = (int) (Math.random()*2);
			}
		}
		return state;
	}
	
	private block[][] setState(int [][] matrix) {
		state = new block[matrix.length][matrix[0].length];
		for(int i = 0; i < state.length; i ++){
			for(int j = 0; j <state[0].length; j ++){
				state[i][j] = new block();
				//state[i][j].ID = ""+cellTypes.A;
				state[i][j].orientation = matrix[i][j];
			}
		}
		return state;
	}
	
	private block[][] getState(){
		return state;
	}
	
	@Override
	public String toString(){
		String result = "";
		for(int i = 0; i < state.length; i++){
			for(int j = 0; j < state[0].length; j++){
				result += state[i][j].orientation;
			}
			result+="\n";
		}
		return result;
	}
	
	public int getOrientation(int x, int y){
		return state[x][y].orientation;
	}
	
	public void setOrientation(int x, int y, int newOrientation){
		state[x][y].orientation = newOrientation;
	}
	//consider return an arraylist<neighbours>
	public int[] getNeighborList(int x, int y){
		int neighbors[] = new int[8];
		int length = 0;
		for(int i = x-1; i < x+2; i++){
			for (int j = y-1; j < y+2; j++){
				if(!(x==i && y==j)){
					int xtemp = (i+state.length)%state.length;
					int ytemp = (j+state[0].length)%state[0].length;
					neighbors[length] = getOrientation(xtemp,ytemp);
					length++;
				} 
			}
		}
		return neighbors;
	}
	
	public int calculateHamiltonian(int x, int y){
		int hamiltonian = 0;
		int neighbors [] = getNeighborList(x,y);
		for(int i = 0; i < neighbors.length; i ++){
			if(getOrientation(x,y) != neighbors[i]) hamiltonian++;
		}
		return hamiltonian;
	}
	
	public class packet{
		public int nOrientation;
		public int delta;
	}
	
	private int original;
	
	public packet changeInEnergy(int x, int y) {
		packet p = new packet();
		int init = calculateHamiltonian(x,y);
		
		int nl = getNeighborList(x,y).length; 
		int randomNeighbour = (int) generator.nextInt(8);
		original = getOrientation(x,y);
		int orientationOfNeighbour = getNeighborList(x,y)[randomNeighbour];
		p.nOrientation = orientationOfNeighbour;
		if(original == orientationOfNeighbour){
			p.delta = 0;
			return p;
		}
		else{
			 setOrientation(x,  y, orientationOfNeighbour);
		}
		
		int fina = calculateHamiltonian(x,y);
		p.delta = fina - init;
		return p;
	}
	
//	private void changeValue(int x, int y, int celltype){
//		if(getOrientation(x,y)==0) setOrientation(x,y, 1);
//		if(getOrientation(x,y)==1) setOrientation(x,y, 0);
//	}
	
	public boolean acceptDecision(int x, int y){
		double probability = 0.0;
		double randomVariable = (double) Math.random();
		int delta = changeInEnergy(x,y).delta;
		if(delta<=0) return true;
		else{
			probability = Math.exp(-delta);
			if(probability < randomVariable){
				setOrientation(x,y, notOriginal());
				return true;
			}
			else{
				setOrientation(x,y, original);
				return false;
			}
		}
	}
	
	private int notOriginal() {
		if (original == 1){
			return 0;
		}
		else{
			return 1;
		}
		
	}
	public int size(){
		return size;
	}
	public void changedOrientation(int x, int y) {
		if (this.acceptDecision(x, y)){
			if(this.getOrientation(x, y) == 1){
				this.setOrientation(x, y, 0);
			}
			else{
				this.setOrientation(x, y, 1);
			}
		}
	}
	
	public static void main (String []args){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter integer parameter: ");
		int n = scan.nextInt();
		IsingModel example = new IsingModel (n);
		System.out.println("I'm testing out my board\n");
		System.out.println("==========================");
		System.out.println(example.toString());
		System.out.println("I'm testing to see if this edit works from my phone\n");
		
		for (int i = 0; i < 10; i ++){
			int x = (int)(Math.random()*example.size());
			int y = (int)(Math.random()*example.size());
			System.out.println("("+x+","+y+") accepted: "+example.acceptDecision(x, y));
			example.changedOrientation(x,y);
//			example.setOrientation(x, y, newOrientation);
		}
		System.out.println("\n"+example.toString());

	}
	
	

}
