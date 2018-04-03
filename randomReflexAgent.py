import cleaner
import random

'''
A randomized reflex agent that can choose actions randomly based on sensor readings.

if-then rules
If dirty then suck up dirt
If facing wall and clean then turn right possibility1 turn left possibility2
If facing wall and at home then turn off
If not facing wall and clean then go forward

'''

class RandomReflexAgent(cleaner.Cleaner):

	def __init__(self, probTurnLeft, probTurnRight,probTurnOff,probMove):
		cleaner.Cleaner.__init__(self)
		random.seed()
		self.probTurnLeft = probTurnLeft
		self.probTurnRight = probTurnRight
		self.probTurnOff = probTurnOff
		self.probMove = probMove

	def Agent (self, grid):
		isFacingWall = self.SenseWall(grid)
		isDirty      = self.SenseDirt(grid)
		isHome       = self.SenseHome()

		if isDirty:
			return self.ActSuckDirt
		else:
			if isFacingWall:
				if isHome:
					if random.uniform (0, 1) < self.probTurnOff:
						return self.ActTurnOff
				if random.uniform(0, 1) < self.probTurnRight:
					return self.ActTurnRight
				else:
				    return self.ActTurnLeft
			else:
				if random.uniform(0,1) < self.probMove:
					return self.ActMove
				else:
					if random.uniform(0, 1) < self.probTurnRight:
						return self.ActTurnRight
					else:
						return self.ActTurnLeft
