package ttt;

import java.util.Arrays;
import java.util.Scanner;
import java.util.Random;

public class TTT {
	
	public static String[] board = {"*", "*", "*", "*", "*", "*", "*", "*", "*"};
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
			Scanner userInput = new Scanner(System.in);
			System.out.print("Enter square to put your X: ");
			int userChoice = userInput.nextInt();
			userChoice--;
			
			if (board[userChoice] == "*") {
				board[userChoice] = "X";
				validChoice = true;
			} else {
				System.out.println("Square not valid or already taken.");
			}
			
		}
		validChoice = false;
	}
	
	public static void cpuTurn() {
		getIndexes();
		while (!validChoice) {
			int cpuChoice = new Random().nextInt(legalSquares.length);
			board[cpuChoice] = "O";
			validChoice = true;
		}
		validChoice = false;
	}
	
	public static void main(String[] args) {
		cpuTurn();
		printBoard();
	}

}
