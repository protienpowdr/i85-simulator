from sim.instructions import InstructionTable
from sim.opcodes import Op
from sim.cpu import Core
from sim.simapi import *

import time

c85 = Core()
try:

    print("RRC Test")
    c85.acc = 0x02
    print("Value of Acc before RRC", hex(c85.acc))
    start = time.perf_counter_ns()
    Result = InstructionTable[Op.RRC].function(ExecArgs(cpu=c85,arg_sample=None))
    end = time.perf_counter_ns()


    if InstructionSuccessful in Result.events:
        print("Value of Acc after RRC", hex(c85.acc))
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
