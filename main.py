import sys
import simpleReflexAgent
import modelBasedAgent
import randomReflexAgent

class Cell(object):
    
    def __init__(self, state):
        self.State = state

    def Clean(self):
        if self.State == 'd':
            self.State = 'c'
            
def InitRoomMap(filename):
    roomMap = []
    mapFile = open(filename)
    try:
        for i in range(0,10):
            eachLine = mapFile.readline( )
            eachRow = []
            for state in eachLine:
                if state != '\t' and state != '\n':
                    eachRow.append(Cell(state))
                    
            roomMap.insert(0,eachRow)
		
    finally:
        mapFile.close()
        return roomMap

def NumOfDirty(roomMap):
    num = 0
    for row in roomMap:
        for cell in row:
            if cell.State == 'd':
                num += 1
    return num

def printG(roomMap):
    for i in range(len(roomMap) - 1, -1, -1):
        line = ''
        for j in range(len(roomMap[0])):
            cell = roomMap[i][j]
            if cell.State == 'w':
                line = line + 'W'
            elif cell.State == 'd':
                line = line + 'D'
            else:
                line = line + ' '
            line = line + ' '
        print (line)

def RunSimpleReflexAgent(roomMapFile):
    roomMap = InitRoomMap(roomMapFile)
    originalNumOfDirty = NumOfDirty(roomMap)
    
    agent = simpleReflexAgent.SimpleReflexAgent()
    numOfAction = agent.Run(roomMap)
    
    finalNumOfcleaned = originalNumOfDirty - NumOfDirty(roomMap)

    PrintResult("Simple-Reflex Agent", originalNumOfDirty, finalNumOfcleaned, numOfAction, roomMap)
def RunModelBasedAgent(roomMapFile):
    roomMap = InitRoomMap(roomMapFile)
    originalNumOfDirty = NumOfDirty(roomMap)
    
    agent = modelBasedAgent.ModelBasedAgent()
    numOfAction = agent.Run(roomMap)
    
    finalNumOfcleaned = originalNumOfDirty - NumOfDirty(roomMap)

    PrintResult("Model-Based Agent", originalNumOfDirty, finalNumOfcleaned, numOfAction, roomMap)

def RunRandomAgent(roomMapFile):
    sumOfActions = 0
    sumOfCleaned = 0
    sumOfDirts = 0

    agent = randomReflexAgent.RandomReflexAgent(0.5,0.5,0.1,0.8)

    for i in range (0,50):
        roomMap = InitRoomMap(roomMapFile)
        originalNumOfDirty = NumOfDirty(roomMap)
        numOfAction = agent.Run(roomMap)
        finalNumOfcleaned = originalNumOfDirty - NumOfDirty(roomMap)
        sumOfActions += numOfAction
        sumOfCleaned += finalNumOfcleaned
        sumOfDirts   += originalNumOfDirty
    PrintResult("Rondom-Relex Agent(Average)", sumOfDirts/50, sumOfCleaned/50, sumOfActions/50, roomMap)


def PrintResult(cleaner, originalNumOfDirty, finalNumOfcleaned, numOfAction, roomMapCleaned):
    output = open(str(cleaner + ' Result.txt'), 'a')
    
    print("*****************************************************")
    output.write("*****************************************************\n")
    for i in range(len(roomMapCleaned) - 1, -1, -1):
        line = ''
        for j in range(len(roomMapCleaned[0])):
            cell = roomMapCleaned[i][j]
            if cell.State == 'c':
                line += ' '
            else:
                line += cell.State
            line += ' '
        print (line)
        output.write(line + '\n')
    
    print("-------------------")
    print("Agent:           " + cleaner)
    print("Total Dirty:     " + str(originalNumOfDirty))
    print("Total Cleaned:   " + str(finalNumOfcleaned))
    print("Action cost:     " + str(numOfAction))
    print("Efficiency:      " + str(finalNumOfcleaned / numOfAction))
    print("Cleaned Percent: " + str(finalNumOfcleaned / originalNumOfDirty) + '\n')

    output.write("-------------------\n")
    output.write("Agent:           " + cleaner + '\n')
    output.write("Total Dirty:     " + str(originalNumOfDirty) + '\n')
    output.write("Total Cleaned:   " + str(finalNumOfcleaned) + '\n')
    output.write("Action cost:     " + str(numOfAction) + '\n')
    output.write("Efficiency:      " + str(finalNumOfcleaned / numOfAction) + '\n')
    output.write("Cleaned Percent: " + str(finalNumOfcleaned / originalNumOfDirty) + '\n\n')
    output.close()
    
if __name__=='__main__':
    RunModelBasedAgent("env1.txt")
    RunModelBasedAgent("env2.txt")
    RunRandomAgent("env1.txt")
    RunRandomAgent("env2.txt")
    RunSimpleReflexAgent("env1.txt")
    RunSimpleReflexAgent("env2.txt")
