int main() {
    int x = 2;
    int y = 6;
    //-------- One parameter in the RHS ----------------
    x = 2
    //-------- Two parameters in the RHS ----------------
    // Addition
    // Operand 1 : const    -----   Operand 2: const
    x = 2 + 3
    // Operand 1 : const    -----   Operand 2: label
    x = 2 + y
    // Operand 1 : label    -----   Operand 2: const
    x = y + 4
    // Operand 1 : label    -----   Operand 2: label
    x = x + y
    // Subtraction
    // Operand 1 : const    -----   Operand 2: const
    x = 4 - 1
    // Operand 1 : const    -----   Operand 2: label
    x = 6 - y
    // Operand 1 : label    -----   Operand 2: const
    x = y - 4
    // Operand 1 : label    -----   Operand 2: label
    x = y - x
    // Division
    // Operand 1 : const    -----   Operand 2: const
    x = 4/2
    // Operand 1 : const    -----   Operand 2: label
    x = 10/y
    // Operand 1 : label    -----   Operand 2: const
    x = y/5
    // Operand 1 : label    -----   Operand 2: label
    x = y/x
    // Multiplication
    // Operand 1 : const    -----   Operand 2: const
    x = 4*2
    // Operand 1 : const    -----   Operand 2: label
    x = 10*y
    // Operand 1 : label    -----   Operand 2: const
    x = y*5
    // Operand 1 : label    -----   Operand 2: label
    x = y*x

}