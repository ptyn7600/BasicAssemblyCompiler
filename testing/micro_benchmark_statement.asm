addiu $t0, $0, 2
addiu $t1, $0, 6
mult $t1, $t0
mflo $t0
li $v0, 10
syscall