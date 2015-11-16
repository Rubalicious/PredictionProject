package Model;

public class Block {
		private String ID;
		private int orientation;
		private int [] neighbors;
		private int [] pos;
		
		public Block(){
			orientation = 0;
		}
		
		public Block(int x, int y){
			ID = "";
			orientation = 0;
			pos = new int [2];//may lengthen
			pos[0] = x;
			pos[1] = y;
			neighbors = getNeighbors(x,y); 
		}
		private int[] getNeighbors(int x, int y) {
			int [] neighbor = new int [8];

			return null;
		}

		public int getOrientation(){
			return this.orientation;
		}
		public void setOrientation(int orientation){
			this.orientation = orientation;
		}
}
