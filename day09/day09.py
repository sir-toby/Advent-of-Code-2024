from math import floor

def main():
    usedSpace, freeSpace = getListsPt1('day09/test1.txt')
    part1(*getListsPt1('day09/input.txt'))
    part2(*getListsPt2('day09/input.txt'))

def part1(usedSpace, freeSpace):
    for i in range(len(freeSpace)):
        if usedSpace[len(usedSpace)-1-i]['pos'] < freeSpace[i]['pos']:
            break
        usedSpace[len(usedSpace)-1-i]['pos'] = freeSpace[i]['pos']
    checksum = calculateChecksum(usedSpace)
    print(checksum)
            

def part2(usedSpace, freeSpace):
    for file in reversed(usedSpace):
        for space in freeSpace:
            if file['pos']<space['pos']: break
            if file['len']<=space['len']:
                file['pos'] = space['pos']
                space['pos'] = space['pos']+file['len']
                space['len']=space['len']-file['len']
                break
    checksum = calculateChecksumPt2(usedSpace)
    print(checksum)

def calculateChecksum(space):
    checksum = 0
    for item in space: 
        checksum += item['pos']*item['val']
    return checksum

def calculateChecksumPt2(usedSpace): 
    checksum = 0
    for file in usedSpace: 
        for i in range(file['len']):
            checksum += file['val']*(file['pos']+i)
    return checksum




def getListsPt1(textfile):
    usedSpace = []
    freeSpace = []
    with open(textfile) as inputfile:
        text = inputfile.read()
        for i in range(len(text)):
            if i%2==0:
                usedSpace = usedSpace + [{'pos': len(usedSpace)+len(freeSpace)+j, 'val': floor(i/2)} for j in range(int(text[i]))]
            else: 
                freeSpace = freeSpace + [{'pos': len(usedSpace)+len(freeSpace)+j, 'val': False} for j in range(int(text[i]))]
    return usedSpace, freeSpace

def getListsPt2(textfile):
    usedSpace = []
    freeSpace = []
    with open(textfile) as inputfile:
        text = inputfile.read()
        pos = 0
        for i in range(len(text)):
            if i%2==0:
                usedSpace.append({'pos': pos, 'val': floor(i/2), 'len': int(text[i])})
            else: 
                freeSpace.append({'pos': pos, 'val': False, 'len': int(text[i])})
            pos += int(text[i])
    return usedSpace, freeSpace            

if __name__ == '__main__':
    main()