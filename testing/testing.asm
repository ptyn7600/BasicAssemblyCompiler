addiu $t0, $0, 0
addiu $t1, $0, 0
addiu $t2, $0, 0
bne $t0, $t1, ELSE_0
IF_0_TRUE:
addiu $t0, $0, 7
j IF_0_EXIT
ELSE_0:
addiu $t0, $0, 8
j IF_0_EXIT
IF_0_EXIT:
WHILE_0_INIT:
addiu $t3, $0, 10
WHILE_0_COND:
bge $t2, $t3, WHILE_0_EXIT
addi $t0, $t0, 1
addi $t2, $t2, 1
j WHILE_0_COND
WHILE_0_EXIT:
li $v0, 10
syscall