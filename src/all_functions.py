import common

#There are the three main functions necessary for minmax_tictactoe
#	-minmax_tictactoe
#	-x_function
#	-o_function

def minmax_tictactoe (board, turn):
	value = 0
	if turn == 1:
		value = x_function(board)
	else:
		value = o_function(board)
	return value

def x_function (board):
	array = []
	initial = common.game_status(board)
	if initial != 0:
		return initial
	elif full(board):
		return 0
	else:
		successor = get_all(board,1)
		for index in range(len(successor)):
			array.append(o_function(successor[index]))
		marker = 2
		for a in range(len(array)):
			if array[a] == 1:
				marker = 1
		if marker == 2:
			for a in range (len(array)):
				if array[a] == 0:
					marker = 0
		return marker

def o_function (board):
	array = []
	initial = common.game_status(board)
	if initial != 0:
		return initial
	elif full(board):
		return 0
	else:
		successor = get_all(board,2)
		for index in range(len(successor)):
			array.append(x_function(successor[index]))
		marker = 1
		for a in range(len(array)):
			if array[a] == 2:
				marker = 2
		if marker == 1:
			for a in range (len(array)):
				if array[a] == 0:
					marker = 0
		return marker

#There are the three main functions necessary for abprun_tictactoe
#	-abprun_tictactoe
#	-mm
#	-init_to_return

def abprun_tictactoe(board, turn):
	test = mm(board, turn, common.neg_inf(), common.pos_inf())
	test =  init_to_return(test)
	return test

def mm (board, turn, a, b):
	b = isdone(board, turn)
	if b != 10:
		return b
	max = -2
	children = get_all(board,turn)
	for index in range(len(children)):
		result = - mm(children[index], opposite_turn(turn), b, a)
		if result > max:
			max = result
		if max >= b  or max == 1:
			return max
		if max > a:
			a = max
	return max

def init_to_return (num):
	if num == 1:
		return 1
	elif num == -1:
		return 2
	else:
		return 0

#The following helper functions are used:
#	-get_all: All possible boards
#	-full: Is the board full already?
#	-opposite_turn: Changes the player
#	-isDone: Returns a value if the board is full

def get_all (board, turn):
	array = []
	b_x = board[:]
	b_y = board[:]
	for y in range(3):
		for x in range(3):
			if b_x[y*3 + x] == 0:
				b_x[y*3 +x] = turn
				array.append(b_x)
				b_x = b_y[:]
	return array

def full (board):
	for x in range(9):
		if board[x] == 0:
			return False
	return True

def opposite_turn(turn):
	if turn == 1:
		return 2
	else:
		return 1

def isdone( board, turn):
	gs = common.game_status(board)
	if gs != 0:
		if turn == gs:
			return 1
		else:
			return -1
	else:
		if full(board):
			return 0
		else:
			return 10
