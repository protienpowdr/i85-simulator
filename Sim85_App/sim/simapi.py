
# Convert the result to uint8_t
def bytewrap(arg):
    return arg & 0xFF

# Convert the result to unit16_t
def wordwrap(arg):
    return arg & 0xFFFF

# Return uint16 from hb and lb
def getword(lb , hb):
    return wordwrap((hb << 8) + lb)

# Return the higher order byte
def gethb(uint16):
    return bytewrap(uint16 >> 8)


# Stores bit positions of the 8085 flags
class Flags:
    __slots__ = ()
    CARRY = 0
    XV = 1
    PARITY = 2
    AUXCARRY = 4
    XK = 5
    ZERO = 6
    SIGN = 7

# Explicitly named states SET and RESET to avoid using magic booleans
class State:
    __slots__ = ()
    SET = True
    RESET = False

# Template argument for all handlers , helps avoid randomised pc increments
# Provides CPU object, and required operands as per size.
class ExecArgs:
    def __init__(self,cpu, arg_sample):
        self.cpu = cpu
        self.arg_sample = arg_sample


class ExecReturn:
    def __init__(self):
        self.events = set()

    def add_event(self,*args):
        self.events.update(args)

# Empty Classes that are used as return objects to make conditional operations idiomatic

class ExecutionSuccessful:
    __slots__ = ()
    pass

class ExecutionFailed:
    __slots__ = ()
    pass

class ExecutionHalted:
    __slots__ = ()
    pass

class ExecutionTerminated:
    __slots__ = ()
    pass

class StepCompleted:
    __slots__ = ()
    pass

class StepSkipped:
    __slots__ = ()
    pass

class InvalidInstruction:
    __slots__ = ()
    pass

class InstructionSuccessful:
    __slots__ = ()
    pass

class BranchingWithoutJump:
    __slots__ = ()
    pass

class BranchingWithJump:
    __slots__ = ()
    pass

class SoftwareInterrupt:
    __slots__ = ()
    pass

class HardwareInterrupt:
    __slots__ = ()
    pass

class ContinueExecution:
    __slots__ = ()
    pass

class StopExecution:
    __slots__ = ()
    pass

class NoOperation:
    __slots__ = ()
    pass

class RegisterUpdate:
    __slots__ = ()
    pass

class MemoryUpdate:
    __slots__ = ()
    pass

class IoUpdate:
    __slots__ = ()
    pass

class UndocumentedOpcode:
    __slots__ = ()
    pass