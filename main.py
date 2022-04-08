import sys
import xml.etree.ElementTree as ET
from programTree import programTree
from parsing import *
from programInfo import programInfo

def parseXML(curXML, tree):
    for curAttr in curXML:
        pos = tree.addBranch(curAttr.tag)
        nextTree = tree.getBranch(pos)
        # print(repr(curAttr.text[0]))
        # if ((curAttr.text == emptyString) or (curAttr == emptyString2)):
        #     # print("None\n")
        if (curAttr.text[0] == '\n'):
            parseXML(curAttr, nextTree)
        else:
            nextTree.addBranch(curAttr.text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # fileName = "pop_count"
    # fileName = "testing"
    if (len(sys.argv) == 2):
        # Take the filename from the argument
        fileName = "./testing/" + sys.argv[1]
        # Open XML file
        file = ET.parse(fileName + ".xml")
        # Open XML and parsing it to a tree
        program = file.getroot()
        mainProgramTree = programTree("program")
        parseXML(program, mainProgramTree)
        # Print out the tree to check result
        # mainProgramTree.printTree()

        # Parsing the tree and write assembly for it
        programInfo = programInfo()
        parseTreetoAssembly(mainProgramTree, programInfo, fileName + ".asm")
    else:
        print("Please input only 1 argument for the file name")













        # ======================================= #
        # # Parsing Variables



    # ========================================== #

    # ========================================== #
    # Testing Hashing
    # symbolTable = hashTable()
    # symbolTable.add_variable("a", "int", 4)
    # symbolTable.add_variable("b", "char", 0)
    # print(symbolTable.get_type("a"))
    # print(symbolTable.get_value("b"))

# ===================================== GARBAGE ==================== #

 # for instruction in program:
    #     pos = mainProgramTree.addBranch(instruction.tag)
    #     curBranch = mainProgramTree.getBranch(pos)
    #     for characteristic in instruction:
    #         anoPos = curBranch.addBranch(characteristic.tag)
    #         curBranch.getBranch(anoPos).addBranch(characteristic.text)
    #         curCurBranch = curBranch.getBranch(anoPos)
    #         for subCharac in characteristic:
    #             anoAnoPos = curCurBranch.addBranch(subCharac.tag)
    #             curCurBranch.getBranch(anoAnoPos).addBranch(subCharac.text)
    #             # curCurBranch = curBranch.getBranch(anoPos)



