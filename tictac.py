#TicTacToe by Tyler Gunter
import random
 
#Defining the display board function
def displayBoard(board):
	#This function prints out the board that it's passed
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
		letter = input("Do you want to be X or O?").upper()

	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']



def whoGoesFirst():
	#select the number 0 or 1, if it's 0 the player will be first.
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	# return true if the player wants to play again.
	print("Would you like to play again? (yes or no)")
	return input().lower().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	return ((bo[1] == le and bo[2] == le and bo[3] == le) 
	or (bo[4] == le and bo[5] == le and bo[6] == le) 
	or (bo[7] == le and bo[8] == le and bo[9] == le) 
	or (bo[1] == le and bo [4] == le and bo [7] == le) 
	or (bo[2] == le and bo [5] == le and bo [8] == le) 
	or (bo[3] == le and bo [6] == le and bo [9] == le) 
	or (bo[1] == le and bo [5] == le and bo [9] == le) 
	or (bo[3] == le and bo [5] == le and bo [7] == le))



def getBoardCopy(board):
	dupeBoard = []
	for i in board:
		dupeBoard.append(i)
	return dupeBoard




def isSpaceFree(board, move):
	return board[move] == ' '


def getPlayerMove(board):
	#Let the player type in their move
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print("What's your next move? (1-9)")
		move = input()
	return int(move)


def chooseRandomMoveFromList(board, movesList):
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

		if len(possibleMoves) != 0:
			return random.choice(possibleMoves)
		else:
			return None



def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	

	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	
	move = chooseRandomMoveFromList(board, [7, 9, 1, 3])
	if move != None:
		return move


	if isSpaceFree(board, 5):
		return 5


	return chooseRandomMoveFromList(board, [8, 4, 6, 2])

def isBoardFull(board):
	# Retun true if every space on the board is occupied. If not, return false
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	return True


print("Welcome to Tic Tac Toe!")

while True:
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first!')
	gameIsPlaying = True

	while gameIsPlaying:
		#Player's turn
		if turn == 'player':
			displayBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				displayBoard(theBoard)
				print("Congratulations! You won the game.")
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					displayBoard(theBoard)
					print('It is a tie!')
					break
				else:
					turn = 'computer'
		else:
			#Computer's turn.
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				displayBoard(theBoard)
				print("The computer has won!")
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					displayBoard(theBoard)
					print('It is a tie!')
					break
				else:
					turn = 'player'
	if not playAgain():
		break







			

