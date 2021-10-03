"""module_bit.py"""

"""
    Bin, Oct, Dec, Hex mutual conversion
    details:
    ・base: radix number (other than Decimal: 0b, 0o, 0x)
    ・radix: 2 | 8 | 10 | 16 (int)
    ・operand: conversion destination (int)
    ・is_print=True: result print
    ※Return int
    ex) number_conv(base=0b10100, radix=2, operand=16) = 0x14 (return 20(int))
"""
def number_conv(base, radix=16, operand=2, is_print=False):
    if radix == 10:
        if operand == 2:
            num = bin(base)
            if is_print:
                print("dec→bin: " + "{}".format(num))
            return int(num, 0)
        elif operand == 8:
            num = oct(base)
            if is_print:
                print("dec→oct: " + "{}".format(num))
            return int(num, 0)
        elif operand == 16:
            num = hex(base)
            if is_print:
                print("dec→hex: " + "{}".format(num))
            return int(num, 0)
        else:
            if is_print:
                print("The operand is incorrect.\nPlease try again.")
    elif radix == 2:
        if operand == 10:
            num = base
            if is_print:
                print("bin→dec: " + "{}".format(num))
            return num
        elif operand == 8:
            num = oct(base)
            if is_print:
                print("bin→oct: " + "{}".format(num))
            return int(num, 0)
        elif operand == 16:
            num = hex(base)
            if is_print:
                print("bin→hex: " + "{}".format(num))
            return int(num, 0)
        else:
            if is_print:
                print("The operand is incorrect.\nPlease try again.")
    elif radix == 8:
        if operand == 10:
            num = base
            if is_print:
                print("oct→dec: " + "{}".format(num))
            return num
        elif operand == 2:
            num = bin(base)
            if is_print:
                print("oct→bin: " + "{}".format(num))
            return int(num, 0)
        elif operand == 16:
            num = hex(base)
            if is_print:
                print("oct→hex: " + "{}".format(num))
            return int(num, 0)
        else:
            if is_print:
                print("The operand is incorrect.\nPlease try again.")
    elif radix == 16:
        if operand == 10:
            num = base
            if is_print:
                print("hex→dec: " + "{}".format(num))
            return num
        elif operand == 2:
            num = bin(base)
            if is_print:
                print("hex→bin: " + "{}".format(num))
            return int(num, 0)
        elif operand == 8:
            num = oct(base)
            if is_print:
                print("hex→oct: " + "{}".format(num))
            return int(num, 0)
        else:
            if is_print:
                print("The operand is incorrect.\nPlease try again.")
    else:
        if is_print:
            print("The radix is incorrect.\nPlease try again.")

"""
    Bit Shift
    details:
    ・base: radix number (other than Decimal: 0b, 0o, 0x)
    ・shift: int
    ・radix: 2 | 8 | 10 | 16 (int)
    ・lr: left | right (str)
    ・is_print=True: result print
    ※Return int
    ex) bit_shift(base=0b10100, shift=3) = 0b10 (return 2(int))
"""
def bit_shift(base, shift, radix=2, lr="right", is_print=False):
    if radix == 10:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if is_print:
                print("shift base (dec):            " + "{}".format(num0))
                print("dec left shift (result):     " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if is_print:
                print("shift base (dec):            " + "{}".format(num0))
                print("dec right shift (result):    " + "{}".format(num1))
            return int(num1, 0)
        else:
            if is_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    elif radix == 2:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if is_print:
                print("shift base (bin):            " + "{}".format(num0))
                print("bin left shift (result):     " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if is_print:
                print("shift base (bin):            " + "{}".format(num0))
                print("bin right shift (result):    " + "{}".format(num1))
            return int(num1, 0)
        else:
            if is_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    elif radix == 8:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if is_print:
                print("shift base (oct):            " + "{}".format(num0))
                print("oct left shift (result):     " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if is_print:
                print("shift base (oct):            " + "{}".format(num0))
                print("oct right shift (result):    " + "{}".format(num1))
            return int(num1, 0)
        else:
            if is_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    elif radix == 16:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if is_print:
                print("shift base (hex):            " + "{}".format(num0))
                print("hex left shift (result):     " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if is_print:
                print("shift base (hex):            " + "{}".format(num0))
                print("hex right shift (result):    " + "{}".format(num1))
            return int(num1, 0)
        else:
            if is_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    else:
        if is_print:
            print("The radix is incorrect.\nPlease try again.")
        
"""
    Bit Mask
    details:
    ・base: int (other than Decimal: 0b, 0o, 0x)
    ・operand: conversion destination (int)
    ・is_print=True: result print
    ※Return int
    ex) bit_mask(base=0x01000001, mask=0x000000FF) = 0x1 (return 1(int))
        bit_mask(base=bit_shift(0x01000001, 24, 16), mask=0x000000FF) = 0x1 (return 1(int))
"""
def bit_mask(base, mask, operand=16, is_print=False):
    if operand == 2:
        num0 = bin(base)
        num1 = bin(mask)
        num2 = bin(base & mask)
        if is_print:
            print("base (bin):          " + "{}".format(num0))
            print("mask (bin):          " + "{}".format(num1))
            print("bin mask (result):   " + "{}".format(num2))
        return int(num2, 0)
    elif operand == 16:
        num0 = hex(base)
        num1 = hex(mask)
        num2 = hex(base & mask)
        if is_print:
            print("base (hex):          " + "{}".format(num0))
            print("mask (hex):          " + "{}".format(num1))
            print("hex mask (result):   " + "{}".format(num2))
        return int(num2, 0)
    else:
        if is_print:
            print("There is no mask specified for binary or hexadecimal.\nPlease try again.")

"""
    Tests
"""
if __name__ == "__main__":
    #from module_bit import *
    
    # mutual conversion
    print("●Bin, Oct, Dec, Hex mutual conversion")
    print(number_conv(0b10100, 2, 16, is_print=True))
    print()
    
    # bit shift
    print("●bit shift")
    print(bit_shift(0b10100, 3, 2, "right", is_print=True))
    print()
    
    # bit mask
    print("●bit mask")
    print(bit_mask(0x01000001, 0x000000FF, 16, is_print=True))
    print()

    # shift and mask
    print("●shift & mask")
    print(bit_mask(bit_shift(0x01000001, 24, 16, "right", is_print=True), 0x000000FF, 16, is_print=True))
    print()
    