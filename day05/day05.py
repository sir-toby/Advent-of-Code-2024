from math import floor
def main():
    rules, updates = serializeInput('day05/input.txt')
    part1(rules, updates)
    part2(rules, updates)

def part1(rules, updates):
    sumOfMiddleNumbers = 0
    for update in updates:
        if isUpdateValid(update, rules):
            sumOfMiddleNumbers += update[floor(len(update)/2)]
    print(sumOfMiddleNumbers)


def part2(rules, updates):
    sumOfMiddleNumbers = 0
    for update in updates:
        if not isUpdateValid(update, rules):
            update = makeValid(update, rules)
            sumOfMiddleNumbers += update[floor(len(update)/2)]
    print(sumOfMiddleNumbers)

def isUpdateValid(update, rules):
    for combination in createAllPossibleCombinations(update):
        if combination in rules: 
            return False
    return True

def createAllPossibleCombinations(update): 
    combinations = []
    for i in range(len(update)): 
        for j in range(i+1, len(update)): 
            combinations.append([update[j], update[i]])
    return combinations

def makeValid(update, rules): 
    sortedUpdate = [update.pop(0)]
    while len(update) > 0: 
        pageToExamine = update.pop(0)
        for i in range(len(sortedUpdate)): 
            if [pageToExamine, sortedUpdate[i]] in rules:
                sortedUpdate.insert(i, pageToExamine)
                break
        if pageToExamine not in sortedUpdate: sortedUpdate.append(pageToExamine)
    return sortedUpdate


def serializeInput(textfile):
    with open(textfile) as file: 
        rules, updates = file.read().split('\n\n')
    rules = rules.split('\n')
    rules = [list(map(int,(rule.split('|')))) for rule in rules]

    updates = updates.split('\n')
    updates = [list(map(int, update.split(','))) for update in updates]

    return rules, updates


if __name__ == '__main__':
    main()