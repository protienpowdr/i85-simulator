from sim.cpu import Core
from sim.simapi import *
import sim.eval_flags as ev

def exec_nop(args : ExecArgs):
    return_obj = ExecReturn()
    return_obj.add_event(NoOperation,InstructionSuccessful,ContinueExecution)
    return return_obj

def exec_undefined(args : ExecArgs):
    return_obj = ExecReturn()
    return_obj.add_event(NoOperation,UndocumentedOpcode,ContinueExecution)
    return return_obj

def exec_lxib(args : ExecArgs):
    return_obj = ExecReturn()
    args.cpu.mar = getword(lb=args.arg_sample[0],hb=args.arg_sample[1])
    Core.memory_read(args.cpu)
    args.cpu.rc = args.cpu.mdr
    args.cpu.increment_mar()
    Core.memory_read(args.cpu)
    args.cpu.rb = args.cpu.mdr

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_staxb(args : ExecArgs):
    return_obj = ExecReturn()
    args.cpu.mar = getword(lb=args.cpu.rc,hb=args.cpu.rb)
    args.cpu.mdr =  args.cpu.acc
    Core.memory_write(args.cpu)

    return_obj.add_event(InstructionSuccessful,ContinueExecution,MemoryUpdate)
    return return_obj

def exec_inxb(args : ExecArgs):
    return_obj = ExecReturn()
    num = getword(lb=args.cpu.rc,hb=args.cpu.rb)
    num += 1
    args.cpu.rb = gethb(num)
    args.cpu.rc = bytewrap(num)
    args.cpu.flag_k(ev.check_x5_on_add16(num))

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_inrb(args : ExecArgs):
    return_obj = ExecReturn()

    temp = args.cpu.rb
    args.cpu.rb = Core.increment_reg(args.cpu.rb)

    args.cpu.flag_v(ev.check_overflow_add(temp, 1, args.cpu.rb))
    args.cpu.flag_ac(ev.check_auxiliary_add(temp, 1, args.cpu.rb))
    args.cpu.flag_p(ev.check_parity(args.cpu.rb))
    args.cpu.flag_z(ev.check_zero(args.cpu.rb))
    args.cpu.flag_s(ev.check_sign(args.cpu.rb))
    args.cpu.flag_k(ev.check_x5(sign_flag=args.cpu.getflag(Flags.SIGN,as_int=True),
                                overflow_flag=args.cpu.getflag(Flags.XV,as_int=True)))

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_dcrb(args : ExecArgs):
    """
        The 8085 Internally uses 2's Complement Subtraction,
        However I'm using sub methods for flags for simplicity
    """
    return_obj = ExecReturn()
    temp = args.cpu.rb
    args.cpu.rb = Core.decrement_reg(args.cpu.rb)
    args.cpu.flag_v(ev.check_overflow_sub(temp, 1, args.cpu.rb))
    args.cpu.flag_ac(ev.check_auxiliary_sub(temp, 1, args.cpu.rb))
    args.cpu.flag_p(ev.check_parity(args.cpu.rb))
    args.cpu.flag_z(ev.check_zero(args.cpu.rb))
    args.cpu.flag_s(ev.check_sign(args.cpu.rb))
    args.cpu.flag_k(ev.check_x5(sign_flag=args.cpu.getflag(Flags.SIGN,as_int=True),
                                overflow_flag=args.cpu.getflag(Flags.XV,as_int=True)))

    return_obj.add_event(InstructionSuccessful, ContinueExecution, RegisterUpdate)
    return return_obj

