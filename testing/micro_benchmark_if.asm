addiu $t0, $0, 5
addiu $t1, $0, 0
addiu $t2, $0, 0
addiu $t3, $0, 3
ble $t0, $t3, ELSE_0
IF_0_TRUE:
addiu $t1, $0, 1
j IF_0_EXIT
ELSE_0:
j IF_0_EXIT
IF_0_EXIT:
addiu $t4, $0, 4
addiu $t5, $0, 3
ble $t4, $t5, ELSE_1
IF_1_TRUE:
addiu $t1, $0, 2
j IF_1_EXIT
ELSE_1:
j IF_1_EXIT
IF_1_EXIT:
bge $t0, $t1, ELSE_2
IF_2_TRUE:
addiu $t1, $0, 3
j IF_2_EXIT
ELSE_2:
addiu $t2, $0, 4
j IF_2_EXIT
IF_2_EXIT:
li $v0, 10
syscall