addiu $t0, $0, 0
addiu $t1, $0, 0
beq $t0, $t1, IF_0_TRUE
j ELSE_0
IF_0_TRUE:
addiu $t0, $0, 7
ELSE_0:
addiu $t0, $0, 8