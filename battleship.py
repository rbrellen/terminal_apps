#!/usr/bin/python

# Import modules
import numpy as np

# Create Board and Ship classes
class Board:
	"""Creates class of type Board"""
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.shape = np.full(shape = (width, length), fill_value = ' ', dtype = 'S10')
		self.spaces = length * width
		self.spaces_available = np.count_nonzero(self == ' ')
		self.hits = np.count_nonzero(self == 'x')
		self.life_remaining = np.count_nonzero(self == '+')
		self.misses = np.count_nonzero(self == '+')

class Ship:
	"""Creates class of type Ship"""
	def __init__(self, length):
		self.length = length
		self.life = length
		self.location = list()

# Define variables for use later
board_1 = None
aircraft_carrier_1 = Ship(5)
battleship_1 = Ship(4)
submarine_1 = Ship(3)
cruiser_1 = Ship(3)
destroyer_1 = Ship(2)

board_2 = None
aircraft_carrier_2 = Ship(5)
battleship_2 = Ship(4)
submarine_2 = Ship(3)
cruiser_2 = Ship(3)
destroyer_2 = Ship(2)

# Define create boards function
def create_boards(length, width):
	global board_1
	global board_2
	board_1 = Board(length, width)
	board_2 = Board(length, width)

# Define place ship function
def place_ship (player, ship):
	# Determine which player has been selected
	if player == 1:
		board = board_1
	elif player == 2:
		board = board_2
	while True: 
		direction = raw_input('Place your ship (v)ertical or (h)orizontal. ')
		if direction == 'v' or direction == 'h':
			break
		else:
			print('Please choose v for vertical placement or h for horizontal placement.')
	row = -1
	column = -1
	if direction == 'v':
		while	row < 0 or row + ship.length + 1 > board.length:
			row = raw_input('\nChoose the top row for your ship.\nNOTE: First row = 0. Last possible row = ' + str(board.length - ship.length) + '.\n\nRow: ')
			try:
				row = int(row)
			except:
				row = -1
			if row < 0 or row + ship.length + 1 > board.length:
				print('Please choose a positive integer value (0 to ' + str(board.length - ship.length) + ') that allows your ship to fit on the board.')
			else:
				print('ACCEPTED')
		while	column < 0 or column + 1 > board.width:
			column = raw_input('\nChoose the column for your ship.\nNOTE: First column = 0. Last column = ' + str(board.width - 1) + '.\n\nColumn: ')
			try:
				column = int(column)
			except:
				column = -1
			if column < 0 or column + 1 > board.width:
				print('\nPlease choose a positive integer value (0 to ' + str(board.width - 1) + ') that allows your ship to fit on the board.')
			else:
				print('ACCEPTED')
		for i in range(ship.length):
			ship.location.append((row + i, column))
		print('Your ship is located in the following spaces: ' + str(ship.location).strip('[]'))
	if direction == 'h':
		while	column < 0 or column + ship.length + 1 > board.width:
			column = raw_input('\nChoose the leftmost column for your ship.\nNOTE: First column = 0. Last column = ' + str(board.width - 1) + '.\n\nColumn: ')
			try:
				column = int(column)
			except:
				column = -1
			if column < 0 or column + ship.length + 1 > board.width:
				print('\nPlease choose a positive integer value (0 to ' + str(board.width - ship.length) + ') that allows your ship to fit on the board.')
			else:
				print('ACCEPTED')
		while	row < 0 or row + 1 > board.length:
			row = raw_input('\nChoose the row for your ship.\nNOTE: First row = 0. Last row = ' + str(board.length - 1) + '.\n\nRow: ')
			try:
				row = int(row)
			except:
				row = -1
			if row < 0 or row + 1 > board.length:
				print('\nPlease choose a positive integer value (0 to ' + str(board.length - 1) + ') that allows your ship to fit on the board.')
			else:
				print('ACCEPTED')
		for i in range(ship.length):
			ship.location.append((row, column + i))
		print('Your ship is located in the following spaces: ' + str(ship.location).strip('[]'))

####################
####################
#### START GAME ####
####################
####################

board_length = int(raw_input('How many rows should the board have? '))
board_width = int(raw_input('How many columns should the board have? '))
create_boards(board_length, board_width)

player_1_ships = ['(a)ircraft carrier', '(b)attleship', '(s)ubmarine', '(c)ruiser', '(d)estroyer']
player_2_ships = ['(a)ircraft carrier', '(b)attleship', '(s)ubmarine', '(c)ruiser', '(d)estroyer']

while len(player_1_ships) > 0 or len(player_2_ships) > 0:
	player = int(raw_input('Select player (1 or 2): '))
	selection = None
	if player == 1:
		if len(player_1_ships) == 0:
			print('All of the ships for Player 1 have been placed')
		else:
			print('Remaining ships for Player 1: \n')
			for ship in player_1_ships:
				print ship
			while selection not in player_1_ships:
				selection = raw_input('Which ship would you like to place?\n\nShip: ')
				if selection == 'a':
					selection = '(a)ircraft carrier'
					ship = aircraft_carrier_1
				elif selection == 'b':
					selection = '(b)attleship'
					ship = battleship_1
				elif selection == 's':
					selection = '(s)ubmarine'
					ship = submarine_1
				elif selection == 'c':
					selection = '(c)ruiser'
					ship = cruiser_1
				elif selection == 'd':
					selection = '(d)estroyer'
					ship = destroyer_1
				else:
					print('Not a valid selection. Try again by choosing the first letter of the ship you would like to place.')
					selection = None
					ship = None
			if selection in player_1_ships:
					player_1_ships.remove(selection)
			place_ship(player, ship)
	if player == 2:
		if len(player_2_ships) == 0:
			print('All of the ships for Player 2 have been placed')
		else:
			print('Remaining ships for Player 2: \n')
			for ship in player_2_ships:
				print ship
			while selection not in player_2_ships:
				selection = raw_input('Which ship would you like to place?\n\nShip: ')
				if selection == 'a':
					selection = '(a)ircraft carrier'
					ship = aircraft_carrier_2
				elif selection == 'b':
					selection = '(b)attleship'
					ship = battleship_2
				elif selection == 's':
					selection = '(s)ubmarine'
					ship = submarine_2
				elif selection == 'c':
					selection = '(c)ruiser'
					ship = cruiser_2
				elif selection == 'd':
					selection = '(d)estroyer'
					ship = destroyer_2
				else:
					print('Not a valid selection. Try again by choosing the first letter of the ship you would like to place.')
					selection = None
					ship = None
			if selection in player_2_ships:
					player_2_ships.remove(selection)
			place_ship(player, ship)
