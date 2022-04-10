class programInfo:
    def __init__(self):
        self.count_while = -1
        self.count_if = -1
        self.count_for = -1

    def getWhileCount(self):
        return str(self.count_while)

    def getIfCount(self):
        return str(self.count_if)

    def getForCount(self):
        return str(self.count_for)

    def addIf(self):
        self.count_if += 1

    def addWhile(self):
        self.count_while += 1

    def addFor(self):
        self.count_for += 1