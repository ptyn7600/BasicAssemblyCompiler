import xml.etree.ElementTree as ET
from hashTable import hashTable


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Open XML file
    file = ET.parse('testing.xml')
    program = file.getroot()
    # Create assembly file
    asmfile = open("testing.asm", "a")
    # Create the look up table
    symbolTable = hashTable()

    for instruction in program:
        instructionType = instruction.tag
        print("============================")
        print(instructionType)
        # Parsing Variables
        if (instructionType == "variable"):
            name = ""
            type = ""
            value = 0
            print("Parsing variable instruction...")
            for attribute in instruction:
                if (attribute.tag == "name"):
                   name = attribute.text
                if (attribute.tag == "type"):
                   type = attribute.text
                if (attribute.tag == "value"):
                   value = int(attribute.text)
            # add to the symbol table
            symbolTable.add_variable(name, type, value)



    # ========================================== #
    # Testing Hashing
    # symbolTable = hashTable()
    # symbolTable.add_variable("a", "int", 4)
    # symbolTable.add_variable("b", "char", 0)
    # print(symbolTable.get_type("a"))
    # print(symbolTable.get_value("b"))






