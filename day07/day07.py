import random
def main():
    equations = serializeInput('day07/input.txt')
    part1(equations)
    part2()

def part1(equations):
    sumOfCorrectEquations = 0
    count = 0
    for equation in equations: 
        if evaluate(equation['targetValue'], equation['values'], ['+', '*']) == True: 
            sumOfCorrectEquations += equation['targetValue']
            count += 1
    print(sumOfCorrectEquations, count)


def part2():
    pass
        
def evaluate(target, numbers, operators):
    openList = [{'value': numbers.pop(0), 'operators': ''}]

    for number in numbers: 
        openList = addStep(openList, number, operators)
        #print(target, openList)
        for entry in openList: 
            if entry['value'] == target: 
                print(entry)
                return True
            elif entry['value'] > target: 
                entry['value'] = False
        
    return False

def addStep(openList, number, operators): 
    newOpenList = []

    for entry in openList:
        if entry['value'] == False: 
            #print(value, openList[value])
            continue
        path = entry['operators']
        for operator in operators: 
            match operator:
                case '+': 
                    newValue = entry['value'] + number
                    newPath = path+operator
                case '*': 
                    newValue = entry['value'] * number
                    newPath = path+operator
            newOpenList.append({'value': newValue, 'operators': newPath})
        
    return newOpenList


def serializeInput(textfile):
    with open(textfile) as inputText: 
        equations = []
        for line in inputText: 
            targetValue = int(line.split(': ')[0])
            values = list(map(int, line.split(': ')[1].split(' ')))
            equations.append({'targetValue': targetValue, 'values': values})
    return equations            


if __name__ == '__main__':
    main()