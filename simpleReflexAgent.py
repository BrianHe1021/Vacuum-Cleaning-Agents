import cleaner
'''
A simple memory-less deterministic reflex agent

if-then rules
If dirty then suck up dirt
If not facing wall and clean then go forward
If facing wall and clean then turn right
If facing wall and at home then turn off
'''
class SimpleReflexAgent(cleaner.Cleaner):

	def Agent(self, grid):
		 isFacingWall = self.SenseWall(grid)
		 isDirty      = self.SenseDirt(grid)
		 isHome       = self.SenseHome()

		 if isDirty:
		 	return self.ActSuckDirt
		 else:
		 	if isFacingWall:
		 		if isHome:
		 			return self.ActTurnOff
		 		else:
		 			return self.ActTurnRight
		 	else:
		 		return self.ActMove
