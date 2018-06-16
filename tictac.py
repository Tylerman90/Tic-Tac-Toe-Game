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
	#Let's the player type which letter they want to be.
	#Returns a list with the player's letter as the first item, and the computer's letter as the second.
	letter = ' '
	while not (letter == 'X' or letter == 'O'):
		letter = input("Do you want to be X or O?\n>>>").upper()

	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():

board = [' '] * 10
playerLetter, computerLetter = inputPlayerLetter()