# Red-Blue-Nim

This program implements a variant of the Nim game called "Red-Blue Nim," where there are two piles of marbles: one red and one blue. The game involves two players (a human and a computer) who take turns removing one marble from either the red or blue pile. The objective is to avoid taking the last marble. The computer uses the Minimax algorithm with alpha-beta pruning to decide its moves.

Here is a detailed breakdown of the code:

Key Functions and Their Roles:
- next(st):
  
Generates the next possible states from the current state st.
If the number of red marbles is less than the number of blue marbles, it suggests removing one red marble.
Otherwise, it suggests removing one blue marble.
- term_st(st):

Checks if the game has reached a terminal state (i.e., one of the piles is empty).
- getnextmove(st, d):

Determines the best next move for the computer using the Minimax algorithm with a specified depth d.
Calls minmax_ab to evaluate the utility of each possible move and selects the move with the highest utility.
- minmax_ab(st, d, a, b, ismax):

Implements the Minimax algorithm with alpha-beta pruning.
st: Current state.
d: Depth limit.
a and b: Alpha and beta values for pruning.
ismax: Boolean indicating whether the current move is maximizing or minimizing the utility.
- util(st):

Calculates the utility value of a state st using the formula 2 * st[0] + 3 * st[1].
This utility function gives different weights to red and blue marbles.

Main Game Logic

Initial Setup:

Reads the number of red marbles (num_r), blue marbles (num_b), the first player (player1), and the depth (d) from the command line arguments.

Game Loop:

Alternates turns between the computer and the human player.
On the computer's turn, it uses getnextmove to find the best move and updates the state.
On the human's turn, it prompts the user to choose a pile to remove a marble from and updates the state accordingly.

Termination and Winning Condition:

- The game loop continues until a terminal state is reached (one of the piles is empty).
- The player who forces the other player to take the last marble wins.
- The utility value of the terminal state is calculated and displayed along with the winner.
- Running the Program
- The program is executed from the command line with the following arguments:

How to Run the application:

python red_blue_nim.py num_r num_b [player1] [d]
num_r: Number of red marbles.
num_b: Number of blue marbles.
player1 (optional): The first player ("human" or "computer"). Defaults to "computer" if not provided.
d (optional): Depth limit for the Minimax algorithm. Defaults to no limit if not provided.

Example Command:

python red_blue_nim.py 5 3 human 3
This starts a game with 5 red marbles and 3 blue marbles, where the human goes first and the Minimax algorithm has a depth limit of 3.
