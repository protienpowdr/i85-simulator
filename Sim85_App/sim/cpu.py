from sim.simapi import bytewrap, wordwrap


# Peripheral Classes
class MemoryModule:
    def __init__(self):
        self.MAX_BYTES = 65536
        self.START_ADDR = 0x0000
        self.END_ADDR = 0xFFFF

        self.data = bytearray(self.MAX_BYTES)

class IOModule:
    def __init__(self):
        self.MAX_BYTES = 256
        self.START_ADDR = 0x00
        self.END_ADDR = 0xFF
        self.data = bytearray(self.MAX_BYTES)







# Main CPU Container
class Core:
    # Using __slots__ to keep registers in a fast low level array and make access faster
    # __Slots__ also avoids definition of new attributes at runtime.

    __slots__ = ('acc','rb','rc','rd','re','rh','rl','rf','sp','pc','mar','mdr')

    ram = MemoryModule()
    ports = IOModule()

    def __init__(self):


        # 8 Bit Registers
        self.acc = 0
        self.rb = 0
        self.rc = 0
        self.rd = 0
        self.re = 0
        self.rh = 0
        self.rl = 0
        self.rf = 0

        # 16 Bit Registers
        self.sp = 0
        self.pc = 0

        # Memory Access Registers
        self.mar = 0
        self.mdr = 0

    # Basic Increment & Decrement Functions
    @staticmethod
    def increment_reg(reg,val=1):
        return bytewrap(reg + val)

    @staticmethod
    def decrement_reg(reg,val=1):
        return bytewrap(reg - val)



    # Classwide Memory & IO Functions
    @classmethod
    def memory_read(cls,obj):
        obj.mdr = bytewrap(cls.ram.data[wordwrap(obj.mar)])

    @classmethod
    def memory_write(cls,obj):
        cls.ram.data[wordwrap(obj.mar)] = obj.mdr

    @classmethod
    def io_read(cls,obj):
        obj.mdr = bytewrap(cls.ports.data[bytewrap(obj.mar)])

    @classmethod
    def io_write(cls,obj):
        cls.ports.data[bytewrap(obj.mar)] = obj.mdr



    # 16 Bit Register Increment & Decrement
    def increment_pc(self,val = 1 ):
        self.pc = wordwrap(self.pc + val)

    def decrement_pc(self,val = 1 ):
        self.pc = wordwrap(self.pc - val)

    def increment_sp(self,val = 1 ):
        self.sp = wordwrap(self.sp + val)

    def decrement_sp(self,val = 1 ):
        self.sp = wordwrap(self.sp - val)

    def increment_mar(self,val = 1 ):
        self.mar = wordwrap(self.mar + val)

    def decrement_mar(self,val = 1 ):
        self.mar = wordwrap(self.mar - val)



    # Flag SET & RESET Bitmasks
    def flag_cy(self,val):
        if val:
            self.rf = self.rf | 0b00000001
        else:
            self.rf = self.rf & 0b11111110

    def flag_p(self,val):
        if val:
            self.rf = self.rf | 0b00000100
        else:
            self.rf = self.rf & 0b11111011

    def flag_ac(self,val):
        if val:
            self.rf = self.rf | 0b00010000
        else:
            self.rf = self.rf & 0b11101111

    def flag_z(self,val):
        if val:
            self.rf = self.rf | 0b01000000
        else:
            self.rf = self.rf & 0b10111111

    def flag_s(self,val):
        if val:
            self.rf = self.rf | 0b10000000
        else:
            self.rf = self.rf & 0b01111111

    def flag_v(self,val):
        if val:
            self.rf = self.rf | 0b00000010
        else:
            self.rf = self.rf & 0b11111101

    def flag_k(self,val):
        if val:
            self.rf = self.rf | 0b00100000
        else:
            self.rf = self.rf & 0b11011111

    def getflag(self,flag,as_int=False):
        f = (self.rf >> flag) & 0b00000001
        if as_int:
            return int(f)
        return bool(f)



