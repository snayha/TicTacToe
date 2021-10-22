#!/usr/bin/python
import random

class TicTacToe:

	#game logistics and setup

	def __init__(self):
		board = []

	def makeBoard(self):
		return  ["_"]*9

	def visualBoard(self,board):
		print(board[0]+" | "+board[1]+" | "+board[2]+"\n---------\n"+board[3]+" | "+board[4]+" | "+board[5]+"\n---------\n"+board[6]+" | "+board[7]+" | "+board[8])

	def boardSchematic(self):
		print("0 | 1 | 2 \n---------\n3 | 4 | 5\n---------\n6 | 7 | 8")

	def choose_player(self):
		if random.randint(0,1) == 0:
			return "Computer"
		else:
			return "Player"

	def inputLetter(self):
		letter = ' '
		while not (letter == "X" or letter == "O"):
			print("Choose X or O please")
			letter = raw_input().upper()

		return letter


	def checkWin(self,board, player):
		return ((board[0]==player and board[1]==player and board[2]==player) or 
				(board[3]==player and board[4]==player and board[5]==player) or 
				(board[6]==player and board[7]==player and board[8]==player) or 
				(board[0]==player and board[3]==player and board[6]==player) or
				(board[1]==player and board[4]==player and board[7]==player) or
				(board[2]==player and board[5]==player and board[8]==player) or
				(board[0]==player and board[4]==player and board[8]==player) or
				(board[2]==player and board[4]==player and board[6]==player))

	def assignPlayers(self, player):
		return "X" if player == "O" else "O"

	def switchPlayers(self, inPlay):
		return "O" if inPlay == "X" else "X"

	def assignLetterToPlayer(self,inPlay,player,computer):
		if inPlay == "Player":
			return player 
		else: return computer

	#running the game

	def pickSpot(self,board,player):
		spot = ' '
		while spot not in [0,1,2,3,4,5,6,7,8] or not self.isSpaceEmpty(board,spot):
			print("Choose a spot 0 to 8")
			spot = int(raw_input())
			# if int(x):
			# 	spot = int(x)
			# else:
			# 	spot = ' '
		
		board[spot] = player

	def computerPick(self, board, player):
		for i in range(0,9): #can Computer win?
			if self.isSpaceEmpty(board, i):
				board[i] = player
				if self.checkWin(board, player):
					return i
				else :
					board[i] = "_"

		for i in range(0,9): #can I block player
			if self.isSpaceEmpty(board, i):
				board[i] = self.switchPlayers(player)
				if self.checkWin(board, self.switchPlayers(player)):
					board[i] = player
					return i
				else :
					board[i] = "_"

		cornerSpot = random.choice([0,2,6,8])
		if self.isSpaceEmpty(board, cornerSpot):
			board[cornerSpot] = player
			return cornerSpot

		if self.isSpaceEmpty(board, 4):
			board[4] = player
			return 4

		randomSpot = random.choice([1,3,5,7])
		if self.isSpaceEmpty(board, randomSpot):
			board[randomSpot] = player
			return randomSpot

	def playAgain(self):
		play = " "
		while not (play == "Y" or play == "N"): 
			print("Do you want to play again? Y/N")
			play = raw_input().upper()
		
		if play == "Y":
			return True
		else:
			return False

	#checking board status

	def isSpaceEmpty(self, board, space):
		return board[space] == "_"

	def isFull(self, board):
		for i in board:
			if i == "_":
				return False
		return True
	
	#Game Run
	def runGame(self):
		board = self.makeBoard()
		player = self.inputLetter()
		computer = self.assignPlayers(player)

		print("You chose " + player + " so I will be " + computer)
		inPlayName = self.choose_player()
		inPlay = self.assignLetterToPlayer(inPlayName,player,computer)

		print(inPlay + " is first")
		print("The board will look like this, enter the spot for your given move")
		self.boardSchematic()
		print("The current empty board")
		self.visualBoard(board)
		print("\n")
		
		replay = False

		while True:
			if replay:
				board = self.makeBoard()
				player = self.inputLetter()
				computer = self.assignPlayers(player)
				print("You chose " + player + " so I will be " + computer)
				inPlayName = self.choose_player()
				inPlay = self.assignLetterToPlayer(inPlayName,player,computer)
				self.visualBoard(board)
				replay = False

			if inPlay == player: 
				self.pickSpot(board,inPlay)
				self.visualBoard(board)
				print("\n")

				if self.checkWin(board,inPlay):
					print("sorry as the computer it looks like you cheated and must forfit the game")
					replay = self.playAgain()
					if not replay:
						break
				else:
					if self.isFull(board):
						print("No one has one, therefore you have lost")
						replay = self.playAgain()
						if not replay:
							break
					else:
						inPlay = self.switchPlayers(inPlay)
			else:
				self.computerPick(board, inPlay)
				self.visualBoard(board)
				print("\n")

				if self.checkWin(board,inPlay):
					print("I am victorious, bow down to me you fool!")
					replay = self.playAgain()
					if not replay:
						break
				else:
					if self.isFull(board):
						print("No one has one, therefore you have lost")
						replay = self.playAgain()
						if not replay:
							break
					else:
						inPlay = self.switchPlayers(inPlay)
		


# starting the game
game = TicTacToe()
game.runGame()

