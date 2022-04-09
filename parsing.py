from hashTable import hashTable

def parseTreetoAssembly(mainProgramTree, programInfo, outputFileName):
    level = 0
    # Create assembly file
    asmfile = open(outputFileName, "w")
    returnStr = ""
    # Create the look up table
    symbolTable = hashTable()
    # Traverse through all sub programs
    for subProgram in mainProgramTree.getBranches():
        returnStr += pasrsingCases(subProgram, symbolTable, programInfo, level, "main")
        symbolTable.printTable()
    # Exit the program
    returnStr += "li $v0, 10\nsyscall"
    # Write to assembly file
    asmfile.write(returnStr)
    # Close the assembly file
    asmfile.close()


def pasrsingCases(programTree, symbolTable, programInfo, level, callFrom):
    instructionType = programTree.getValue()
    # Checking different types of instructions
    # ======================================= #
    # Parsing Argument statement
    if (instructionType == "argument"):
        returnStr = parseArgument(programTree, symbolTable, level)
        # print(returnStr)
        return returnStr
    # ======================================= #
    # Parsing Variable statement
    elif (instructionType == "variable"):
        returnStr = parseVariable(programTree, symbolTable, level)
        # print(returnStr)
        # # Write assembly instruction
        # asmfile.write(str)
        # print(str)
        return returnStr
    # ======================================= #
    # Parsing If statement
    elif (instructionType == "if"):
        returnStr = parseIf(programTree, symbolTable, programInfo, level)
        # print(returnStr)
        # asmfile.write(str)
        # print(str)
        return returnStr

    # ======================================= #
    # Parsing If statement
    elif (instructionType == "statement"):
        returnStr = parseStatement(programTree, symbolTable, programInfo, level)
        # print(returnStr)
        return returnStr

    # ======================================= #
    # Parsing For statement
    elif (instructionType == "for"):
        returnStr = parseFor(programTree, symbolTable, programInfo, level)
        # print(returnStr)
        return returnStr

    # ======================================= #
    # Parsing For statement
    elif (instructionType == "while"):
        returnStr = parseWhile(programTree, symbolTable, programInfo, level)
        # print(returnStr)
        return returnStr

    # ======================================= #
    # Parsing Label
    elif (instructionType == "label"):
        returnStr = parseLabel(programTree, symbolTable, level)
        # print(returnStr)
        return returnStr

    # ======================================= #
    # Parsing Label
    elif (instructionType == "const"):
        returnStr = parseConstant(programTree, symbolTable, programInfo, level, callFrom)
        # print(returnStr)
        return returnStr

    # ======================================= #
    # Parsing Expression
    elif (instructionType == "expression"):
        returnStr = parseExpression(programTree, symbolTable, programInfo, level, callFrom)
        # print(returnStr)
        return returnStr

    return "ERRORS"
def parseWhile(programTree, symbolTable, programInfo, level):
    returnStr = ""
    # get the branches of the tree
    characteristic = programTree.getBranches()
    for eachPart in characteristic:
        if (eachPart.getValue() == "init"):
            returnStr += "WHILE_" + programInfo.getWhileCount() + "_INIT:\n"
            for eachPartInit in eachPart.getBranches():
                returnStr += pasrsingCases(eachPartInit, symbolTable, programInfo, level + 1, "while")
        elif (eachPart.getValue() == "cond"):
            returnStr += "WHILE_" + programInfo.getForCount() + "_COND:\n"
            print(eachPart.getBranches()[0].getValue())
            returnStr += pasrsingCases(eachPart.getBranches()[0], symbolTable, programInfo, level + 1, "while")
        elif (eachPart.getValue() == "body"):
            for eachPartBody in eachPart.getBranches():
                returnStr += pasrsingCases(eachPartBody, symbolTable, programInfo, level + 1, "while")
            returnStr += "j WHILE_" + programInfo.getWhileCount() + "_COND\n"
        elif (eachPart.getValue() == "exit"):
            returnStr += "WHILE_" + programInfo.getForCount() + "_EXIT:\n"
    programInfo.addWhile()
    return returnStr


