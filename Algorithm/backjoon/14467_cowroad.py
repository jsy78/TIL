import sys
input = sys.stdin.readline

class Cow :
    def __init__(self, number, position) :
        self.number = number
        self.position = position
        self.count = 0

    def getNumber(self) :
        return self.number

    def setPosition(self, position) :
        self.position = position

    def getPosition(self) :
        return self.position
    
    def addMoveCount(self) :
        self.count += 1
    
    def getMoveCount(self) :
        return self.count

T = int(input())
cow_list = []
for _ in range(T) :
    number, position = map(int, input().split())
    if number not in map(Cow.getNumber, cow_list) :
        cow_list.append(Cow(number, position))
        continue

    for cow in cow_list :
        if cow.getNumber() != number :
            continue
        if cow.getPosition() == position :
            break
        
        cow.setPosition(position)
        cow.addMoveCount()

print(sum(map(Cow.getMoveCount, cow_list)))
