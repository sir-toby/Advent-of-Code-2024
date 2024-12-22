class Coordinate:
    instances = []
    def __init__(self, x, y, value): 
        self.x = int(x)
        self.y = int(y)
        self.value = int(value)
        Coordinate.instances.append(self)
    
    def getNeighbours(self):
        neighbours = []
        for coordinate in self.instances: 
            if (((coordinate.x == self.x and abs(coordinate.y - self.y) == 1) or 
               (coordinate.y == self.y and abs(coordinate.x - self.x) == 1)) and 
               coordinate.value-self.value == 1):
                neighbours.append(coordinate)
        return neighbours


def main():
    serializeInput('day10/input.txt')
    findSolution('targets')
    findSolution('paths')

def findSolution(uniqueInstance):
    score = 0
    for coordinate in Coordinate.instances:
        if coordinate.value == 0:
            score += len(findTargets(coordinate, uniqueInstance))
    print(score)

def findTargets(coordinate, uniqueInstance):
    targets = []
    neighbours = coordinate.getNeighbours()
    if neighbours != []:
        for neighbour in neighbours:
            if neighbour.value == 9:
                targets.append((neighbour.x, neighbour.y))
            else:
                targets = targets + findTargets(neighbour, uniqueInstance)
    
    if uniqueInstance == 'targets': 
        return list(set(targets))
    elif uniqueInstance == 'paths': 
        return targets


def serializeInput(textfile):
    with open(textfile) as inputFile:
        inputList = inputFile.read().split('\n')
        for i in range(len(inputList)): 
            for j in range(len(inputList[i])): 
                Coordinate(j, i, inputList[i][j])
    

            


if __name__ == '__main__':
    main()