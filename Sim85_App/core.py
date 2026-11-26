from sim.instructions import InstructionTable
from sim.opcodes import Op
from sim.cpu import Core
from sim.simapi import *

import time

c85 = Core()
try:

    print("LXI D TEST")
    c85.rb = 0x00
    c85.rc = 0x00
    print("Value of D/E before LXIB", hex(c85.rd), hex(c85.re))
    start = time.perf_counter_ns()
    Result = InstructionTable[Op.LXID].function(ExecArgs(cpu=c85,arg_sample=[0x56,0x25]))
    end = time.perf_counter_ns()


    if InstructionSuccessful in Result.events:
        print("Value of D/E before LXIB", hex(c85.rd), hex(c85.re))
        print("Flag CY", c85.getflag(Flags.CARRY))
        print("Flag P", c85.getflag(Flags.PARITY))
        print("Flag V", c85.getflag(Flags.XV))
        print("Flag K", c85.getflag(Flags.XK))
        print("Flag AC", c85.getflag(Flags.AUXCARRY))
        print("Flag Z", c85.getflag(Flags.ZERO))
        print("Flag S", c85.getflag(Flags.SIGN))
        print("Flag Register :",hex(c85.rf))
    print('Exec time approx : ', end - start , 'ns')
except KeyboardInterrupt:
    print("Execution Terminated...")
