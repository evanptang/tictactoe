Tic Tac Toe-Read Me
By Evan Tang

This project has two primary purposes:
  1. Provide the player with an computer opponent for Tic Tac Toe where the best
  they can do is to tie
  2. Upon request, analyze whether the board is already winnable.

Both directives use the minimax algorithm which is ideal for adversarial zero-
sum two player games like tic tac toe. Additionally, a modification of minimax
which trims the solution space is used under the name alpha beta pruning

For further information on the files see below
  -main.py: executes the actual commands. No functions stored here
  -all_functions.py: the definitions for the functions utilizing minimax and
  ab pruning as well as their helper functions.
  -common.py: shared definitions.
All Rights Reserved Evan Tang 2019.
