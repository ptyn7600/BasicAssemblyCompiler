addiu $t0, $0, 2
addiu $t1, $0, 6
mult $t1, $t1
mflo $t2
mult $t1, $t2
mflo $t0
li $v0, 10
syscall