from re import findall, sub, DOTALL

def main():
    inputString = serializeInput('input.txt')
    part1(inputString)
    part2(inputString)

def part1(inputString):
    foundList = findall(r"mul\(\d{1,3},\d{1,3}\)", inputString)
    getResultFromList(foundList)

def part2(inputString):
    cleanedString = sub(r"don't\(\).*?do\(\)","",inputString, flags=DOTALL)
    print(len(inputString), len(cleanedString))
    foundList = findall(r"mul\(\d{1,3},\d{1,3}\)", cleanedString)
    getResultFromList(foundList)
    

def getResultFromList(foundList):
    result = 0
    for operation in foundList: 
        result += multiply(*operation[4:-1].split(','))
    print(result)
     

def multiply(a, b):
     return int(a)*int(b)

def serializeInput(textfile):
        with open(textfile, 'r') as inputFile:
            return inputFile.read()
            


if __name__ == '__main__':
    main()