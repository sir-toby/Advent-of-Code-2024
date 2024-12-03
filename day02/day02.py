def main():
    reportList = serializeInput('input.txt')
    part1(reportList)
    part2(reportList)

def part1(reportList):
    safeCount = 0
    for report in reportList:
        if evaluateReport(report) == True: safeCount += 1
    print(safeCount)          


def part2(reportList):
    safeCount = 0
    for report in reportList: 
        if evaluateReport(report) == True: safeCount += 1
        else: 
            for i in range(len(report)): 
                if evaluateReport(report[0:i]+report[i+1:]) == True: 
                    safeCount += 1
                    break
    print(safeCount)


def evaluateReport(report):
    direction = None
    unsafe = False
    for i in range(1, len(report)): 
        diff = report[i]-report[i-1]
        match diff:
            case diff if abs(diff) >3: unsafe = True
            case diff if diff == 0: unsafe = True 
            case diff if diff <0:
                if direction == 'asc': unsafe = True
                else: direction = 'desc'
            case diff if diff > 0: 
                if direction == 'desc': unsafe = True
                else: direction = 'asc'
    if not unsafe: return True


def serializeInput(textfile):
    reportList = []
    with open(textfile) as inputFile:
        for line in inputFile:
            reportList.append(list(map(int,line.split(' '))))
    return reportList
            


if __name__ == '__main__':
    main()