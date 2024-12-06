def main():
    obstaclesList, startPosition, maxY, maxX = serializeInput('day06/input.txt')
    visitedList = part1(obstaclesList, startPosition, maxY, maxX)
    part2(obstaclesList, startPosition, maxY, maxX, visitedList)

def part1(obstaclesList, startPosition, maxY, maxX):
    visitedFields = []
    direction = 'up'
    currentPosition = startPosition
    while (-1 < currentPosition['x'] < maxX and
           -1 < currentPosition['y'] < maxY):
        if currentPosition not in visitedFields: visitedFields.append(currentPosition)
        currentPosition, direction = determineNextStep(currentPosition, direction, obstaclesList)
    print(len(visitedFields))
    return visitedFields

def determineNextStep(currentPosition, direction, obstaclesList):
    directions = ['up', 'right', 'down', 'left']
    match direction: 
            case 'up': 
                nextPosition = {'y': currentPosition['y']-1, 'x': currentPosition['x']}
            case 'down': 
                nextPosition = {'y': currentPosition['y']+1, 'x': currentPosition['x']}
            case 'left': 
                nextPosition = {'y': currentPosition['y'], 'x': currentPosition['x']-1}
            case 'right': 
                nextPosition = {'y': currentPosition['y'], 'x': currentPosition['x']+1}
    #print(currentPosition, nextPosition, direction)
    if nextPosition in obstaclesList:
        return currentPosition, directions[(directions.index(direction)+1)%4]
    else:
        return nextPosition, direction


def part2(obstaclesList, startPosition, maxY, maxX, visitedList):
    visitedList.pop(0)
    validObstaclePositions = 0
    for visitedPosition in visitedList:
        obstaclesListNew = obstaclesList + [visitedPosition]
        visitedFields = []
        direction = 'up'
        currentPosition = startPosition
        i = 0
        while (-1 < currentPosition['x'] < maxX and
            -1 < currentPosition['y'] < maxY):
            if currentPosition not in visitedFields: 
                i=0 
                visitedFields.append(currentPosition)
            else: 
                i+=1
            currentPosition, direction = determineNextStep(currentPosition,direction,obstaclesListNew)
            if i == max(maxY, maxX): 
                validObstaclePositions += 1
                print(visitedPosition)
                break
    print(validObstaclePositions)
        

def serializeInput(textfile):
    obstacles = []
    with open(textfile) as file:
        map = file.readlines()
        map = [line.strip('\n') for line in map]
    for line in map:
        for i in range(len(line)):
            if line[i] == '#':
                obstacles.append({'y': int(map.index(line)),'x': i})
            elif line[i] == '^': 
                startposition = {'y': int(map.index(line)), 'x': i}
    return obstacles, startposition, len(map), len(map[0])
            


if __name__ == '__main__':
    main()