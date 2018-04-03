import cleaner

class ModelBasedAgent(cleaner.Cleaner):

    '''
    3bit memeory, so, there are eight kinds of method:

    state0(0,0,0):not wall: move. is wall: turn left, state = 1
    state1(0,0,1):not wall: move, state = 2. is wall: turn left, state = 0
    state2(0,1,0):not wall or wall: turn left, state = 3
    state3(0,1,1):not wall: move. is wall: turn right, state = 4
    state4(1,0,0):not wall: move, state = 5. is wall: turn left, state = 6
    state5(1,0,1):not wall or wall: turn right, state = 0
    state6(1,1,0):only wall: turn left, state = 0

    '''
    # The initial state is 3, which is 0,1,1, because the cleaner is
    # in the bottom leftmost corner oriented upwards.
    def __init__(self):
        cleaner.Cleaner.__init__(self)
        self.bit0 = False
        self.bit1 = True
        self.bit2 = True

    def SetState(self,bit0, bit1, bit2):
        self.bit0 = bit0
        self.bit1 = bit1
        self.bit2 = bit2
    def Agent(self, roomMap):
        isWall = self.SenseWall(roomMap)
        isDirty = self.SenseDirt(roomMap)
        isHome = self.SenseHome()
        
        if isDirty:
            return self.ActSuckDirt
        elif isHome and isWall:
            return self.ActTurnOff
        # state = 0
        elif not self.bit0 and not self.bit1 and not self.bit2:
            if isWall:
                # set state = 1
                self.SetState(False,False,True)
                return self.ActTurnLeft
            else:
                return self.ActMove
            # state = 1
        elif not self.bit0 and not self.bit1 and self.bit2:
            if isWall:
                # set state = 6 || 0
                self.SetState(False, False, False)
                return self.ActTurnLeft
            else:
                # set state = 2
                self.SetState(False,True,False)
                return self.ActMove
        # state = 2
        elif not self.bit0 and self.bit1 and not self.bit2:
            # set state = 3
            self.SetState(False,True,True)
            return self.ActTurnLeft
        # state = 3
        elif not self.bit0 and self.bit1 and self.bit2:
            if isWall:
                # set state = 4
                self.SetState(True,False,False)
                return self.ActTurnRight
            else:
                return self.ActMove
        # state = 4
        elif self.bit0 and not self.bit1 and not self.bit2:
            if isWall:
                # set state = 6
                self.SetState(True,True,False)
                return self.ActTurnLeft
            else:
                # set state = 5
                self.SetState(True,False,True)
                return self.ActMove
        # state = 5
        elif self.bit0 and not self.bit1 and self.bit2:
            #s et state = 0
            self.SetState(False,False,False)
            return self.ActTurnRight
        # state = 6
        elif self.bit0 and self.bit1 and not self.bit2:
            # set state = 0
            self.SetState(False,False,False)
            return self.ActTurnLeft
            
