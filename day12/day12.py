class Area:
    def __init__(self, letter, coordinates):
        self.crop = letter
        self.coordinates = coordinates
    
    def __str__(self):
        returnString =  'Crop: ' + self.crop + '\nCoordinates (x,y): '
        for coordinate in self.coordinates: 
            returnString += (coordinate.__str__() + ' | ')
        returnString += '\n\n'
        return returnString
    
    def area(self): 
        return len(self.coordinates)
    
    def circumference(self): 
        circumference = 0
        for i in range(len(self.coordinates)): 
            border = 4
            for j in range(len(self.coordinates)): 
                if j == i: continue
                if abs(self.coordinates[i].x-self.coordinates[j].x)+abs(self.coordinates[i].y-self.coordinates[j].y) == 1:
                    border -= 1
            circumference += border
        return circumference

class Coordinate:
    def __init__(self, y, x):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

def main():
    inputList = serializeInput('day12/input.txt')
    areaList = findAreas(inputList)
    print(*areaList, sep = '')
    part1(areaList)
    part2()

def part1(areaList):
    price = 0
    for area in areaList: 
        print(area.area(), area.circumference())
        price += area.area()*area.circumference()
    print(price)

def part2():
    pass
        
def serializeInput(textfile):
    returnList = []
    with open(textfile) as inputFile: 
        lineList = inputFile.read().split('\n')
        for line in lineList:
            returnList.append([None]+[char for char in line]+[None])
        returnList.insert(0, [None]*len(returnList[0]))
        returnList.append([None]*len(returnList[0]))
        return returnList
            
def findAreas(inputList):
    areaList = []
    for i in range(len(inputList)):
        for j in range(len(inputList[i])): 
            if inputList[i][j] == None: continue
            letter = inputList[i][j]
            coordinateList = findNeighbours(letter, Coordinate(i, j), inputList)
            area = Area(letter, coordinateList)
            areaList.append(area)
    return areaList

def findNeighbours(letter, coordinate, inputList):
    areaList = []
    inputList[coordinate.y][coordinate.x] = None
    if inputList[coordinate.y+1][coordinate.x] == letter:
       areaList += findNeighbours(letter, Coordinate(coordinate.y+1, coordinate.x), inputList)
    if inputList[coordinate.y-1][coordinate.x] == letter:
       areaList += findNeighbours(letter, Coordinate(coordinate.y-1, coordinate.x), inputList)
    if inputList[coordinate.y][coordinate.x+1] == letter:
       areaList += findNeighbours(letter, Coordinate(coordinate.y, coordinate.x+1), inputList)
    if inputList[coordinate.y][coordinate.x-1] == letter:
       areaList += findNeighbours(letter, Coordinate(coordinate.y, coordinate.x-1), inputList)
    areaList.append(coordinate)
    return areaList

if __name__ == '__main__':
    main()