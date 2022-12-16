package ttt;

import java.util.Arrays;

public class TTT {
	
	public static String[] board = {"X", "*", "*", "*", "*", "*", "*", "*", "O"};
	public static int[] legalSquares = {};
	public static boolean validChoice = false;
	
	public static void clear() {
		//i hate this, it doesn't work how i want it to but as far as i'm aware it's the only way.
		for(int i = 0; i < 20; i++)
		{
		    System.out.println("\n");
		}

	}

	public static void printBoard() {
		int newlcounter = 0;
		for (int x = 0; x < board.length; x++) {
			System.out.print(board[x]);
			newlcounter++;
			if (newlcounter == 3) {
				System.out.print("\n");
				newlcounter = 0;
			}
		}
	}
	
	public static void getIndexes() {
		for (int x = 0; x < board.length; x++) {
			if (board[x] == "*") {
				//this is the dumbest thing i have seen
				legalSquares = Arrays.copyOf(legalSquares, legalSquares.length + 1);
				legalSquares[legalSquares.length - 1] = x;
			}
		}
	}
	
	public static void userTurn() {
		while (!validChoice) {
			
		}
	}
	
	public static void main(String[] args) {
		clear();
		getIndexes();
		System.out.println(Arrays.toString(legalSquares));
	}

}
