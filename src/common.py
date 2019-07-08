class constants:
	NONE = 0
	X = 1
	O = 2

class variables:
	explored=0

def print_board(board):
	print(simbol(board[0])+"|"+simbol(board[1])+"|"+simbol(board[2]));
	print("-----")
	print(simbol(board[3])+"|"+simbol(board[4])+"|"+simbol(board[5]));
	print("-----")
	print(simbol(board[6])+"|"+simbol(board[7])+"|"+simbol(board[8]));

def set_board(map, data):
	for y in range(9):
		map[y]=constants.X if data[y]=='X' else constants.O if data[y]=='O' else constants.NONE;

def set_cell(b, y, x, s):
	b[y*3+x]=s

def get_cell(b, y,x):
	return b[y*3+x];

def simbol(c):
	if (c==constants.X):
		return 'X'
	if (c==constants.O):
		return 'O'
	return ' '

def legend(c):
	if (c==constants.X):
		return "X"
	if (c==constants.O):
		return "O"
	return "Nobody"

def game_status(board):
	variables.explored+=1
	#diags
	if (board[0]==constants.X and board[4]==constants.X and board[8]==constants.X):
		return constants.X
	if (board[2]==constants.X and board[4]==constants.X and board[6]==constants.X):
		return constants.X

	#horizontal
	if (board[0]==constants.X and board[1]==constants.X and board[2]==constants.X):
		return constants.X
	if (board[3]==constants.X and board[4]==constants.X and board[5]==constants.X):
		return constants.X
	if (board[6]==constants.X and board[7]==constants.X and board[8]==constants.X):
		return constants.X

	#vertical
	if (board[0]==constants.X and board[3]==constants.X and board[6]==constants.X):
		return constants.X
	if (board[1]==constants.X and board[4]==constants.X and board[7]==constants.X):
		return constants.X
	if (board[2]==constants.X and board[5]==constants.X and board[8]==constants.X):
		return constants.X

	#diags
	if (board[0]==constants.O and board[4]==constants.O and board[8]==constants.O):
		return constants.O
	if (board[2]==constants.O and board[4]==constants.O and board[6]==constants.O):
		return constants.O

	#horizontal
	if (board[0]==constants.O and board[1]==constants.O and board[2]==constants.O):
		return constants.O
	if (board[3]==constants.O and board[4]==constants.O and board[5]==constants.O):
		return constants.O
	if (board[6]==constants.O and board[7]==constants.O and board[8]==constants.O):
		return constants.O

	#vertical
	if (board[0]==constants.O and board[3]==constants.O and board[6]==constants.O):
		return constants.O
	if (board[1]==constants.O and board[4]==constants.O and board[7]==constants.O):
		return constants.O
	if (board[2]==constants.O and board[5]==constants.O and board[8]==constants.O):
		return constants.O

	return constants.NONE#tie or unfinished
def neg_inf():
	return -1*float("inf")
def pos_inf():
	return float("inf")
