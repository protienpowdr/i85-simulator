import re
from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Keyword, Name, Number, Punctuation, Text

class I85Lexer(RegexLexer):

    name = "Intel 8085 Assembly"
    aliases = ["intel8085", "8085", "sim8085"]
    filenames = ["*.asm", "*.8085"]

    # Enable case-insensitivity to handle both 'mov' and 'MOV'
    flags = re.IGNORECASE | re.MULTILINE

    # Complete 8085 Instruction Set Architecture (ISA) Mnemonics
    OPCODES = (
        "ACI", "ADC", "ADD", "ADI", "ANA", "ANI", "CALL", "CC", "CM", "CMA",
        "CMC", "CMP", "CNC", "CNZ", "CP", "CPE", "CPI", "CPO", "CZ", "DAA",
        "DAD", "DCR", "DCX", "DI", "EI", "HLT", "IN", "INR", "INX", "JC",
        "JM", "JMP", "JNC", "JNZ", "JP", "JPE", "JPO", "JZ", "LDA", "LDAX",
        "LHLD", "LXI", "MOV", "MVI", "NOP", "ORA", "ORI", "OUT", "PCHL",
        "POP", "PUSH", "RAL", "RAR", "RC", "RET", "RIM", "RLC", "RM", "RNC",
        "RNZ", "RP", "RPE", "RPO", "RRC", "RST", "RZ", "SBB", "SBI", "SHLD",
        "SIM", "SPHL", "STA", "STAX", "STC", "SUB", "SUI", "XCHG", "XRA",
        "XRI", "XTHL"
    )

    # 8-bit / 16-bit Registers and Status Flags
    REGISTERS = ("A", "B", "C", "D", "E", "H", "L", "M", "SP", "PSW")

    # Standard Assembler Directives
    DIRECTIVES = ("ORG", "EQU", "DB", "DW", "DS", "END")

    tokens = {
        "root": [
            # Whitespace and Single-line Comments
            (r"\s+", Text),
            (r";.*$", Comment.Single),

            # Labels (e.g., 'START:' or 'LOOP_2:')
            # Placed first so keywords inside label names aren't matched as opcodes
            (r"^[A-Za-z_][\w]*:", Name.Label),
            (r"[A-Za-z_][\w]*:", Name.Label),

            # Assembler Directives, Opcodes, and Architecture Registers
            # Bounded by \b to prevent partial matching inside variables
            (words(DIRECTIVES, suffix=r"\b"), Keyword.Directive),
            (words(OPCODES, suffix=r"\b"), Keyword),
            (words(REGISTERS, suffix=r"\b"), Name.Builtin),

            # Numeric constants (Hexadecimal variations: 2000H, 0x2000)
            (r"0[xX][0-9a-fA-F]+\b", Number.Hex),
            (r"[0-9a-fA-F]+[hH]\b", Number.Hex),

            # Numeric constants (Binary, Octal, and standard Base-10 integers)
            (r"[0-1]+[bB]\b", Number.Bin),
            (r"[0-7]+[oO|qQ]\b", Number.Oct),
            (r"\d+", Number.Integer),

            # Operators, Punctuations, and Syntax Structures
            (r"[,:]", Punctuation),

            # Fallback for safe variables, symbols, or un-labelled addresses
            (r"[A-Za-z_][\w]*", Name.Variable),
        ]
    }


