addiu $s0, $0, 7
addiu $t0, $0, 0
FOR_0_INIT:
addiu $t1, $0, 0
addiu $t2, $0, 32
FOR_0_COND:
bge $t1, $t2, FOR_0_EXIT
andiu $t3, $s0, 1
add $t0, $t0, $t3
addiu $t4, $0, 2
div $s0, $t4
mflo $s0
FOR_0_INCRE:
addiu $t1, $t1, 1
j FOR_0_COND
FOR_0_EXIT:
li $v0, 10
syscall