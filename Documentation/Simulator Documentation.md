# sim85 API Documentation
**sim85** is the custom built simulation engine for i85 Simulator & IDE. 
The `sim` package is dedicated for the sim85 source code and its components.


# Sources

- `core.py` : Main execution loop and test code during development
- `sim`
    - `cpu.py` : Class definition & API for CPU Registers, Memory & IO Ports.
    - `simapi.py` : Functions and Classes that provide different useful utilities.
    - `opcodes.py` : Opcodes stored as integers wrapped in a `Op` class.
    - `instructions.py` : Definition of the `Instruction` class and the `InstructionTable`
    - `functions.py` : Definition of all the handler functions.
    - `parity_table.py` : A list containing parity for all numbers in 0 to 255.
    - `eval_flags.py` : Reusable arithmetic functions for evaluation of flag states.


# CPU Core
`Core` is the class which instantiates the main microprocessor state.  
The microprocessor state and the registers and flags are instance variables, whereas the Memory and IO Ports are
class variables, this is done to logically separate the ownership between the memory modules, io modules and the microprocessor core.  

Moreover, the `Core` class exposes <kbd>@classmethod</kbd> for `memory_read`, `memory_write`, `io_read` and `io_write` , each of these functions take a
reference to the cpu object and follow a hardware accurate access sequence.  

The `Core` class uses `__slots__` hence, adding new attributes to the cpu object during runtime is intentionally prohibited.  

#### Write Operations
1. Load the data in mdr.
2. Load the address in mar.
3. Write data using `memory_read`, `io_write`.

#### Read Operations
1. Load the address in mar.
2. Read data using `memeory_read`, `io_read`.
3. The data is accessible from the mdr. 

#### Register Access and Updates
All register updates are done via  `increment_reg` <kbd>@staticmethod</kbd> or `the increment_pc` , `increment_sp` and `increment_mar` instance methods.
Same for decrementing. 
This is done to prevent off by one, errors especially during increment and decrement operations inside other instructions.  

The class `Core` is defined inside `sim/cpu.py`



# Memory & IO
`MemoryModule` and `IOModule` are classes which define the max addressable ranges of both I/O and Random Access memory at 256 and 65536 bytes respectively.  
The memory storage is implemented as a `bytearray` of the required size.  
The classes `MemoryModule` and `IOModule` are defined inside `sim/cpu.py`



# Registers and Flags
Registers are instance variables of the `Core` object and are standard python integers. The `simapi.py` functions `bytewrap` , `wordwrap` and `gethb` 
are employed to mask the results and thereby keep arithmetic operations frictionless.   
The flag register is a single integer inside the `Core` object named `rf` , the `Core` objects
have instance methods namely `flag_cy` , `flag_z` etc which take a `State.SET` or `State.RESET` argument.  

Each individual flag is set by performing bitwise operations on the flag register rather than storing each flag as a boolean variable.  
The `Core` object also features a `getflag` instance function which takes an argument of `Flag.CARRY` , `Flag.ZERO` , `Flag.AUXCARRY`, `Flag.PARITY`, 
`Flag.SIGN` , `Flag.XV` or `FLAG.XK` to return the corresponding bit.  

**Note : The required flag can be returned as an integer or as a boolean variable using the `as_integer` argument**  
The Flags class contains the bit position of each flag which is used to perform bitwise shifts on the corresponding flag 
to get the required flag.  

Both `State` and `Flag` classes are defined inside `sim/simapi.py`  






