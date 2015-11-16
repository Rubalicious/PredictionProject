package Model;
import static org.junit.Assert.*;

import org.junit.Test;


public class IsingModelTest {
//tests are working
	@Test
	public void test() {
		IsingModel board = new IsingModel(100);
		System.out.println(board.toString());
	}
	
	@Test
	public void testSetStateAndGetOrientation(){
		int [][] state = {		{1,0,1},
								{0,0,1},
								{0,1,1}			};
		IsingModel board = new IsingModel(state);
		
		assertEquals(1, board.getOrientation(0, 0));
		assertEquals(0, board.getOrientation(0, 1));
		assertEquals(1, board.getOrientation(0, 2));
		
		assertEquals(0, board.getOrientation(1, 0));
		assertEquals(0, board.getOrientation(1, 1));
		assertEquals(1, board.getOrientation(1, 2));
		
		assertEquals(0, board.getOrientation(2, 0));
		assertEquals(1, board.getOrientation(2, 1));
		assertEquals(1, board.getOrientation(2, 2));
	}
	
	@Test
	public void testGetNeighbors(){
		int [][] state = {		{1,0,1,0},
								{0,0,1,1},
								{0,1,1,0},
								{0,1,0,0}		};
		IsingModel board = new IsingModel(state);
		
		int [] neighbors = {1,0,1,0,1,0,1,1};
		assertEquals(0, board.getOrientation(1, 1));
		assertEquals(neighbors[0], board.getNeighborList(1, 1)[0]);
		assertEquals(neighbors[1], board.getNeighborList(1, 1)[1]);
		assertEquals(neighbors[2], board.getNeighborList(1, 1)[2]);
		assertEquals(neighbors[3], board.getNeighborList(1, 1)[3]);
		assertEquals(neighbors[4], board.getNeighborList(1, 1)[4]);
		assertEquals(neighbors[5], board.getNeighborList(1, 1)[5]);
		assertEquals(neighbors[6], board.getNeighborList(1, 1)[6]);
		assertEquals(neighbors[7], board.getNeighborList(1, 1)[7]);
		
		int [] neighbors1 = {0,1,0,0,1,1,1,0};
		assertEquals(1, board.getOrientation(1, 2));
		assertEquals(neighbors1[0], board.getNeighborList(1, 2)[0]);
		assertEquals(neighbors1[0], board.getNeighborList(1, 2)[0]);
		assertEquals(neighbors1[1], board.getNeighborList(1, 2)[1]);
		assertEquals(neighbors1[2], board.getNeighborList(1, 2)[2]);
		assertEquals(neighbors1[3], board.getNeighborList(1, 2)[3]);
		assertEquals(neighbors1[4], board.getNeighborList(1, 2)[4]);
		assertEquals(neighbors1[5], board.getNeighborList(1, 2)[5]);
		assertEquals(neighbors1[6], board.getNeighborList(1, 2)[6]);
		assertEquals(neighbors1[7], board.getNeighborList(1, 2)[7]);
	}
	
	@Test
	public void testGetNeighborsWithWrapAround(){
		int [][] state = {		{1,0,1,0},
								{0,0,1,1},
								{0,1,1,0},
								{0,1,0,0}		};
		IsingModel board = new IsingModel(state);
		
		int [] neighbors = {0,0,1,0,0,1,0,0};
		assertEquals(1, board.getOrientation(0, 0));
		assertEquals(neighbors[0], board.getNeighborList(0, 0)[0]);
		assertEquals(neighbors[1], board.getNeighborList(0,0)[1]);
		assertEquals(neighbors[2], board.getNeighborList(0,0)[2]);
		assertEquals(neighbors[3], board.getNeighborList(0,0)[3]);
		assertEquals(neighbors[4], board.getNeighborList(0,0)[4]);
		assertEquals(neighbors[5], board.getNeighborList(0,0)[5]);
		assertEquals(neighbors[6], board.getNeighborList(0,0)[6]);
		assertEquals(neighbors[7], board.getNeighborList(0,0)[7]);
		
		int [] neighbors1 = {1,1,0,1,0,0,1,0};
		assertEquals(0, board.getOrientation(3, 2));
		assertEquals(neighbors1[0], board.getNeighborList(3, 2)[0]);
		assertEquals(neighbors1[1], board.getNeighborList(3, 2)[1]);
		assertEquals(neighbors1[2], board.getNeighborList(3, 2)[2]);
		assertEquals(neighbors1[3], board.getNeighborList(3, 2)[3]);
		assertEquals(neighbors1[4], board.getNeighborList(3, 2)[4]);
		assertEquals(neighbors1[5], board.getNeighborList(3, 2)[5]);
		assertEquals(neighbors1[6], board.getNeighborList(3, 2)[6]);
		assertEquals(neighbors1[7], board.getNeighborList(3, 2)[7]);
	}
	
	@Test
	public void testCalculateHamiltonian(){
		int [][] state = {		{1,0,1,0},
								{0,0,1,1},
								{0,1,1,0},
								{0,1,0,0}		};
		IsingModel board = new IsingModel(state);
		
		assertEquals(5, board.calculateHamiltonian(1, 1));
		board.setOrientation(1, 1, 1);
		assertEquals(3, board.calculateHamiltonian(1, 1));
	}
	
	@Test
	public void testCalculateChangeInEnergy(){
		int [][] state = {		{1,0,1,0},
								{0,0,1,1},
								{0,1,1,0},
								{0,1,0,0}		};
		IsingModel board = new IsingModel(state);
		
		if(board.changeInEnergy(1,1).nOrientation == 0){
			assertEquals(0, board.changeInEnergy(1,1).delta);
		}
		else if(board.changeInEnergy(1, 1).nOrientation == 1){
			assertEquals(-2, board.changeInEnergy(1,1).delta);
		}
		
	}
	
	@Test
	public void testAcceptanceDecision(){
		int [][] state = {		{1,0,1,0},
								{0,0,1,1},
								{0,1,1,0},
								{0,1,0,0}		};
		IsingModel board = new IsingModel(state);
		
		assertTrue(board.acceptDecision(1,1));
	}

}