def exec_mvib(args : ExecArgs):
    return_obj = ExecReturn()
    args.cpu.rb = bytewrap(args.arg_sample[0])

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_rlc(args : ExecArgs):
    return_obj = ExecReturn()
    temp = args.cpu.acc
    cy_value = bytewrap(args.cpu.acc >> 7)
    args.cpu.acc = (args.cpu.acc << 1) | cy_value
    args.cpu.flag_v(ev.check_overflow_add(temp,temp, args.cpu.acc))
    if cy_value:
        args.cpu.flag_cy(State.SET)
    else:
        args.cpu.flag_cy(State.RESET)
    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_dadb(args : ExecArgs):
    return_obj = ExecReturn()
    pairbc = getword(lb=args.cpu.rc,hb=args.cpu.rb)
    pairhl = getword(lb=args.cpu.rl,hb=args.cpu.rh)
    result = pairhl + pairbc
    args.cpu.flag_v(ev.check_overflow_add16(pairbc,pairhl,wordwrap(result)))
    if result > 0xffff:
        args.cpu.flag_cy(State.SET)
    else:
        args.cpu.flag_cy(State.RESET)

    args.cpu.rh = gethb(result)
    args.cpu.rl = bytewrap(result)

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_ldaxb(args: ExecArgs):
    return_obj = ExecReturn()
    args.cpu.mar = getword(lb=args.cpu.rc,hb=args.cpu.rb)
    Core.memory_read(args.cpu)
    args.cpu.acc = args.cpu.mdr
    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_dcxb(args : ExecArgs):
    return_obj = ExecReturn()
    num = getword(lb=args.cpu.rc, hb=args.cpu.rb)
    num -= 1
    args.cpu.rb = gethb(num)
    args.cpu.rc = bytewrap(num)
    args.cpu.flag_k(ev.check_x5_on_sub16(num))

    return_obj.add_event(InstructionSuccessful, ContinueExecution, RegisterUpdate)
    return return_obj

def exec_inrc(args : ExecArgs):
    return_obj = ExecReturn()

    temp = args.cpu.rc
    args.cpu.rc = Core.increment_reg(args.cpu.rc)

    args.cpu.flag_v(ev.check_overflow_add(temp, 1, args.cpu.rc))
    args.cpu.flag_ac(ev.check_auxiliary_add(temp, 1, args.cpu.rc))
    args.cpu.flag_p(ev.check_parity(args.cpu.rc))
    args.cpu.flag_z(ev.check_zero(args.cpu.rc))
    args.cpu.flag_s(ev.check_sign(args.cpu.rc))
    args.cpu.flag_k(ev.check_x5(sign_flag=args.cpu.getflag(Flags.SIGN,as_int=True),
                                overflow_flag=args.cpu.getflag(Flags.XV,as_int=True)))

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_dcrc(args : ExecArgs):
    """
        The 8085 Internally uses 2's Complement Subtraction,
        However I'm using sub methods for flags for simplicity
    """
    return_obj = ExecReturn()
    temp = args.cpu.rc
    args.cpu.rc = Core.decrement_reg(args.cpu.rc)
    args.cpu.flag_v(ev.check_overflow_sub(temp, 1, args.cpu.rc))
    args.cpu.flag_ac(ev.check_auxiliary_sub(temp, 1, args.cpu.rc))
    args.cpu.flag_p(ev.check_parity(args.cpu.rc))
    args.cpu.flag_z(ev.check_zero(args.cpu.rc))
    args.cpu.flag_s(ev.check_sign(args.cpu.rc))
    args.cpu.flag_k(ev.check_x5(sign_flag=args.cpu.getflag(Flags.SIGN,as_int=True),
                                overflow_flag=args.cpu.getflag(Flags.XV,as_int=True)))

    return_obj.add_event(InstructionSuccessful, ContinueExecution, RegisterUpdate)
    return return_obj

def exec_mvic(args : ExecArgs):
    return_obj = ExecReturn()
    args.cpu.rc = bytewrap(args.arg_sample[0])

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj

def exec_rrc(args : ExecArgs):
    return_obj = ExecReturn()
    cy_value = bytewrap(args.cpu.acc & 1)
    args.cpu.acc = (args.cpu.acc >> 1)  | (cy_value << 7)
    args.cpu.flag_v(State.RESET)
    if cy_value:
        args.cpu.flag_cy(State.SET)
    else:
        args.cpu.flag_cy(State.RESET)

    return_obj.add_event(InstructionSuccessful,ContinueExecution,RegisterUpdate)
    return return_obj