def parseFor(programTree, symbolTable, programInfo, level):
    returnStr = ""
    # get the branches of the tree
    characteristic = programTree.getBranches()
    for eachPart in characteristic:
        if (eachPart.getValue() == "init"):
            returnStr += "FOR_" + programInfo.getForCount() + "_INIT:\n"
            for eachPartInit in eachPart.getBranches():
                returnStr += pasrsingCases(eachPartInit, symbolTable, programInfo, level+1, "for")
        elif (eachPart.getValue() == "cond"):
                returnStr += "FOR_" + programInfo.getForCount() + "_COND:\n"
                returnStr += pasrsingCases(eachPart.getBranches()[0], symbolTable, programInfo, level+1, "for")
        elif (eachPart.getValue() == "body"):
            for eachPartBody in eachPart.getBranches():
                returnStr += pasrsingCases(eachPartBody, symbolTable, programInfo, level+1, "for")
        elif (eachPart.getValue() == "increment"):
            returnStr += "FOR_" + programInfo.getForCount() + "_INCRE:\n"
            for eachPartIncre in eachPart.getBranches():
                returnStr += pasrsingCases(eachPartIncre, symbolTable, programInfo, level+1, "for")
            returnStr += "j FOR_" + programInfo.getForCount() + "_COND\n"
        elif (eachPart.getValue() == "exit"):
            returnStr += "FOR_" + programInfo.getForCount() + "_EXIT:\n"
    programInfo.addFor()
    return returnStr

def parseArgument(programTree, symbolTable, level):
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
    symbolTable.add_argument(name, type, value)
    returnStr = "addiu " + symbolTable.get_register(name) + ", $0, " + str(value) + "\n"
    return returnStr

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
    returnStr = "addiu " + symbolTable.get_register(name) + ", $0, " + str(value) + "\n"
    return returnStr

def parseIf(programTree, symbolTable, programInfo, level):
    # get the branches of the tree
    characteristic = programTree.getBranches()
    returnStr = ""
    # print("Parsing IF instruction...")
    for eachChar in characteristic:
        if ((eachChar.getValue()) == "expression"):
            returnStr += parseExpression(eachChar, symbolTable, programInfo, level, "if") + "\n"
        elif ((eachChar.getValue()) == "true"):
            returnStr += "IF_" + programInfo.getIfCount() + "_TRUE:\n"
            for subTrue in eachChar.getBranches():
                op1 = pasrsingCases(subTrue, symbolTable, programInfo, level,"if")
                returnStr += op1
            returnStr += "j IF_" + programInfo.getForCount() + "_EXIT\n"
        elif ((eachChar.getValue()) == "false"):
            returnStr += "ELSE_" + programInfo.getIfCount() + ":\n"
            for subTrue in eachChar.getBranches():
                op1 = pasrsingCases(subTrue, symbolTable, programInfo, level,"if")
                returnStr += op1
            returnStr += "j IF_" + programInfo.getForCount() + "_EXIT\n"
            # print(eachChar.getNumBranches())
        #     level += 1
        #     for eachStatement in eachChar.getBranches():
        #         pasrsingCases(eachStatement, symbolTable, asmfile, programInfo, level)
    returnStr += "IF_" + programInfo.getForCount() + "_EXIT:\n"
    # increment the number of if count
    programInfo.addIf()
    # Return the pasrsing string
    return returnStr

def parseLabel(programTree, symbolTable, level):
    variable = programTree.getBranches()[0].getValue()
    return symbolTable.get_register(variable)

