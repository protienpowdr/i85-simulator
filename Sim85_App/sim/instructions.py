from sim.opcodes import  Op
import sim.functions as fn

class Instruction:
    __slots__ = ("function","size","cycles")

    def __init__(self, function, size, cycles):
        self.function = function
        self.size = size
        self.cycles = cycles


""" Main Instruction Table
Defining InstructionTable list that can hold Instruction OR None with 256 Elements, 
undocumented instructions default to exec_undefined as a fallback. """
InstructionTable: list[Instruction | None] = [None] * 256



InstructionTable[Op.NOP] = Instruction(fn.exec_nop, 1, 4)               # NOP

InstructionTable[Op.LXIB] = Instruction(fn.exec_lxib, 3, 10)            # LXI B

InstructionTable[Op.STAXB] = Instruction(fn.exec_staxb, 1, 7)           # STAX B

InstructionTable[Op.INXB] = Instruction(fn.exec_inxb, 1, 6)             # INX B

InstructionTable[Op.INRB] = Instruction(fn.exec_inrb, 1, 4)             # INR B

InstructionTable[Op.DCRB] = Instruction(fn.exec_dcrb, 1 , 4)            # DCR B

InstructionTable[Op.MVIB] = Instruction(fn.exec_mvib, 2, 7)             # MVI B

InstructionTable[Op.RLC] = Instruction(fn.exec_rlc, 1 , 4)              # RLC

InstructionTable[Op.DSUB] = Instruction(fn.exec_undefined , 1 , 10)     # DSUB

InstructionTable[Op.DADB] = Instruction(fn.exec_dadb , 1 , 10)          # DAD B

InstructionTable[Op.LDAXB] = Instruction(fn.exec_ldaxb, 1 , 7)          # LDAX B

InstructionTable[Op.DCXB] = Instruction(fn.exec_dcxb , 1 , 6)           # DCX B

InstructionTable[Op.INRC] = Instruction(fn.exec_inrc , 1 , 4)           # INR C

InstructionTable[Op.DCRC] = Instruction(fn.exec_dcrc , 1 , 4)           # DCR C

InstructionTable[Op.MVIC] = Instruction(fn.exec_mvic , 2 , 7)           # MVI C

InstructionTable[Op.RRC] = Instruction(fn.exec_rrc , 1 , 4)             # RRC