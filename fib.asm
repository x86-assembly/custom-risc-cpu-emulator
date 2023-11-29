ldi 0, 01
ldi 1, 01
ldi f, 08
ldi e, 04
    cpy 0, 2
    add 2, 1
    jnf d, d, f
    hlt
    cpy 1, 0
    cpy 2, 1
    hid 0
    jnf d, d, e