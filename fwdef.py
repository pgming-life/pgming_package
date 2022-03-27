"""fwdef.py"""

import os
import sys
import time
from tqdm.autonotebook import tqdm
import subprocess
import ctypes
import _winapi

# subprocess bug fix (EXE)
ctypes.windll.kernel32.SetStdHandle(_winapi.STD_INPUT_HANDLE, 0)

"""
    Naked Decorator
    details: Debug decorator to display function details.
"""
def func_naked(func: "function") -> "function":
    import functools
    @functools.wraps(func)
    def wrapper(*args: "any", **kwargs: "any") -> "any":
        ret = func(*args, **kwargs)
        print("Funcname  : {}".format(func.__name__))
        print("Arguments : {}".format(args))
        print("Keywords  : {}".format(kwargs))
        print("Return    : {}".format(ret))
        return ret
    return wrapper

"""
    Tests
"""
if __name__ == "__main__":
    #from fwdef import *

    @func_naked
    def func(msg1: str, msg2: str, flag=False, mode=3) -> int:
        print(msg1 + " " + msg2)
        return 123456
    
    # execute
    result = func("Hello", "World!", flag=True)
    print(result)
    