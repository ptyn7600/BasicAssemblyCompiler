addiu $s0, $0, 0
addiu $t0, $0, 0
FOR_0_INIT:
addiu $t1, $0, 0
addiu $t2, $0, 5
FOR_0_COND:
bge $t1, $t2, FOR_0_EXIT
addiu $t3, $0, 3
div $t1, $t3
mflo $t0
addiu $t4, $0, 0
bne $t0, $t4, ELSE_0
IF_0_TRUE:
addiu $s0, $s0, 1
j IF_0_EXIT
ELSE_0:
j IF_0_EXIT
IF_0_EXIT:
FOR_0_INCRE:
addiu $t1, $t1, 1
j FOR_0_COND
FOR_0_EXIT:
addiu $t5, $0, 6
blt $s0, $t0, ELSE_1
IF_1_TRUE:
WHILE_0_INIT:
addiu $t6, $0, 3
WHILE_0_COND:
ble $t5, $t6, WHILE_0_EXIT
mult $s0, $t5
mflo $s0
subiu $t5, $t5, 1
j WHILE_0_COND
WHILE_0_EXIT:
j IF_1_EXIT
ELSE_1:
addiu $s0, $0, 10
j IF_1_EXIT
IF_1_EXIT:
li $v0, 10
syscall