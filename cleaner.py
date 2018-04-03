class Cleaner(object):
	Up = 0
	Right = 1
	Down = 2
	Left = 3
	NumOfDirections = 4
	Home = (1, 1)
	ActMove = 0
	ActTurnRight = 1
	ActTurnLeft = 2
	ActSuckDirt = 3
	ActTurnOff = 4

	def __init__(self):
		self.Position = self.Home
		self.Direction = self.Up

	def Turn(self, direction):
		if direction == 1:
			self.Direction = (self.Direction + 1) % self.NumOfDirections
		else:
			self.Direction = (self.Direction - 1 + self.NumOfDirections) \
							% self.NumOfDirections

	def GeCellInFront(self):
		x, y = self.Position
		if self.Direction == self.Up:
			y += 1
		elif self.Direction == self.Right:
			x += 1
		elif self.Direction == self.Down:
			y -= 1
		else:
			x -= 1
		return (x, y)
	

	def SenseWall(self, roomMap):
		x, y = self.GeCellInFront()

		if x <= 0 or x >= len(roomMap[y]) - 1:
			return True
		if y <= 0 or y >= len(roomMap) - 1:
			return True
		if roomMap[y][x].State == 'w':
			return True
		else:
			return False
		

	def SenseDirt(self, roomMap):
		x, y = self.Position
		if roomMap[y][x].State == 'd':
			return True
		else:
			return False
	

	def SenseHome(self):
		return self.Position == self.Home


	def Move(self, roomMap):
		if self.SenseWall(roomMap):
			return False
		
		x, y = self.GeCellInFront()
		if x <= 0 or x >= len(roomMap[y]) - 1:
			return False
		if y <= 0 or y >= len(roomMap) - 1:
			return False

		self.Position = (x, y)
		return True
	

	def SuckDirt(self, roomMap):
		x, y = self.Position
		roomMap[y][x].Clean()
		

	def Agent(self, roomMap):
		return self.ActTurnOff


	def Run(self, roomMap):
		numOfActions = 0
	
		while True:
			action = self.Agent(roomMap)
			numOfActions += 1

			if numOfActions > 500:
				return numOfActions;

			if action == self.ActMove:
				self.Move(roomMap)
			elif action == self.ActTurnRight:
				self.Turn(1)

			elif action == self.ActTurnLeft:
				self.Turn(0)

			elif action == self.ActSuckDirt:
				self.SuckDirt(roomMap)
			elif action == self.ActTurnOff:
				return numOfActions
	

