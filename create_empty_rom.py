with open("ROM.bin", "wb") as f:
    f.write(bytearray((2**24)*2))