
def readInput():
    measurements = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            measurements.append(int(line.rstrip()))
    return measurements


def checkDepth(measurements):

    #Assign starting number and remove first index from array so we dont loop through it
    previousPos = measurements[0]
    measurements.pop(0)
    increaseCounter = 0

    for i in measurements:
        if i > previousPos:
            increaseCounter +=1
        previousPos = i
    return increaseCounter


def slidingWindows(measurements):

    #Assign starting number and remove first index from array so we dont loop through it
    previousBlock = measurements[0] + measurements[1] + measurements[2]
    measurements.pop(0)
    increaseCounter = 0

    for i in range(0, len(measurements) - 2):
        currentBlock = measurements[i] + measurements[i+1] + measurements[i+2]
        if currentBlock > previousBlock:
            increaseCounter +=1
        previousBlock = currentBlock
    return(increaseCounter)


#Part 1
print(checkDepth(readInput()))

#Part 2
print(slidingWindows(readInput()))
