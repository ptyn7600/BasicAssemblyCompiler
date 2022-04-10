addiu $t0, $0, 5
addiu $t1, $0, 0
addiu $t2, $0, 3
ble $t0, $t2, ELSE_0
IF_0_TRUE:
addiu $t1, $0, 1
j IF_0_EXIT
ELSE_0:
j IF_0_EXIT
IF_0_EXIT:
li $v0, 10
syscall