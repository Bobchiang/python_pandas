import random

class Game():

	def __init__(self):
		self._score = 0
		self._steps = 0
		self._m = []
		self._stopGame = False

		for i in range(4):
			self._m.append([0,0,0,0])

	def getStopGame(self):
		return self._stopGame

	def setGoal(self, goal):
		self._goal = goal

	def add_random_block(self):

		while True:
			row = random.randint(0, 3)
			column = random.randint(0, 3)
			if self._m[row][column] == 0:
				self._m[row][column] = 2
				break

	def printMatrix(self):
		for i in range(4):
			for j in range(4):
				print('%5d' % self._m[i][j], end='')
			if i <= 2:
				print(',')
			else:
				print('')

	def moveUp(self):
		self._global_moved = False
		moved = False
		# move
		for i in range(1, 4):
			for j in range(4):
				x = i
				if self._m[i][j] != 0:
					while x >= 1 and self._m[x-1][j] == 0:
						x = x - 1
						moved = True
						self._global_moved = True
					if moved:
						self._m[x][j] = self._m[i][j]
						self._m[i][j] = 0
						moved = False

		# merge
		points = 0
		for i in range(1, 4):
			for j in range(4):
				if self._m[i][j] == self._m[i-1][j] and self._m[i][j] != 0:
					points = points + self._m[i][j]*2
					self._m[i-1][j] = self._m[i-1][j] * 2
					self._m[i][j] = 0
					self._global_moved = True
		self._score = self._score + points

		# move
		if points != 0:
			for i in range(1, 4):
				for j in range(4):
					x = i
					if self._m[i][j] != 0:
						while x >= 1 and self._m[x-1][j] == 0:
							x = x - 1
							moved = True
							self._global_moved = True
						if moved:
							self._m[x][j] = self._m[i][j]
							self._m[i][j] = 0
							moved = False

		if self._global_moved:
			self._steps = self._steps + 1
			print('shifted, ' + str(points) + ' points')
			print('Score: ' + str(self._score))
			print('Steps: ' + str(self._steps))

	def moveDown(self):
		self._global_moved = False
		moved = False
		# move
		for i in range(2, -1, -1):
			for j in range(4):
				x = i
				if self._m[i][j] != 0:
					while x <= 2 and self._m[x+1][j] == 0:
						x = x + 1
						moved = True
						self._global_moved = True
					if moved:
						self._m[x][j] = self._m[i][j]
						self._m[i][j] = 0
						moved = False

		# merge
		points = 0
		for i in range(2, -1, -1):
			for j in range(4):
				if self._m[i][j] == self._m[i+1][j] and self._m[i][j] != 0:
					points = points + self._m[i][j]*2
					self._m[i+1][j] = self._m[i+1][j] * 2
					self._m[i][j] = 0
					self._global_moved = True
		self._score = self._score + points

		# move
		if points != 0:
			for i in range(2, -1, -1):
				for j in range(4):
					x = i
					if self._m[i][j] != 0:
						while x <= 2 and self._m[x+1][j] == 0:
							x = x + 1
							moved = True
							self._global_moved = True
						if moved:
							self._m[x][j] = self._m[i][j]
							self._m[i][j] = 0
							moved = False

		if self._global_moved:
			self._steps = self._steps + 1
			print('shifted, ' + str(points) + ' points')
			print('Score: ' + str(self._score))
			print('Steps: ' + str(self._steps))

	def moveLeft(self):
		self._global_moved = False
		moved = False
		# move
		for j in range(1, 4):
			for i in range(4):
				x = j
				if self._m[i][j] != 0:
					while x >= 1 and self._m[i][x-1] == 0:
						x = x - 1
						moved = True
						self._global_moved = True
					if moved:
						self._m[i][x] = self._m[i][j]
						self._m[i][j] = 0
						moved = False

		# merge
		points = 0
		for j in range(1, 4):
			for i in range(4):
				if self._m[i][j] == self._m[i][j-1] and self._m[i][j] != 0:
					points = points + self._m[i][j]*2
					self._m[i][j-1] = self._m[i][j-1] * 2
					self._m[i][j] = 0
					self._global_moved = True
		self._score = self._score + points

		# move
		if points != 0:
			for j in range(1, 4):
				for i in range(4):
					x = j
					if self._m[i][j] != 0:
						while x >= 1 and self._m[i][x-1] == 0:
							x = x - 1
							moved = True
							self._global_moved = True
						if moved:
							self._m[i][x] = self._m[i][j]
							self._m[i][j] = 0
							moved = False

		if self._global_moved:
			self._steps = self._steps + 1
			print('shifted, ' + str(points) + ' points')
			print('Score: ' + str(self._score))
			print('Steps: ' + str(self._steps))

	def moveRight(self):
		self._global_moved = False
		moved = False
		# move
		for j in range(2, -1, -1):
			for i in range(4):
				x = j
				if self._m[i][j] != 0:
					while x <= 2 and self._m[i][x+1] == 0:
						x = x + 1
						moved = True
						self._global_moved = True
					if moved:
						self._m[i][x] = self._m[i][j]
						self._m[i][j] = 0
						moved = False

		# merge
		points = 0
		for j in range(2, -1, -1):
			for i in range(4):
				if self._m[i][j] == self._m[i][j+1] and self._m[i][j] != 0:
					points = points + self._m[i][j]*2
					self._m[i][j+1] = self._m[i][j+1] * 2
					self._m[i][j] = 0
					self._global_moved = True
		self._score = self._score + points

		# move
		if points != 0:
			for j in range(2, -1, -1):
				for i in range(4):
					x = j
					if self._m[i][j] != 0:
						while x <= 2 and self._m[i][x+1] == 0:
							x = x + 1
							moved = True
							self._global_moved = True
						if moved:
							self._m[i][x] = self._m[i][j]
							self._m[i][j] = 0
							moved = False

		if self._global_moved:
			self._steps = self._steps + 1
			print('shifted, ' + str(points) + ' points')
			print('Score: ' + str(self._score))
			print('Steps: ' + str(self._steps))

	def checkWin(self):
		# win
		for i in range(4):
			for j in range(4):
				if self._m[i][j] == self._goal:
					print('you won')
					self._stopGame = True
					return

		# lose
		noZero = True
		for i in range(4):
			for j in range(4):
				if self._m[i][j] != 0:
					noZero = False

		noPair = True
		for i in range(4):
			for j in range(3):
				if self._m[i][j] == self._m[i][j+1]:
					noPair = False
		for i in range(3):
			for j in range(4):
				if self._m[i][j] == self._m[i+1][j]:
					noPair = False

		if noZero and noPair:
			print('you lost')
			self._stopGame = True
			return
		else:
			if self._global_moved:
				self.add_random_block()

game = Game()
game.add_random_block()
game.add_random_block()
game.printMatrix()
game.setGoal(16)

while True:
	command = input('up/down/left/right: ')
	if command in ['up', 'down', 'left','right']:
		if command == 'up':
			game.moveUp()
			game.checkWin()
			game.printMatrix()
		if command == 'down':
			game.moveDown()
			game.checkWin()
			game.printMatrix()
		if command == 'left':
			game.moveLeft()
			game.checkWin()
			game.printMatrix()
		if command == 'right':
			game.moveRight()
			game.checkWin()
			game.printMatrix()
		if game.getStopGame():
			break
	else:
		print('invalid command')
