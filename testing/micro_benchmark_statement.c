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
    //-------- Three parameters in the RHS ----------------
    // ======================================================================== LINE 277
    // Operator 1 : +          -----   Operator 2: +
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 + (2 + 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 + (2 + y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 + (y + 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 + (y + y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y + (2 + 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y + (2 + y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y + (y + 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y + (y + y)
    // ======================================================================== LINE 469
    // Operator 1 : +          -----   Operator 2: -
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 + (2 - 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 + (2 - y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 + (y - 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 + (y - y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y + (2 - 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y + (2 - y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y + (y - 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y + (y - y)
    // ======================================================================== LINE 664
    // Operator 1 : +          -----   Operator 2: *
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 + (2 * 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 + (2 * y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 + (y * 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 + (y * y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y + (2 * 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y + (2 * y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y + (y * 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y + (y * y)
    // ======================================================================== LINE 857
    // Operator 1 : +          -----   Operator 2: /
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 + (2 / 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 + (2 / y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 + (y / 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 + (y / y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y + (2 / 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y + (2 / y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y + (y / 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y + (y / y)
    // ========================================================================  LINE 1050
    // Operator 1 : -          -----   Operator 2: +
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 - (2 + 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 - (2 + y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 - (y + 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 - (y + y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y - (2 + 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y - (2 + y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y - (y + 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y - (y + y)
    // ======================================================================== LINE 1243
    // Operator 1 : -          -----   Operator 2: -
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 - (2 - 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 - (2 - y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 - (y - 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 - (y - y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y - (2 - 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y - (2 - y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y - (y - 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y - (y - y)
    // ========================================================================
    // Operator 1 : -          -----   Operator 2: *
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 - (2 * 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 - (2 * y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 - (y * 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 - (y * y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y - (2 * 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y - (2 * y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y - (y * 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y - (y * y)
    // ========================================================================
    // Operator 1 : -          -----   Operator 2: /
     // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: const
    x = 5 - (2 / 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 - (2 / y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 - (y / 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 - (y / y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y - (2 / 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y - (2 / y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y - (y / 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y - (y / y)
    // ======================================================================== NOT TESTED BECAUSE SAME AS (+,*)
    // Operator 1 : *          -----   Operator 2: +
     x = 5 * (2 + 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 * (2 + y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 * (y + 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 * (y + y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y * (2 + 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y * (2 + y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y * (y + 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y * (y + y)
    // ======================================================================== NOT TESTED BECAUSE SAME AS (-,*)
    // Operator 1 : *          -----   Operator 2: -
    x = 5 * (2 - 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 * (2 - y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 * (y - 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 * (y - y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y * (2 - 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y * (2 - y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y * (y - 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y * (y - y)
    // ========================================================================
    // Operator 1 : *          -----   Operator 2: *
     x = 5 * (2 * 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 * (2 * y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 * (y * 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 * (y * y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y * (2 * 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y * (2 * y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y * (y * 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y * (y * y)
    // ========================================================================
    // Operator 1 : *          -----   Operator 2: /
     x = 5 * (2 / 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 * (2 / y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 * (y / 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 * (y / y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y * (2 / 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y * (2 / y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y * (y / 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y * (y / y)
    // ======================================================================== NOT TESTED BECAUSE SAME AS (+,/)
    // Operator 1 : /          -----   Operator 2: +
    x = 5 * (2 + 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 / (2 + y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 / (y + 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 / (y + y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y / (2 + 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y / (2 + y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y / (y + 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y / (y + y)
    // ======================================================================== NOT TESTED BECAUSE SAME AS (-,/)
    // Operator 1 : /          -----   Operator 2: -
    x = 5 / (2 - 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 / (2 - y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 / (y - 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 / (y - y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y / (2 - 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y / (2 - y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y / (y - 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y / (y - y)
    // ========================================================================
    // Operator 1 : /          -----   Operator 2: *
    x = 5 / (2 * 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 / (2 * y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 / (y * 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 / (y * y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y / (2 * 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y / (2 * y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y / (y * 2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y / (y * y)
    // ========================================================================
    // Operator 1 : /          -----   Operator 2: /
    x = 5 / (2 / 3)
    // Operand 1 : const    -----   Operand 2: const   -----   Operand 3: label
    x = 5 / (2 / y)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: const
    x = 5 / (y / 10)
    // Operand 1 : const    -----   Operand 2: label   -----   Operand 3: label
    x = 5 / (y / y)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: const
    x = y / (2 / 3)
    // Operand 1 : label    -----   Operand 2: const   -----   Operand 3: label
    x = y / (2 / y)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: const
    x = y / (y /2)
    // Operand 1 : label    -----   Operand 2: label   -----   Operand 3: label
    x = y / (y / y)
}