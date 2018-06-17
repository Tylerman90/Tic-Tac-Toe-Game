#TicTacToe by Tyler Gunter
import random
print("Welcome to Tic Tac Toe!")
 
#Defining the display board function
def display_board(board):
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



def inputPlayerLetter():
	#Let's the player type which letter they want to play as.
	#Returns a list with the player's letter as the first item, and the computer's letter as the second.
	letter = ' '
	while not (letter == 'X' or letter == 'O'):
		letter = input("Do you want to be X or O?\n>>>").upper()

	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	#select the number 0 or 1, if it's 0 the player will be first.
	if random.randint(0, 1) == 0:
		return 'player'
	else:
		return 'computer'

def playagain():
	# return true if the player wants to play again.
	input("Would you like to play again? (yes or no)\n>>>>")
	return input.lowercase().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter

	

while True:
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first!')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			display_board(theBoard)
			input("Select your space\n>>>>")
		else:
			print("You are so Gay!")
