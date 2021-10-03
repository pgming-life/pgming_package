"""fwmodule_console_progress.py"""

is_release = False

try:
    import practical_package.release as r
except Exception:
    pass
else:
    is_release = r.is_release

if is_release:
    from practical_package.fwmodule_general import *
else:
    # variable route path control for VSCode debug
    import sys, os
    if not [i for i in sys.path if i == os.path.dirname(__file__)]:
        sys.path.append(os.path.dirname(__file__))
    from fwmodule_general import *

"""
    Python Start
"""
def python_start():
    print("\nDo you want to run it?")
    print("Executes when the Enter key is pressed...")
    print("    (  I        I  )")
    print("    (  I   II   I  )")
    print("   ((  I  I  I  I  ))")
    print("  ((  I   I  I   I  ))")
    print(" ((  I   I    I   I  ))")
    print(" ((  I    I  I    I  ))")
    print(" ( (  I   I  I   I  ) )")
    print(" ((( I I   II   I I )))")
    print("  (((I  I  II  I  I)))")
    print("   ([0)  I    I  (0])")
    print("    ((I   I  I   I))")
    print("     ((I        I))")
    print("      ()I      I()")
    print("       ( o    o )")
    input("        (__人__)")
    print("           ((")
    print("            ))")
    print("           ((")

"""
    Python Connection
    details: Connection at the time of calculation result output.
"""
def python_connection():
    print("            ))")
    print("           ((")
    print("            ))")
    print("           ((")

"""
    Sub Calc (Nondeterministic processing)
    details: When the maximum value of range is not decided, it is represented by a guruguru bar.
"""
class python_sub:
    def __init__(self, name_calc):
        self.name_calc = name_calc
        self.g = guruguru()
        
    def start(self):
        print("{}...\r".format(self.name_calc), end="")
    
    def calc(self):
        print("{0}...{1}\r".format(self.name_calc, next(self.g)), end="")
        
    def end(self):
        print("{}...OK!!".format(self.name_calc))

# guruguru bar
def guruguru():
    i = 0
    while 1:
        yield "|/--/"[i % 5]
        i += 1

"""
    Main Calc (Deterministic processing)
    details: Use the tqdm.
"""
#for i in tqdm(range(n)):

"""
    Python End
"""
def python_end():
    print("            ))")
    print("           ((")
    print("            ))")
    print("           ((")
    print("            ))")
    print("           ((")
    print("           )(")
    input("\nThe process is finished.\nCloses the window when the Enter key is pressed...\n\n")
    sys.exit()

"""
    Class Decorator
    details:
    ・Has constructor and destructor functionality.
    ・Use for the Main Function.
"""
def class_decorator(func):
    def wrapper():
        python_start()
        func()
        python_end()
    return wrapper

"""
    Tests
"""
if __name__ == "__main__":
    #from fwmodule_console_progress import *

    # main function
    @class_decorator
    def main_func():
        for i in range(5):
            print("output result: " + str(i))
        python_connection()
        for i in range(5):
            print("output result: " + str(i))
        python_connection()

        # Sub Calc
        sub = python_sub("Sub Calc")
        sub.start()
        for i in range(100):
            sub.calc()
            time.sleep(.01)
        sub.end()
        python_connection()

        # Main Calc
        print("Main Calc")
        for i in tqdm(range(100)):
            time.sleep(.01)
        python_connection()

        # self-made progressbar
        for i in range(1, 21):
            sys.stdout.write("\r[ %-20s %3.0f%% ]" % ("#" * i, i * 100 / 20))
            sys.stdout.flush()
            time.sleep(.1)
        print()
        python_connection()

        # self-made progress moving
        for i in range(1, 51):
            char = "|>-<"[i % 4] 
            sys.stdout.write("\r%s %3.0f%% done %s" % (char * 10, i * 100 / 50, char * 10))
            sys.stdout.flush()
            time.sleep(.1)
        print()

    # execute
    main_func()
    