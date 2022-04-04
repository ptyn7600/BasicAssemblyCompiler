from hashTable import hashTable

def parseTreetoAssembly(mainProgramTree, programInfo):
    level = 0
    # Create assembly file
    asmfile = open("testing.asm", "w")
    returnStr = ""
    # Create the look up table
    symbolTable = hashTable()
    # Traverse through all sub programs
    for subProgram in mainProgramTree.getBranches():
        returnStr += pasrsingCases(subProgram, symbolTable, asmfile, programInfo, level)
    # Write to assembly file
    asmfile.write(returnStr)
    # Close the assembly file
    asmfile.close()


def pasrsingCases(programTree, symbolTable, asmfile, programInfo, level):
    instructionType = programTree.getValue()

    # Checking different types of instructions
    if (instructionType == "variable"):
        str = parseVariable(programTree, symbolTable, level)
        # # Write assembly instruction
        # asmfile.write(str)
        # print(str)
        return str
    # ======================================= #
    # Parsing If statement
    elif (instructionType == "if"):
        str = parseIf(programTree, symbolTable, asmfile, programInfo, level)
        # asmfile.write(str)
        # print(str)
        return str
    # ======================================= #
    # Parsing If statement
    elif (instructionType == "statement"):
        str = parseStatement(programTree, symbolTable, asmfile, programInfo, level)
        return str
    # ======================================= #
    # Parsing Label
    elif (instructionType == "label"):
        str = parseLabel(programTree, symbolTable, level)
        return str

    # ======================================= #
    # Parsing Label
    elif (instructionType == "constant"):
        str = parseConstant(programTree)
        return str

def parseVariable(programTree, symbolTable, level):
    # get the branches of the tree
    characteristic = programTree.getBranches()
    name = ""
    type = ""
    value = 0
    # print("Parsing VARIABLE instruction...")
    for eachChar in characteristic:
        if (eachChar.getValue() == "name"):
            name = eachChar.getBranches()[0].getValue()
        elif (eachChar.getValue() == "type"):
            type = eachChar.getBranches()[0].getValue()
        elif (eachChar.getValue() == "value"):
            value = eachChar.getBranches()[0].getValue()
    # add to the symbol table
    symbolTable.add_variable(name, type, value)
    returnStr = '\t' * level + "addiu " + symbolTable.get_register(name) + ", $0, " + str(value) + "\n"
    return returnStr

def parseIf(programTree, symbolTable, asmfile, programInfo, level):
    # get the branches of the tree
    characteristic = programTree.getBranches()
    returnStr = '\t' * level
    # print("Parsing IF instruction...")
    for eachChar in characteristic:
        if ((eachChar.getValue()) == "expression"):
            returnStr += parseExpression(eachChar, symbolTable, programInfo, level) + "\n"
        elif ((eachChar.getValue()) == "true"):
            returnStr += "IF_" + str(programInfo.getIfCount()) + "_TRUE:\n"
            for subTrue in eachChar.getBranches():
                op1 = pasrsingCases(subTrue, symbolTable, asmfile, programInfo, level)
                returnStr += op1 + "\n"
        elif ((eachChar.getValue()) == "false"):
            returnStr += "ELSE_" + str(programInfo.getIfCount()) + ":\n"
            for subTrue in eachChar.getBranches():
                op1 = pasrsingCases(subTrue, symbolTable, asmfile, programInfo, level)
                returnStr += op1
            # print(eachChar.getNumBranches())
        #     level += 1
        #     for eachStatement in eachChar.getBranches():
        #         pasrsingCases(eachStatement, symbolTable, asmfile, programInfo, level)

    # increment the number of if count
    programInfo.addIf()
    # Return the pasrsing string
    return returnStr

def parseStatement(programTree, symbolTable, asmfile, programInfo, level):
    # print("Parsing a Statement")
    lhs = ""
    rhs = ""
    for side in programTree.getBranches():
        if (side.getValue() == "lhs"):
            for subProgram in side.getBranches():
                lhs += pasrsingCases(subProgram, symbolTable, asmfile, programInfo, level)
            # print(side.getBranches()[0].getValue())
        elif (side.getValue() == "rhs"):
            for subProgram in side.getBranches():
                rhs += pasrsingCases(subProgram, symbolTable, asmfile, programInfo, level)
            # print(side.getBranches()[0])
    returnStr = "addiu " + lhs + ", " + "$0, " + rhs
    return returnStr

def parseLabel(programTree, symbolTable, level):
    variable = programTree.getBranches()[0].getValue()
    return symbolTable.get_register(variable)

def parseConstant(programTree, funcCall):
    if (funcCall == "")
    return "" + programTree.getBranches()[0].getValue()

def parseExpression(programTree, symbolTable, programInfo, level):
    operands = []
    returnStr = '\t' * level
    expressionList = programTree.getBranches()
    for eachExpress in expressionList:
        if ((eachExpress.getValue()) == "operator"):
            operator = eachExpress.getBranches()[0].getValue()
            operatorStr = switchOperator(operator)
        elif ((eachExpress.getValue()) == "operand"):
            operands.append(eachExpress.getBranches()[0].getValue())
    returnStr += operatorStr + " " + symbolTable.get_register(operands[0]) + ", " + symbolTable.get_register(operands[1])
    returnStr += ", IF_" + str(programInfo.getIfCount()) + "_TRUE\nj ELSE_" + str(programInfo.getIfCount())
    return returnStr

def switchOperator(operator):
    if (operator == "=="):
        return "beq"
