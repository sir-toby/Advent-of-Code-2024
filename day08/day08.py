class Antenna:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Frequency:
    instances = []
    def __init__(self, symbol, antenna = None):
        for instance in Frequency.instances:
            if symbol == instance.channel: 
                instance.antennaList.append(antenna)
                return  
        self.channel = symbol
        self.antennaList = [antenna]
        Frequency.instances.append(self)

    def calculate_antinodes(self, numberOfNodes): 
        antinodes = set()
        for antenna1 in self.antennaList:
            for antenna2 in self.antennaList:
                if antenna1 == antenna2: continue
                xdistance = antenna1.x-antenna2.x
                ydistance = antenna1.y-antenna2.y

                for i in range(1 if numberOfNodes==1 else 0, numberOfNodes+1): 
                    antinodes.add((antenna1.x+i*xdistance, antenna1.y+i*ydistance))
                    antinodes.add((antenna2.x-i*xdistance, antenna2.y-i*ydistance))
        
        return antinodes

def main():
    maxX, maxY = serializeInput('day08/input.txt')
    part1(maxX, maxY)
    part2(maxX, maxY)

def part1(maxX, maxY):
    all_antinodes = set()
    for frequency in Frequency.instances:
        all_antinodes.update(frequency.calculate_antinodes(1))
    cleaned_antinodes = [node for node in all_antinodes if (0<=node[0]<=maxX and 0<=node[1]<=maxY)]
    print((cleaned_antinodes), len(cleaned_antinodes))


def part2(maxX, maxY):
    all_antinodes = set()
    for frequency in Frequency.instances:
        all_antinodes.update(frequency.calculate_antinodes(max(maxX, maxY)))
    cleaned_antinodes = [node for node in all_antinodes if (0<=node[0]<=maxX and 0<=node[1]<=maxY)]
    print((cleaned_antinodes), len(cleaned_antinodes))
        

def serializeInput(textfile):
    with open(textfile) as inputFile:
        text = inputFile.read()
        inputList = text.split('\n')
        for y in range(len(inputList)):
            for x in range(len(inputList[y])):
                if inputList[y][x] != '.': 
                    Frequency(inputList[y][x],Antenna(x,y))
        maxX = len(inputList[0])-1
        maxY = len(inputList)-1
    return maxX, maxY


if __name__ == '__main__':
    main()