def parseConstant(programTree, symbolTable, programInfo, level, funcCall):
    if ((funcCall == "statement") or (funcCall == "expression")):
        return "" + programTree.getBranches()[0].getValue()
    elif (funcCall == "for"):
        value = programTree.getBranches()[0].getValue()
        name = "for_" + programInfo.getForCount() + "_constant"
        symbolTable.add_variable(name, "int", value)
        return "addiu " + symbolTable.get_register(name) + ", $0, " + symbolTable.get_value_from_name(name) + '\n'
    elif (funcCall == "while"):
        value = programTree.getBranches()[0].getValue()
        name = "while_" + programInfo.getWhileCount() + "_constant"
        symbolTable.add_variable(name, "int", value)
        return "addiu " + symbolTable.get_register(name) + ", $0, " + symbolTable.get_value_from_name(name) + '\n'

def parseStatement(programTree, symbolTable, programInfo, level):
    # print("Parsing a Statement")
    lhs = ""
    rhs = None
    returnStr = ""
    for side in programTree.getBranches():
        if (side.getValue() == "lhs"):
            for subProgram in side.getBranches():
                lhs += pasrsingCases(subProgram, symbolTable, programInfo, level, "statement")
            # print(side.getBranches()[0].getValue())
        elif (side.getValue() == "rhs"):
            for subProgram in side.getBranches():
                rhs = pasrsingCases(subProgram, symbolTable, programInfo, level, "statement")
    # print(rhs)
    # Simple assignment: for example x = 2
    if (str(type(rhs)) != "<class 'dict'>"):
        # print("1", end="--->")
        # print(rhs)
        returnStr += "addiu " + lhs + ", " + "$0, " + rhs + "\n"
        # if (symbolTable.isRegister(lhs)):
        #     # Update symbolTable
        #     symbolTable.update_variable(symbolTable.get_name_from_register(lhs), rhs)
    # elif (len(rhs) == 1):
    #     print("2", end="--->")
    #     print(rhs)
    #     returnStr += "addiu " + lhs + ", " + "$0, " + rhs["operand"][0] + "\n"
    #     # Update symbolTable
    #     symbolTable.update_variable(symbolTable.get_name_from_register(lhs), rhs["operand"][0])
    elif (len(rhs['operands']) == 2):
        # print("3", end="--->")
        # print(rhs)
        if (str(type(rhs['operands'][1])) == "<class 'list'>"):
            returnStr += rhs['operands'][1][1]
            returnStr += processOperation(rhs['operator'], lhs, [rhs['operands'][0], rhs['operands'][1][0]], symbolTable)
            # result = int(symbolTable.get_value_from_register(rhs['operands'][0])) + \
            #          int(symbolTable.get_value_from_register(rhs['operands'][1][0]))
            # Update symbolTable
            # symbolTable.update_variable(symbolTable.get_name_from_register(lhs), result)
        # elif (len([s for s in rhs['operands'] if s.isdigit()]) > 0):
        #     # returnStr += rhs['operator'] + "iu " + lhs + ", " + str(rhs['operands'].pop(0)) + ", " \
        #     #              + str(rhs['operands'].pop(0)) + "\n"
        #     returnStr += processOperation(1, rhs['operator'], lhs, rhs['operands'], symbolTable)
        else:
            # returnStr += rhs['operator'] + " " + lhs + ", " + str(rhs['operands'].pop(0)) \
            #              + ", " + str(rhs['operands'].pop(0)) + "\n"
            # returnStr += processOperation(0, rhs['operator'], lhs, rhs['operands'], symbolTable)
            returnStr += processOperation(rhs['operator'], lhs, rhs['operands'], symbolTable)
    return returnStr

