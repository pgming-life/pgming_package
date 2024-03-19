"""fwmodule_general.py"""

import unicodedata

is_release = False

try:
    import practical_package.release as r
except Exception:
    pass
else:
    is_release = r.is_release

if is_release:
    from practical_package.fwdef import *
else:
    # variable route path control for VSCode debug
    import sys, os
    if not [i for i in sys.path if i == os.path.dirname(__file__)]:
        sys.path.append(os.path.dirname(__file__))
    from fwdef import *

"""
    Counter Control
    details:
    ・Count each the count().
    ・Return the previous result with the result().
"""
class counter:
    def __init__(self, radix=0, operand=1, operator="+"):
        self.radix = radix
        self.operand = operand
        self.operator = operator
    def count(self) -> int:
        if self.operator == "+":
            self.radix += self.operand
        elif self.operator == "-":
            self.radix -= self.operand
        elif self.operator == "*":
            self.radix *= self.operand
        elif self.operator == "/":
            self.radix /= self.operand
        elif self.operator == "%":
            self.radix %= self.operand
        elif self.operator == "expo":
            self.radix **= self.operand
        elif self.operator == "root":
            self.radix **= (1 / self.operand)
        else:
            self.radix = None
        return self.radix
    def result(self) -> int:
        return self.radix

"""
    Half Width Count
    details:
        Count half-width intervals.
"""
def half_width_count(char) -> int:
    res = unicodedata.east_asian_width(char)
    if 'F' == res:
        return 2
    elif 'H' == res:
        return 1
    elif 'W' == res:
        return 2
    elif 'Na' == res:
        return 1
    elif 'A' == res:
        return 2
    return 1

"""
    Tests
"""
if __name__ == "__main__":
    #from fwmodule_general import *
    
    # counter
    a = counter()
    x = 2
    b = counter(x, 2, "*")
    for i in range(10):
        c = counter()
        print(a.count())
        b.count()
        c.count()
    print(a.result())
    print(b.result())           # it is not 1024
    print(int(b.result() / x))  # reduce by one dose
    print(c.result())

    # half_width_count
    text = "123１２３ABCＡＢＣ"
    cnt = 0
    for c in text:
        cnt += half_width_count(c)
    print(text)
    print("-" * cnt)
