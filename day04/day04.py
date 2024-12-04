from re import findall

def main():
    wordMap = serializeInput('day04/input.txt')
    part1(wordMap)
    part2(wordMap)

def part1(wordMap):
    allStrings = generateSubStrings(wordMap)
    found = 0
    for direction in allStrings: 
            found += countMatches(direction, 'XMAS')
    print(found)

def part2(wordMap):
    count =0
    for i in range(1,len(wordMap)-1):
        for j in range(1, len(wordMap[i])-1):
            if wordMap[i][j] == 'A': 
                try: print(wordMap[i+1][j+1])
                except: print(j)
                if (
                    (
                        (wordMap[i-1][j-1] == 'M' and wordMap[i+1][j+1] == 'S') or 
                        (wordMap[i-1][j-1] == 'S' and wordMap[i+1][j+1] == 'M')
                    ) and
                    ( 
                         (wordMap[i-1][j+1] == 'M' and wordMap[i+1][j-1] == 'S') or 
                         (wordMap[i-1][j+1] == 'S' and wordMap[i+1][j-1] == 'M')
                    )
                ):
                    print(i,j)
                    count += 1
    print(count)
        

def serializeInput(textfile):
    with open(textfile) as inputFile:
        return [line for line in inputFile]

def generateSubStrings(wordMap): 
     return [
       wordMap, 
       reverse(wordMap), 
       transpose(wordMap),
       reverse(transpose(wordMap)),
       diagonal1(wordMap),
       reverse(diagonal1(wordMap)),
       diagonal2(wordMap), 
       reverse(diagonal2(wordMap))
       ]


def reverse(listOfStrings):
    return [string[::-1] for string in listOfStrings]
     
def transpose(listOfStrings): 
     return [''.join(s) for s in zip(*listOfStrings)]

def diagonal1(listOfStrings): 
    diagonalList = []
    #firstHalf
    for i in range(len(listOfStrings)):
        diagonalString = ''
        for j in range(i+1):
            diagonalString += listOfStrings[j][i-j]
        diagonalList.append(diagonalString)
    #secondHalf
    for i in range(len(listOfStrings)-1):
        diagonalString = ''
        for j in range(i+1):
            diagonalString += listOfStrings[len(listOfStrings)-1-i+j][len(listOfStrings)-1-j]
        diagonalList.append(diagonalString)
    return diagonalList

def diagonal2(listOfStrings):
    diagonalList = []
    #firstHalf
    for i in range(len(listOfStrings)):
        diagonalString = ''
        for j in range(i+1):
            diagonalString += listOfStrings[j][len(listOfStrings)-1-i+j]
        diagonalList.append(diagonalString)
    #secondHalf
    for i in range(len(listOfStrings)-1):
        diagonalString = ''
        for j in range(i+1):
            diagonalString += listOfStrings[len(listOfStrings)-1-i+j][j]
        diagonalList.append(diagonalString)
    return diagonalList

def countMatches(stringList, searchTerm):
    count = 0
    for string in stringList:
        count += len(findall(searchTerm,string))
    print(stringList, count)
    return count


if __name__ == '__main__':
     main()