from copy import deepcopy
def main():
    equations = serializeInput('day07/input.txt')
    part1(deepcopy(equations))
    part2(deepcopy(equations))

def part1(equations):
    sumOfCorrectEquations = 0
    for equation in equations: 
        if evaluate(equation['targetValue'], equation['values'], ['+', '*']) == True: 
            sumOfCorrectEquations += equation['targetValue']
    print(sumOfCorrectEquations)


def part2(equations):
    sumOfCorrectEquations = 0
    for equation in equations: 
        if evaluate(equation['targetValue'], equation['values'], ['+', '*', '||']) == True: 
            sumOfCorrectEquations += equation['targetValue']
    print(sumOfCorrectEquations)
        
def evaluate(target, numbers, operators):
    openList = [{'value': numbers.pop(0), 'operators': ''}]

    for number in numbers: 
        openList = addStep(openList, number, operators)
        #print(target, openList)
        for entry in openList: 
            if entry['value'] > target: 
                entry['value'] = False
    for entry in openList:
        if entry['value'] == target: 
            print(entry)
            return True
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
                case '||':
                    newValue = int(str(entry['value'])+str(number))
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