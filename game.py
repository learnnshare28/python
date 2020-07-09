#-------Global variable

#Game board
board = ["-", "-", "-",
         "-", "-", "-",
          "-", "-", "-"]

#If the game is stillgoing
game_is_still_going = True

#Who won? or tie?
winner = None

# Whose turn is it
current_player = "X"


def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
	#Display initial board
	display_board()

	while game_is_still_going:

		#handle a single turn of a arbitary player
		handle_turn(current_player)

		#Check if game is over
		check_if_game_over()

		#Flip to the another player
		flip_player()

	#If the game ended
	if winner == "X" or winner == "O":
		print(winner + "won.")
	elif winner == None:
		print("Tie.")


def handle_turn(player):
	print(player + "'s turn.")
	position = input("Choose a position from 1-9: ")

	valid = False
	while not valid:

		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			position = input("Invalid choice. Choose a position from 1-9: ")

		position = int(position) - 1

		if board[position] == "-":
			valid = True
		else:
			print("You can't go there,Go again.")

	board[position] = player
	display_board()


def check_if_game_over():
	check_for_winner()
	check_if_tie()


def check_for_winner():

	#Set up global variable
	global winner

	#check rows
	row_winner = check_rows()
	#check columns
	column_winner = check_columns()
	#check diagonals
	diagonal_winner = check_diagonals()

	#Get the winner
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None

	return


def check_rows():
	#Set up global variables
	global game_is_still_going
	#Check if any of  the rows have same value or (and is not empty)
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"
	#if any row does have a match,flag that there is a win
	if row_1 or row_2 or row_3:
		game_is_still_going = False
	#Return the winner(X or O)
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]

	return


def check_columns():
	#Set up global variables
	global game_is_still_going
	#Check if any of  the rows have same value or (and is not empty)
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"
	#if any column does have a match,flag that there is a win
	if column_1 or column_2 or column_3:
		game_is_still_going = False
	#Return the winner(X or O)
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	return


def check_diagonals():
	#Set up global variables
	global game_is_still_going
	#Check if any of  the rows have same value or (and is not empty)
	daigonal_1 = board[0] == board[4] == board[8] != "-"
	daigonal_2 = board[6] == board[4] == board[2] != "-"
	#if any daigonal does have a match,flag that there is a win
	if daigonal_1 or daigonal_2:
		game_is_still_going = False
	#Return the winner(X or O)
	if daigonal_1:
		return board[0]
	elif daigonal_2:
		return board[6]
	return


def check_if_tie():
	global game_is_still_going
	if "-" not in board:
		game_is_still_going = False
	return


def flip_player():
	#global variable we need
	global current_player
	#if the current player was X, then changed it to 0
	if current_player == "X":
		current_player = "0"
	#if the current player was 0,then changed it to X
	elif current_player == "0":
		current_player = "X"

	return


play_game()
