def main():
    numberList1, numberList2 = serializeInput('input.txt')
    part1(numberList1, numberList2)
    part2(numberList1, numberList2)

def part1(numberList1, numberList2):
    numberList1.sort()
    numberList2.sort()
    distance = 0
    for i in range(len(numberList1)): 
        distance += abs(numberList1[i]-numberList2[i])
    print(distance)

def part2(numberList1, numberList2):
    similarityScore = 0
    for number1 in numberList1: 
        foundEntries = 0
        for number2 in numberList2: 
            if number1 == number2: 
                foundEntries += 1
        similarityScore += number1*foundEntries
    print(similarityScore)
        

def serializeInput(textfile):
    numberList1 = []
    numberList2 = [] 
    with open(textfile,'r') as inputFile: 
        for line in inputFile:
            number1, number2 = line.split('   ')
            numberList1.append(int(number1))
            numberList2.append(int(number2))
    return numberList1, numberList2
            


if __name__ == '__main__':
    main()