def parseExpression(programTree, symbolTable, programInfo, level, callFrom):
    operands = []
    expressionList = programTree.getBranches()
    if (callFrom == "if"):
        returnStr = ""
        for eachExpress in expressionList:
            if ((eachExpress.getValue()) == "operator"):
                operator = eachExpress.getBranches()[0].getValue()
                operatorStr = switchOperator(operator)
            elif ((eachExpress.getValue()) == "operand"):
                operands.append(pasrsingCases(eachExpress.getBranches()[0], symbolTable, programInfo, level, "expression"))
        returnStr += operatorStr + " " + operands[0] + ", " + operands[1]
        returnStr += ", ELSE_" + programInfo.getIfCount()
        return returnStr
    elif (callFrom == "for"):
        returnStr = ""
        operatorStr = ""
        for eachExpress in expressionList:
            if ((eachExpress.getValue()) == "operator"):
                operator = eachExpress.getBranches()[0].getValue()
                operatorStr = switchOperator(operator)
            elif ((eachExpress.getValue()) == "operand"):
                operands.append(pasrsingCases(eachExpress.getBranches()[0], symbolTable, programInfo, level, "expression"))
        returnStr += operatorStr + " " + operands[0] + ", " + operands[1]
        returnStr += ", FOR_" + programInfo.getForCount() + "_EXIT\n"
        return returnStr
    elif (callFrom == "while"):
        returnStr = ""
        operatorStr = ""
        for eachExpress in expressionList:
            if ((eachExpress.getValue()) == "operator"):
                operator = eachExpress.getBranches()[0].getValue()
                operatorStr = switchOperator(operator)
            elif ((eachExpress.getValue()) == "operand"):
                operands.append(pasrsingCases(eachExpress.getBranches()[0], symbolTable, programInfo, level, "expression"))
        returnStr += operatorStr + " " + operands[0] + ", " + operands[1]
        returnStr += ", WHILE_" + programInfo.getForCount() + "_EXIT\n"
        return returnStr

    elif(callFrom == "statement"):
        returnDict = {"operator":"", "operands": []}
        for eachExpress in expressionList:
            if ((eachExpress.getValue()) == "operator"):
                operator = eachExpress.getBranches()[0].getValue()
                operatorStr = switchOperator(operator)
                returnDict.update({"operator": operatorStr})
            elif ((eachExpress.getValue()) == "operand"):
                # print(eachExpress.getBranches()[0].getValue())
                print(eachExpress.getBranches()[0].getValue())
                returnStr = pasrsingCases(eachExpress.getBranches()[0], symbolTable, programInfo, level, "expression")
                returnDict["operands"].append(returnStr)
        print(returnDict)
        return returnDict
    elif (callFrom == "expression"):
        # returnStr = ""
        returnArr = []
        operator = ""
        for eachExpress in expressionList:
            if ((eachExpress.getValue()) == "operator"):
                operator = eachExpress.getBranches()[0].getValue()
                operatorStr = switchOperator(operator)
            elif ((eachExpress.getValue()) == "operand"):
                operands.append(pasrsingCases(eachExpress.getBranches()[0], symbolTable, programInfo, level+1, "expression"))
        name = "expression" + str(level) + "constant"
        returnReg = symbolTable.add_variable(name, "int", None)
        returnArr.append(returnReg)
        returnArr.append(processOperation(operatorStr, returnReg, operands, symbolTable))
        # if (len([s for s in operands if s.isdigit()]) > 0):
        #     # newValue = eval(symbolTable.get_value_from_register(operands[0]) + operator +
        #     #                 symbolTable.get_value_from_register(operands[1]))
        #     name = "expression" + str(level) + "constant"
        #     returnReg = symbolTable.add_variable(name, "int", None)
        #     returnArr.append(returnReg)
        #     returnStr += processOperation(1, operatorStr, returnReg, operands, symbolTable)
        #     # returnStr += operatorStr + "i " + returnReg + ", " + operands[0] + ", " + operands[1] + "\n"
        #     returnArr.append(returnStr)
        # else:
        #     newValue = eval(symbolTable.get_value_from_register(operands[0]) + operator +
        #                     symbolTable.get_value_from_register(operands[1]))
        #     name = "expression" + str(level) + "constant"
        #     returnReg = symbolTable.add_variable(name, "int", str(newValue))
        #     returnArr.append(returnReg)
        #     # returnStr += operatorStr + " " + operands[0] + ", " + operands[1] + "\n"
        #     returnStr += processOperation(0, operatorStr, returnReg, operands, symbolTable)
        #     returnArr.append(returnStr)
        return returnArr
    return None

