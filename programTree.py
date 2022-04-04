class Node:
    # Constructor
    def __init__(self, data):
        self.data = data

    # Return the data of the Node
    def getValue(self):
        return self.data

class programTree:
    def __init__(self, name):
        self.root = Node(name)
        self.branches = []
        self.numBranches = 0

    def addBranch(self, data):
        newBranch = programTree(data)
        self.branches.append(newBranch)
        self.numBranches += 1
        return (self.numBranches - 1)

    def getBranch(self, pos):
        return self.branches[pos]

    def getBranches(self):
        # return the list of trees
        return self.branches

    def getValue(self):
        return self.root.getValue()

    def printTree(self, level=0):
        print('\t' * level + repr(self.root.getValue()))
        for branch in self.getBranches():
            # print('\t' * level + repr(branch.getValue()))
            branch.printTree(level + 1)

    def getNumBranches(self):
        return self.numBranches