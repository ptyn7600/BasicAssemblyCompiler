import xml.etree.ElementTree as ET
from hashTable import hashTable

# Global variables
if_count = 0

def assConvertIf(operator, operands):
    returnStr = ""
    if (operator == "=="):
        returnStr += "beq " + symbolTable.get_register(operands[0]) + ", " + symbolTable.get_register(operands[1])
        returnStr += ", IF_" + str(if_count) + "_TRUE\nj ELSE_" + str(if_count) + "\n"
        return returnStr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Open XML file
    file = ET.parse('testing.xml')
    program = file.getroot()
    # Create assembly file
    asmfile = open("testing.asm", "w")
    # Create the look up table
    symbolTable = hashTable()

    for instruction in program:
        instructionType = instruction.tag
        print("============================")
        print(instructionType)
        # ======================================= #
        # Parsing Variables
        if (instructionType == "variable"):
            name = ""
            type = ""
            value = 0
            print("Parsing VARIABLE instruction...")
            for attribute in instruction:
                if (attribute.tag == "name"):
                   name = attribute.text
                if (attribute.tag == "type"):
                   type = attribute.text
                if (attribute.tag == "value"):
                   value = int(attribute.text)
            # add to the symbol table
            symbolTable.add_variable(name, type, value)
            # Write assembly instruction
            asmfile.write("addiu " + symbolTable.get_register(name) + ", $0, " + str(value) + "\n")
            print("addiu " + symbolTable.get_register(name) + ", $0, " + str(value) + "\n")
        # ======================================= #
        # Parsing If statement
        if (instructionType == "if"):
            print("Parsing IF instruction...")
            for ifPart in instruction:
                if ((ifPart.tag) == "expression"):
                    operator = ""
                    operands = []
                    for attribute in ifPart:
                        if(attribute.tag == "operator"):
                            operator = attribute.text
                        else:
                            operands.append(attribute.text)
                    ass_intr = assConvertIf(operator, operands)
                    # Write assembly instruction
                    asmfile.write(ass_intr + "\n")
                    print(ass_intr + "\n")
            if_count += 1


    # ========================================== #
    # Close the assembly file and save the file
    asmfile.close()
    # ========================================== #
    # Testing Hashing
    # symbolTable = hashTable()
    # symbolTable.add_variable("a", "int", 4)
    # symbolTable.add_variable("b", "char", 0)
    # print(symbolTable.get_type("a"))
    # print(symbolTable.get_value("b"))






