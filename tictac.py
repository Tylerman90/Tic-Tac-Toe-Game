#TicTacToe by Tyler Gunter

print("Welcome to Tic Tac Toe!")

#Defining the board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#Defining the display board function
def display_board():
	print('  |' + '   |')
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('  |' + '   |')
	print('---------')
	print('  |' + '   |')
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('  |' + '   |')
	print('---------')
	print('  |' + '   |')
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('  |' + '   |')

display_board()

def player_input():
	while True:
		choice = input("Choose an empty space to place X.\n>>>")
		choice = int(choice)

		board[choice] = 'X'
		display_board()
player_input()