def processOperation(operator, lhs, operands, symbolTable):
    returnStr = ""
    if (operator == "div"):
        op1 = symbolTable.add_variable("divConst", "int", operands[0]) if operands[0].isdigit() else operands[0]
        returnStr += ("addiu " + symbolTable.get_register("divConst") + ", $0, "
                      + symbolTable.get_value_from_name("divConst")) + "\n" if operands[0].isdigit() else ""
        op2 = symbolTable.add_variable("divConst", "int", operands[1]) if operands[1].isdigit() else operands[1]
        returnStr += ("addiu " + symbolTable.get_register("divConst") + ", $0, "
                      + symbolTable.get_value_from_name("divConst") + "\n") if operands[1].isdigit() else ""
        returnStr += operator
        returnStr += " " + str(op1) + ", " + str(op2) + "\n"
        returnStr += "mflo " + lhs + "\n"
    elif (operator == "mult"):
        op1 = symbolTable.add_variable("multConst", "int", operands[0]) if operands[0].isdigit() else operands[0]
        returnStr += ("addiu " + symbolTable.get_register("multConst") + ", $0, "
                      + symbolTable.get_value_from_name("multConst")) + "\n" if operands[0].isdigit() else ""
        op2 = symbolTable.add_variable("multConst", "int", operands[1]) if operands[1].isdigit() else operands[1]
        returnStr += ("addiu " + symbolTable.get_register("multConst") + ", $0, "
                      + symbolTable.get_value_from_name("multConst") + "\n") if operands[1].isdigit() else ""
        returnStr += operator
        returnStr += " " + str(op1) + ", " + str(op2) + "\n"
        returnStr += "mflo " + lhs + "\n"
    else:
        # When two operands are register
        op1 = operands[0]
        if (operands[0].isdigit()):
            op1 = symbolTable.add_variable(operator+"Const", "int", operands[0])
            returnStr += "addiu " + op1 + ", " + "$0, " +  operands[0] + "\n"
        if (operands[1].isdigit()):
            returnStr += operator + "iu " + lhs + ", " + op1 + ", " + operands[1] + "\n"
        else:
            returnStr += operator + " " + lhs + ", " + op1 + ", " + operands[1] + "\n"
    return returnStr
# def processOperation(haveConstant, operator,lhs, operands, symbolTable):
#     returnStr = ""
#     if (operator == "div"):
#         print(operands[0])
#         print(type(operands[0]))
#         print(operands[0].isdigit())
#         print(operands[1])
#         print(type(operands[1]))
#         print(operands[1].isdigit())
#         op1 = symbolTable.add_variable("divConst", "int", operands[0]) if operands[0].isdigit() else operands[0]
#         returnStr += ("addiu " + symbolTable.get_register("divConst")+ ", $0,  "
#                       + symbolTable.get_value_from_name("divConst")) + "\n" if operands[0].isdigit() else ""
#         op2 = symbolTable.add_variable("divConst", "int", operands[1]) if operands[1].isdigit() else operands[1]
#         returnStr += ("addiu " + symbolTable.get_register("divConst") + ", $0, "
#                       + symbolTable.get_value_from_name("divConst") + "\n") if operands[1].isdigit() else ""
#         returnStr += operator
#         returnStr += " " + str(op1) + ", " + str(op2) + "\n"
#         returnStr += "mflo " + lhs + "\n"
#     else:
#         returnStr += operator
#         if (haveConstant):
#             returnStr += "iu"
#         returnStr += " " + lhs + ", " + operands[0] + ", " + operands[1] + "\n"
#     return returnStr

def switchOperator(operator):
    # Comparison operator
    if (operator == "=="):
        return "bne"
    elif (operator == "<"):
        return "bge"
    elif (operator == ">"):
        return "ble"
    elif (operator == "<="):
        return "bgt"
    elif (operator == ">="):
        return "blt"
    # Calculation Operators
    elif (operator == "+"):
        return "add"
    elif (operator == "-"):
        return "sub"
    elif (operator == "&"):
        return "and"
    elif (operator == "/"):
        return "div"
    elif (operator == "*"):
        return "mult"