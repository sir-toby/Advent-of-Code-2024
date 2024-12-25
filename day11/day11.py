from copy import deepcopy

def main():
    stoneList = serializeInput('day11/input.txt')
    iterate(deepcopy(stoneList), 25)
    iterate(deepcopy(stoneList), 75)

def iterate(stoneList, iterations):
    for i in range(iterations):
        #print(str(i/iterations*100)+'%') 
        stoneList = transform(stoneList)
    stoneCount = 0
    for stone in stoneList:
        stoneCount += stone['count']
    print(stoneCount, len(stoneList))      

def transform(stoneList):
    newStoneList = []
    for stone in stoneList: 
        match stone['value']: 
            case 0:
                newStoneList = addToList(newStoneList, {'value': 1, 'count': stone['count']})
            case _ if len(str(stone['value']))%2 == 0:
                stone2 = {'value': int(str(stone['value'])[int(len(str(stone['value']))/2):]), 'count': stone['count']}
                stone1 = {'value': int(str(stone['value'])[:int(len(str(stone['value']))/2)]), 'count': stone['count']}
                newStoneList = addToList(newStoneList, stone1)
                newStoneList = addToList(newStoneList, stone2)
            case _:
                newStoneList = addToList(newStoneList, {'value': stone['value']*2024, 'count': stone['count']})
    return newStoneList

def addToList(stoneList, stone):
    if stone['value'] not in [newStone['value'] for newStone in stoneList]:
        stoneList.append(stone)
    else: 
        for newStone in stoneList: 
            if stone['value'] == newStone['value']: 
                newStone['count'] += stone['count']
                break
    return stoneList

def serializeInput(textfile):
    stoneList = []
    with open(textfile) as inputFile:
        for val in inputFile.read().split(' '): 
            stoneList.append({'value': int(val), 'count': 1})
    print(stoneList)
    return stoneList

if __name__ == '__main__':
    main()