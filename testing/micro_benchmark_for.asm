addiu $t0, $0, 0
addiu $t1, $0, 0
FOR_0_INIT:
addiu $t2, $0, 0
addiu $t3, $0, 5
FOR_0_COND:
bge $t2, $t3, FOR_0_EXIT
add $t0, $t0, $t2
FOR_0_INCRE:
addiu $t2, $t2, 1
j FOR_0_COND
FOR_0_EXIT:
FOR_1_INIT:
addiu $t4, $0, 10
addiu $t5, $0, 5
FOR_1_COND:
ble $t4, $t5, FOR_1_EXIT
add $t1, $t1, $t4
FOR_1_INCRE:
subiu $t4, $t4, 1
j FOR_1_COND
FOR_1_EXIT:
li $v0, 10
syscall