"""module_bit.py"""

"""
    Bin, Oct, Dec, Hex mutual conversion
    details:
    ・base: radix number (other than Decimal: 0b, 0o, 0x)
    ・radix: 2 | 8 | 10 | 16 (int)
    ・operand: conversion destination (int)
    ・flag_print=True: result print
    ※Return int
    ex) number_conv(base=0b10100, radix=2, operand=16) = 0x14 (return 20(int))
"""
def number_conv(base, radix=16, operand=2, flag_print=False):
    if radix == 10:
        if operand == 2:
            num = bin(base)
            if flag_print:
                print("dec→bin: " + num)
            return int(num, 0)
        elif operand == 8:
            num = oct(base)
            if flag_print:
                print("dec→oct: " + num)
            return int(num, 0)
        elif operand == 16:
            num = hex(base)
            if flag_print:
                print("dec→hex: " + num)
            return int(num, 0)
        else:
            if flag_print:
                print("The operand is incorrect.\nPlease try again.")
    elif radix == 2:
        if operand == 10:
            num = base
            if flag_print:
                print("bin→dec: " + "{}".format(num))
            return num
        elif operand == 8:
            num = oct(base)
            if flag_print:
                print("bin→oct: " + "{}".format(num))
            return int(num, 0)
        elif operand == 16:
            num = hex(base)
            if flag_print:
                print("bin→hex: " + "{}".format(num))
            return int(num, 0)
        else:
            if flag_print:
                print("The operand is incorrect.\nPlease try again.")
    elif radix == 8:
        if operand == 10:
            num = base
            if flag_print:
                print("oct→dec: " + "{}".format(num))
            return num
        elif operand == 2:
            num = bin(base)
            if flag_print:
                print("oct→bin: " + "{}".format(num))
            return int(num, 0)
        elif operand == 16:
            num = hex(base)
            if flag_print:
                print("oct→hex: " + "{}".format(num))
            return int(num, 0)
        else:
            if flag_print:
                print("The operand is incorrect.\nPlease try again.")
    elif radix == 16:
        if operand == 10:
            num = base
            if flag_print:
                print("hex→dec: " + "{}".format(num))
            return num
        elif operand == 2:
            num = bin(base)
            if flag_print:
                print("hex→bin: " + "{}".format(num))
            return int(num, 0)
        elif operand == 8:
            num = oct(base)
            if flag_print:
                print("hex→oct: " + "{}".format(num))
            return int(num, 0)
        else:
            if flag_print:
                print("The operand is incorrect.\nPlease try again.")
    else:
        if flag_print:
            print("The radix is incorrect.\nPlease try again.")

"""
    Bit Shift
    details:
    ・base: radix number (other than Decimal: 0b, 0o, 0x)
    ・shift: int
    ・radix: 2 | 8 | 10 | 16 (int)
    ・lr: left | right (str)
    ・flag_print=True: result print
    ※Return int
    ex) bit_shift(base=0b10100, shift=3) = 0b10 (return 2(int))

"""
def bit_shift(base, shift, radix=2, lr="right", flag_print=False):
    if radix == 10:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if flag_print:
                print("shift radix (dec):       " + num0)
                print("dec left shift (result): " + num1)
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if flag_print:
                print("shift radix (dec):       " + num0)
                print("dec right shift (result): " + num1)
            return int(num1, 0)
        else:
            if flag_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    elif radix == 2:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if flag_print:
                print("shift radix (bin):       " + "{}".format(num0))
                print("bin left shift (result): " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if flag_print:
                print("shift radix (bin):       " + "{}".format(num0))
                print("bin right shift (result): " + "{}".format(num1))
            return int(num1, 0)
        else:
            if flag_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    elif radix == 8:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if flag_print:
                print("shift radix (oct):       " + "{}".format(num0))
                print("oct left shift (result): " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if flag_print:
                print("shift radix (oct):           " + "{}".format(num0))
                print("oct right shift (result):    " + "{}".format(num1))
            return int(num1, 0)
        else:
            if flag_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    elif radix == 16:
        num0 = bin(base)
        if lr == "left":
            num1 = bin(base << shift)
            if flag_print:
                print("shift radix (hex):       " + "{}".format(num0))
                print("hex left shift (result): " + "{}".format(num1))
            return int(num1, 0)
        elif lr == "right":
            num1 = bin(base >> shift)
            if flag_print:
                print("shift radix (hex):       " + "{}".format(num0))
                print("hex right shift (result): " + "{}".format(num1))
            return int(num1, 0)
        else:
            if flag_print:
                print("There is no specification of left shift or right shift.\nPlease try again.")
    else:
        if flag_print:
            print("The radix is incorrect.\nPlease try again.")
        
"""
    Bit Mask
    details:
    ・base: int (other than Decimal: 0b, 0o, 0x)
    ・shift: int
    ・radix: 2 | 8 | 10 | 16 (int)
    ・lr: left | right (str)
    ・flag_print=True: result print
    ※Return int
        ・base(基数)とmask(マスク)への入力は自由でどの進数もint型(10進数はそのままでその他の進数は0b, 0o, 0x表記)
        ・operandへの入力はmaskに乗っ取ったマスクする進数でint型(operandは2進数か16進数しか選べない)(初期値: 16進数)
        ・flag_printがTrueの場合print出力する
        ・print出力結果は入力したoperand(2進数か16進数)の表記となる(戻り値は文字列なのでintでキャストする)
    ex) bit_mask(base=0x01000001, mask=0x000000FF) = 0x1
        bit_mask(base=bit_shift(0x01000001, 24, 16), mask=0x000000FF) = 0x1

"""
def bit_mask(base, mask, operand=16, flag_print=False):
    if operand == 2:
        num0 = bin(base)
        num1 = bin(mask)
        num3 = bin(base & mask)
        if flag_print:
            print("マスク基数(2進数): " + num0)
            print("マスク(2進数)    : " + num1)
            print("2進数マスク(結果): " + "{}".format(num3))
        return int(num3, 0)
    elif operand == 16:
        num0 = hex(base)
        num1 = hex(mask)
        num3 = hex(base & mask)
        if flag_print:
            print("マスク基数(16進数): " + num0)
            print("マスク(16進数)    : " + num1)
            print("16進数マスク(結果): " + "{}".format(num3))
        return int(num3, 0)
    else:
        if flag_print:
            print("2進数か16進数かのマスク指定がありません。\nやり直してください。")

#####################################################################
"""
    テスト

"""
# ↓↓↓直接このファイルを実行したときの処理
if __name__ == "__main__":
    #from module_bit import *

    #--------進数相互変換--------#
    print("●2進数、8進数、10進数、16進数の相互変換")
    print(number_conv(0b10100, 2, 16, flag_print=True))
    print()
    
    #--------ビット操作--------#
    # ビットシフト
    print("●ビットシフト")
    print(bit_shift(0b10100, 3, 2, "right", flag_print=True))
    print()
    
    # ビットマスク
    print("●ビットマスク")
    print(bit_mask(0x01000001, 0x000000FF, 16, flag_print=True))
    print()

    # シフト＆マスク
    print("●シフト＆マスク")
    print(bit_mask(bit_shift(0x01000001, 24, 16, "right", flag_print=True), 0x000000FF, 16, flag_print=True))
    print()
    
    input(">>>\n>>>\n>>>\n処理が終了しました。\n")
    
