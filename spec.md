# MyCPU - Spec

regX -> reference to register X
[*regX] -> reference to value in register X

====INSTRUCTIONS====

all instructions are at a fixed size of 2bytes or 16bits
[4bits instruction select][12bits for possible parameters, value ignored if unused]

memory(ram) has 8bits of data at each address

0 nop [] ; nop, clears flag
1 jnf [reg1][reg2][reg3] ; jump not flag to [*reg1][*reg2][*reg3] in ROM
2 ldi [reg][8bit value]; load immidiate to reg1
3 cpy [reg1][reg2]; copy [*reg1] to reg2
4 lda [reg1][reg2][reg3]; load data from ram at [*reg2][*reg3] into reg1
5 sta [reg1][reg2][reg3]; store data to ram at [*reg2][*reg3] from reg1
6 add [reg1][reg2]; add [*reg1][*reg2], store in reg1, set flag on carry
7 sub [reg1][reg2]; subtract [*reg1][*reg2], store in reg1, set flag on carry
8 hid [reg1][reg2][reg3]; set hid select port to [*reg1], and hid dataOut to [*reg2][*reg3], store result from dataIn in {always} register 0x1 . ??Assigning/Managing ids of devices is left to the user??
9 les [reg1][reg2]; compare [*reg1] <  [*reg2], set flag if true
a equ [reg1][reg2]; compare [*reg1] == [*reg2], set flag if true
b and [reg1][reg2]; and [*reg1][*reg2], store in reg1, set flag if result 0
c orr [reg1][reg2] ; or [*reg1][*reg2], store in reg1, set flag if result 0
d xor [reg1][reg2] ; xor [*reg1][*reg2], store in reg1, set flag if result 0
e not [reg] ; not [*reg], store in reg, set flag if result 0
f hlt []; halt with exit code [*reg0]

====REGISTERS====

every register is 8bits in value

0 gpo reg
1 gpo reg
2 gpo reg
3 gpo reg
4 gpo reg
5 gpo reg
6 gpo reg
7 gpo reg
8 gpo reg
9 gpo reg + Debug out ; value is displayed with LEDs, can be used as display
a gpo reg + Debug out ; value is displayed with LEDs, can be used as display
b gpo reg + Debug out ; value is displayed with LEDs, can be used as display
c gpo reg + Debug out ; value is displayed with LEDs, can be used as display
d R/O reg ; value is set by physical switches, software read only
e R/O reg ; value is set by physical switches, software read only
f R/O reg ; value is set by physical switches, software read only

hidden:
24bit PC

====FLAG====
single flag, only used by jnf
after each instruction, the flag is cleared.