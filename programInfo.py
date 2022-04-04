class programInfo:
    def __init__(self):
        self.count_while = 0
        self.count_if = 0
        self.count_for = 0

    def getWhileCount(self):
        return self.count_while

    def getIfCount(self):
        return self.count_if

    def getForCount(self):
        return self.count_for

    def addIf(self):
        self.count_if += 1

    def addWhile(self):
        self.count_while += 1

    def addFor(self):
        self.count_for += 1