import time
OPCODES = {
    "nop" : 0x0,
    "jnf" : 0x1,
    "ldi" : 0x2,
    "cpy" : 0x3,
    "lda" : 0x4,
    "sta" : 0x5,
    "add" : 0x6,
    "sub" : 0x7,
    "hid" : 0x8,
    "les" : 0x9,
    "equ" : 0xa,
    "and" : 0xb,
    "orr" : 0xc,
    "xor" : 0xd,
    "not" : 0xe,
    "hlt" : 0xf
}


rev_OPCODES = {
    0x0 : "nop",
    0x1 : "jnf",
    0x2 : "ldi",
    0x3 : "cpy",
    0x4 : "lda",
    0x5 : "sta",
    0x6 : "add",
    0x7 : "sub",
    0x8 : "hid",
    0x9 : "les",
    0xa : "equ",
    0xb : "and",
    0xc : "orr",
    0xd : "xor",
    0xe : "not",
    0xf : "hlt"
}

DEBUG = True

class CPU:
    def start(self, ROM, ram=bytearray(2**16)):
        self.ROM = ROM  
        self.ram = ram  
        self.flag= False
        self.halt= False
        self.pc  = 0
        self.regs = bytearray(16)

        self.run()

        with open("ram_dump", "wb") as f:
            f.write(self.ram)
    def run(self):

        while not(self.halt):
            new_flag = False
            instruction_b1 = self.ROM[(self.pc *2)]
            instruction_b2 = self.ROM[(self.pc *2) + 1]

            opcode = instruction_b1 >> 4
            Ireg1 = instruction_b1 & 0b1111

            Ireg2 = instruction_b2 >> 4
            Ireg3 = instruction_b2 & 0b1111

            jumped = False

            if(DEBUG):
                print(f"[{self.pc}]: Opcode: {rev_OPCODES[opcode]}, Ireg1: {Ireg1}, Ireg2: {Ireg2}, Ireg3: {Ireg3}, new: {new_flag}, {self.flag}", end="")

            if(opcode == OPCODES["nop"]):
                pass
            elif(opcode == OPCODES["jnf"]):
                if(not(self.flag)):
                    self.pc = (self.regs[Ireg1] << 16) + (self.regs[Ireg2] << 8) + self.regs[Ireg3]
                    jumped = True
                    print(f", {(self.regs[Ireg1] << 16) + (self.regs[Ireg2] << 8) + self.regs[Ireg3]}", end="")
            elif(opcode == OPCODES["ldi"]):
                self.regs[Ireg1] = (Ireg2 << 4) + Ireg3
            elif(opcode == OPCODES["cpy"]):
                self.regs[Ireg2] = self.regs[Ireg1]
            elif(opcode == OPCODES["lda"]):
                self.regs[Ireg1] = self.ram[self.regs[Ireg2]<<8 + self.regs[Ireg3]]
            elif(opcode == OPCODES["sta"]):
                self.ram[self.regs[Ireg2]<<8 + self.regs[Ireg3]] = self.regs[Ireg1]
            elif(opcode == OPCODES["add"]):
                _calc_val = self.regs[Ireg1] + self.regs[Ireg2]
                if(_calc_val > 255):
                    self.flag = True
                    new_flag = True

                self.regs[Ireg1] = _calc_val % 256

            elif(opcode == OPCODES["sub"]):
                _calc_val = self.regs[Ireg1] - self.regs[Ireg2]

                if _calc_val < 0:
                    self.flag = True
                    new_flag = True
                    _calc_val = (_calc_val & 0xFF)
                
                self.regs[Ireg1] = _calc_val

            elif(opcode == OPCODES["hid"]):
                # ! not implemented yet, used for debug reg print
                if(DEBUG):
                    print(f", debug_print: {self.regs[Ireg1]}", end="")
                pass
            elif(opcode == OPCODES["les"]):
                if(self.regs[Ireg1] < self.regs[Ireg2]):
                    self.flag = True
                    new_flag = True

            elif(opcode == OPCODES["equ"]):
                if(self.regs[Ireg1] == self.regs[Ireg2]):
                    self.flag = True
                    new_flag = True

            elif(opcode == OPCODES["and"]):
                self.regs[Ireg1] = self.regs[Ireg1] & self.regs[Ireg2]
                
            elif(opcode == OPCODES["orr"]):
                self.regs[Ireg1] = self.regs[Ireg1] | self.regs[Ireg2]
                
            elif(opcode == OPCODES["xor"]):
                self.regs[Ireg1] = self.regs[Ireg1] ^ self.regs[Ireg2]
                
            elif(opcode == OPCODES["not"]):
                self.regs[Ireg1] = self.regs[Ireg1] ^ 0xff

            elif(opcode == OPCODES["hlt"]):
                self.halt = True

            if(not(new_flag)):
                self.flag=False

            if(not(jumped)):
                self.pc+=1
            print()

            
        return


if __name__ == "__main__":
    ROM = 0;
    with open("ROM.bin", "rb") as tmpROM:
        ROM = bytearray(tmpROM.read());
    Ram = bytearray(2**24)
    myCPU = CPU()

    myCPU.start(ROM, ram=Ram)
