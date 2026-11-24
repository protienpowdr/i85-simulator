from sim.simapi import State, bytewrap
from sim.parity_table import  PARITY_TABLE


def check_carry_on_add(result):
    if result > 255:
        return State.SET
    return State.RESET


def check_parity(result):
    return PARITY_TABLE[bytewrap(result)]



def check_sign(result):
    if bytewrap(result) & 0b10000000:
        return State.SET

    return State.RESET



def check_zero(result):
    if bytewrap(result) != 0:
        return State.RESET
    return State.SET



def check_auxiliary_add(a,b,result):
    if (a ^ b ^ result) & 0x10:
        return State.SET
    return State.RESET

def check_auxiliary_sub(a,b,result):
    comp2_b = bytewrap(~b)
    if (a ^ comp2_b ^ result) & 0x10:
        return State.SET
    return State.RESET




def check_carry_on_sub(result):
    if result < 0:
        return State.SET
    return State.RESET


def check_overflow_add(a,b,result):

   if (~( a ^ b)) & (a ^ result) & 0x80:
        return State.SET
   return State.RESET

def check_overflow_sub(a,b,result):
    if ( a ^ b) & (a ^ result) & 0x80:
        return State.SET
    return State.RESET


def check_x5(sign_flag,overflow_flag):
    if sign_flag ^ overflow_flag:
        return State.SET
    return State.RESET


# For 16 Bit , mask the integer with 0x8000 , it fixes the ~ error with pythons arbitrary precision integers
def check_overflow_add16(a,b,result):

   if (~( a ^ b)) & (a ^ result) & 0x8000:
        return State.SET
   return State.RESET

def check_overflow_sub16(a,b,result):
    if ( a ^ b) & (a ^ result) & 0x8000:
        return State.SET
    return State.RESET


def check_x5_on_add16(result):
    if result > 0xffff:
        return State.SET
    return State.RESET

def check_x5_on_sub16(result):
    if result < 0:
        return State.SET
    return State.RESET