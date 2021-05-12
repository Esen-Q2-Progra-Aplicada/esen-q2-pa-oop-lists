class ListUtil:
    def __init__(self):
        self.numberList = []

    def getList(self):
        return self.numberList

    def addNumbers(self, number=1):
        self.numberList = range(1, 10)
        total = 0
        for num in self.numberList:
            total += num
        return total
