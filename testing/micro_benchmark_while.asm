addiu $t0, $0, 0
addiu $t1, $0, 10
addiu $t2, $0, 0
addiu $t3, $0, 0
WHILE_0_INIT:
addiu $t4, $0, 5
WHILE_0_COND:
bge $t0, $t4, WHILE_0_EXIT
add $t2, $t2, $t0
addiu $t0, $t0, 1
j WHILE_0_COND
WHILE_0_EXIT:
WHILE_1_INIT:
addiu $t5, $0, 5
WHILE_0_COND:
ble $t1, $t5, WHILE_0_EXIT
add $t3, $t3, $t1
subiu $t1, $t1, 1
j WHILE_1_COND
WHILE_0_EXIT:
li $v0, 10
syscall