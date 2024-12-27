import re
from math import floor

class Machine: 
    def __init__(self, buttonA, buttonB, prizePosition): 
        self.buttonA = Button(*buttonA)
        self.buttonB = Button(*buttonB)
        self.prizeX = prizePosition[0]
        self.prizeY = prizePosition[1]
    
    def getCheapestSolution(self, maxValue): 
        solutions = self.findSolution(maxValue)
        if solutions == []: return 0
        else: return min(solutions)
    
    def findSolution(self, maxSteps):
        solutions = []
        buttonPressB = -(self.prizeX*self.buttonA.y-self.prizeY*self.buttonA.x)/(self.buttonA.x*self.buttonB.y-self.buttonB.x*self.buttonA.y)
        buttonPressA = (self.prizeX-buttonPressB*self.buttonB.x)/self.buttonA.x
        for i in range(1, maxSteps): 
            if (buttonPressA*i <= maxSteps and buttonPressB*i <= maxSteps and
                (buttonPressA*i).is_integer() and (buttonPressB*i).is_integer()): 
                solutions.append(int(3*buttonPressA*i+1*buttonPressB*i))
            else: break
        return solutions

class Button: 
    def __init__(self, xValue, yValue): 
        self.x = xValue
        self.y = yValue
    
    def __str__(self):
        return 'X=' + str(self.x) +  ', Y=' + str(self.y)


def main():
    machines = serializeInput('day13/input.txt')
    part1(machines)
    part2(machines)

def part1(machines):
    count = 0
    for machine in machines: 
        count += machine.getCheapestSolution(100)
    print(count)

def part2(machines):
    machines = unitConversion(machines)
    count = 0
    for machine in machines: 
        count += machine.getCheapestSolution(10000000000000)
    print(count)

def unitConversion(machines): 
    for machine in machines: 
        machine.prizeX += 10000000000000
        machine.prizeY += 10000000000000
    return machines
        

def serializeInput(textfile):
    with open(textfile)as inputFile:
        machines = []
        for machine in inputFile.read().split('\n\n'):
            buttonA = int(re.search(r'Button A: X\+(\d+),', machine).group(1)), int(re.search(r'Button A: X\+\d+, Y\+(\d+)', machine).group(1))
            buttonB = int(re.search(r'Button B: X\+(\d+),', machine).group(1)), int(re.search(r'Button B: X\+\d+, Y\+(\d+)', machine).group(1))
            prize = int(re.search(r'Prize: X=(\d+),', machine).group(1)), int(re.search(r'Prize: X=\d+, Y=(\d+)', machine).group(1))
            machines.append(Machine(buttonA, buttonB, prize))
    return machines
            


if __name__ == '__main__':
    main()