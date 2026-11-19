from sim.instructions import InstructionTable
from sim.opcodes import Op
from sim.cpu import Core
from sim.simapi import *

import time

c85 = Core()
try:

    print("DAD B TEST")
    c85.rh = 0x7f
    c85.rl = 0x00
    c85.rb = 0x01
    c85.rc = 0x00
    print("Value of hl before dad b", hex(c85.rh),hex(c85.rl))
    start = time.perf_counter_ns()
    Result = InstructionTable[Op.DADB].function(ExecArgs(cpu=c85,arg_sample=None))
    end = time.perf_counter_ns()


    if InstructionSuccessful in Result.events:
        print("Value of hl after dad b", hex(c85.rh),hex(c85.rl))
        print("Value of flag register : ", hex(c85.rf))
        print("Flag CY", c85.getflag(Flags.CARRY))
        print("Flag P", c85.getflag(Flags.PARITY))
        print("Flag V", c85.getflag(Flags.XV))
        print("Flag K", c85.getflag(Flags.XK))
        print("Flag AC", c85.getflag(Flags.AUXCARRY))
        print("Flag Z", c85.getflag(Flags.ZERO))
        print("Flag S", c85.getflag(Flags.SIGN))
    print('Exec time approx : ', end - start , 'ns')
except KeyboardInterrupt:
    print("Execution Terminated...")
